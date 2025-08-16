import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# 페이지 설정
st.set_page_config(
    page_title="AI 직무 교육 추천 시스템",
    page_icon="🎓",
    layout="wide"
)

# 제목
st.title("🎓 AI 직무 교육 추천 시스템")
st.markdown("직무 설명을 입력하면 AI가 관련 교육 과정을 추천해드립니다!")

# 파일 경로
JOB_DB_PATH = "직무정보DB.csv"
EDU_DB_PATH = "교육정보DB.csv"

@st.cache_resource
def load_model():
    """AI 모델을 로드합니다."""
    with st.spinner("AI 모델을 로딩 중입니다..."):
        model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache_data
def load_data():
    """데이터를 로드합니다."""
    with st.spinner("데이터베이스를 로딩 중입니다..."):
        # 인코딩 목록을 시도해볼 순서대로 정의
        encodings_to_try = ['utf-8-sig', 'utf-8', 'cp949', 'euc-kr']
        
        # 직무정보DB 로드
        job_df = None
        for encoding in encodings_to_try:
            try:
                job_df = pd.read_csv(JOB_DB_PATH, encoding=encoding)
                break
            except UnicodeDecodeError:
                continue
        
        if job_df is None:
            st.error(f"'{JOB_DB_PATH}' 파일을 읽을 수 없습니다.")
            return None, None
        
        # 교육정보DB 로드
        edu_df = None
        for encoding in encodings_to_try:
            try:
                edu_df = pd.read_csv(EDU_DB_PATH, encoding=encoding)
                break
            except UnicodeDecodeError:
                continue
        
        if edu_df is None:
            st.error(f"'{EDU_DB_PATH}' 파일을 읽을 수 없습니다.")
            return None, None
        
        return job_df, edu_df

@st.cache_data
def create_embeddings(model, edu_df):
    """교육 과정명에 대한 임베딩을 생성합니다."""
    with st.spinner("교육 과정 임베딩을 생성 중입니다..."):
        course_names = edu_df.iloc[:, 2].fillna('').tolist()
        embeddings = model.encode(course_names, convert_to_tensor=True, show_progress_bar=True)
        return embeddings

def get_recommendations(model, user_description, edu_df, edu_embeddings, top_k=5):
    """사용자 입력에 대한 추천을 생성합니다."""
    # 사용자 입력을 벡터로 변환
    user_embedding = model.encode(user_description, convert_to_tensor=True)
    
    # 코사인 유사도 계산
    cosine_scores = cosine_similarity(
        user_embedding.reshape(1, -1).cpu().numpy(),
        edu_embeddings.cpu().numpy()
    )
    
    scores = cosine_scores[0]
    top_indices = np.argsort(scores)[-top_k:][::-1]
    
    recommendations = []
    for idx in top_indices:
        course_info = edu_df.iloc[idx]
        recommendations.append({
            'category': course_info.iloc[1],
            'name': course_info.iloc[2],
            'duration': course_info.iloc[3],
            'similarity': round(float(scores[idx]), 4)
        })
    
    return recommendations

# 메인 앱
def main():
    # 모델과 데이터 로드
    model = load_model()
    job_df, edu_df = load_data()
    
    if job_df is None or edu_df is None:
        st.error("데이터 로딩에 실패했습니다.")
        return
    
    # 임베딩 생성
    edu_embeddings = create_embeddings(model, edu_df)
    
    st.success("✅ 모든 준비가 완료되었습니다!")
    
    # 사용자 입력
    st.subheader("📝 직무 설명을 입력해주세요")
    user_description = st.text_area(
        "예시: 웹 개발자로서 React와 Node.js를 사용하여 프론트엔드와 백엔드 개발을 담당하고 있습니다.",
        height=100,
        placeholder="담당하고 있는 직무나 원하는 직무에 대해 자세히 설명해주세요..."
    )
    
    if st.button("🎯 교육 과정 추천받기", type="primary"):
        if user_description.strip():
            with st.spinner("AI가 분석 중입니다..."):
                recommendations = get_recommendations(model, user_description, edu_df, edu_embeddings)
            
            st.subheader("🎓 추천 교육 과정")
            
            for i, rec in enumerate(recommendations, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"**{i}. {rec['name']}**")
                        st.markdown(f"📂 분류: {rec['category']}")
                        st.markdown(f"⏱️ 교육시간: {rec['duration']}")
                    
                    with col2:
                        similarity_percent = rec['similarity'] * 100
                        st.metric("유사도", f"{similarity_percent:.1f}%")
                    
                    st.divider()
        else:
            st.warning("직무 설명을 입력해주세요.")
    
    # 통계 정보
    with st.sidebar:
        st.header("📊 통계 정보")
        st.metric("총 직무 수", len(job_df))
        st.metric("총 교육 과정 수", len(edu_df))
        
        st.header("💡 사용 팁")
        st.markdown("""
        - 구체적으로 직무 내용을 설명할수록 더 정확한 추천을 받을 수 있습니다
        - 사용하는 기술이나 도구명을 포함하면 좋습니다
        - 담당 업무나 프로젝트 경험을 언급해보세요
        """)

if __name__ == "__main__":
    main() 