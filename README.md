# Chat Template logger

## 프로젝트 개요

우리는 매일 ChatGPT, Claude 등의 AI 챗봇을 사용하며 무의식적으로 양질의 데이터를 생성하고 있습니다. 하지만 대부분의 경우, 이렇게 만들어진 귀중한 데이터들은 저장되지 않고 사라지고 맙니다. 이 프로젝트는 사용자가 AI와의 대화를 통해 만든 양질의 데이터셋을 쉽게 정리하고 저장할 수 있도록 돕는 간단한 웹 애플리케이션입니다.

Chat Template logger를 사용하면 사용자와 AI 사이의 대화를 ChatTemplate 형식의 JSON으로 저장할 수 있습니다. 이를 통해 사용자는 자신만의 고유한 데이터셋을 구축하고 관리할 수 있습니다.

## 기능

- 사용자 입력과 AI 응답을 텍스트 영역에 입력
- 입력된 대화를 ChatTemplate JSON 형식으로 저장
- 저장된 JSON 파일 목록 확인
- 선택한 JSON 파일의 내용 확인

## 설치 방법

1. 이 저장소를 클론합니다:
   ```
   git clone https://github.com/daje0601/chat_template_logger.git
   cd chat_template_logger
   ```

2. 가상 환경을 생성하고 활성화합니다 (선택사항이지만 권장):
   ```
   python -m venv venv
   source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
   ```

3. 필요한 라이브러리를 설치합니다:
   ```
   pip install streamlit
   ```

## 사용 방법

1. 다음 명령어로 Streamlit 앱을 실행합니다:
   ```
   streamlit run app.py
   ```

2. 웹 브라우저에서 표시된 로컬 URL을 엽니다 (보통 http://localhost:8501).

3. "Human Input" 텍스트 영역에 사용자의 입력을 입력합니다.

4. "AI Output" 텍스트 영역에 AI의 응답을 입력합니다.

5. "Save" 버튼을 클릭하여 대화를 JSON 파일로 저장합니다.

6. "Saved Data" 섹션에서 저장된 파일을 선택하여 내용을 확인할 수 있습니다.

## 기여하기

프로젝트 개선에 관심이 있으시다면 언제든 풀 리퀘스트를 보내주세요. 큰 변경사항의 경우, 먼저 이슈를 열어 논의해 주시기 바랍니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.