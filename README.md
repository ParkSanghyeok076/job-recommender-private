# 🎓 AI 직무 교육 추천 시스템

AI를 활용하여 직무 설명에 맞는 교육 과정을 추천해주는 웹 애플리케이션입니다.

## ✨ 기능

- 🤖 **AI 기반 추천**: 한국어 문장 임베딩 모델 사용
- 📊 **대용량 데이터**: 2,208개의 교육 과정 데이터베이스 활용
- ⚡ **실시간 분석**: 사용자 입력에 대한 즉시 추천
- 📱 **반응형 디자인**: 모바일/데스크톱 모든 기기 지원
- 🎯 **정확한 매칭**: 코사인 유사도 기반 정밀 추천

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **AI Model**: sentence-transformers (ko-sroberta-multitask)
- **Data Processing**: pandas, scikit-learn, numpy
- **Deployment**: Streamlit Cloud

## 🚀 배포 방법

### Streamlit Cloud 배포 (권장)

1. **GitHub 저장소 생성**
   - [GitHub.com](https://github.com)에 로그인
   - "New repository" 클릭
   - 저장소 이름: `job-recommender`
   - Public으로 설정

2. **파일 업로드**
   - 다음 파일들을 GitHub에 업로드:
     - `streamlit_app.py` (메인 앱)
     - `requirements_streamlit.txt` (패키지 목록)
     - `직무정보DB.csv`
     - `교육정보DB.csv`
     - `README.md`

3. **Streamlit Cloud 배포**
   - [share.streamlit.io](https://share.streamlit.io) 접속
   - GitHub 계정으로 로그인
   - "New app" 클릭
   - Repository: `your-username/job-recommender`
   - Main file path: `streamlit_app.py`
   - "Deploy" 클릭

4. **배포 완료!**
   - `https://your-app-name.streamlit.app` 형태로 링크 생성
   - 이 링크를 공유하면 누구나 사용 가능!

## 💻 로컬 실행

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 패키지 설치
pip install -r requirements_streamlit.txt

# 앱 실행
streamlit run streamlit_app.py
```

## 📁 파일 구조

```
job-recommender/
├── streamlit_app.py           # 메인 Streamlit 애플리케이션
├── requirements_streamlit.txt # Python 패키지 목록
├── 직무정보DB.csv            # 직무 정보 데이터 (1,533개)
├── 교육정보DB.csv            # 교육 정보 데이터 (2,208개)
└── README.md                 # 프로젝트 설명서
```

## 🎯 사용 방법

1. **직무 설명 입력**: 담당하고 있는 직무나 원하는 직무에 대해 자세히 설명
2. **AI 분석**: 시스템이 입력 내용을 분석하여 관련 교육 과정 검색
3. **추천 결과**: 유사도 순으로 상위 5개 교육 과정 추천
4. **상세 정보**: 각 교육 과정의 분류, 교육시간, 유사도 점수 제공

## 💡 사용 팁

- **구체적인 설명**: 직무 내용을 구체적으로 설명할수록 더 정확한 추천
- **기술명 포함**: 사용하는 기술이나 도구명을 포함하면 좋음
- **경험 언급**: 담당 업무나 프로젝트 경험을 언급해보세요

## 📊 데이터 정보

- **직무 정보**: 1,533개의 직무 데이터
- **교육 과정**: 2,208개의 교육 과정 데이터
- **AI 모델**: 한국어 문장 임베딩 모델 (ko-sroberta-multitask)
- **처리 속도**: 평균 2-3초 내 추천 완료

## 🔗 배포 링크

배포가 완료되면 다음과 같은 형태의 링크가 생성됩니다:
```
https://job-recommender-ai.streamlit.app
```

이 링크를 공유하면 **전 세계 누구나 접속하여 사용할 수 있습니다!** 🌍

## 📄 라이선스

MIT License

---

**만든이**: AI 직무 교육 추천 시스템  
**버전**: 1.0.0  
**최종 업데이트**: 2025년 8월 