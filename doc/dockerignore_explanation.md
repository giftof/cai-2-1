# .dockerignore 파일의 역할 및 각 항목 추가 이유

## 1. .dockerignore 파일의 역할

`.dockerignore` 파일은 Docker가 **이미지를 빌드할 때 무시할 파일/디렉토리**를 지정하는 설정 파일이다.  
Docker가 `COPY . .` 등의 명령어를 수행할 때 **불필요한 파일을 빌드 컨텍스트에 포함하지 않도록** 하여 다음을 기대할 수 있다:

- 빌드 속도 향상
- 이미지 용량 감소
- 보안 위험 파일 제외 (예: 인증서, 환경 파일)
- Git 등 불필요한 내부 개발 파일 제외

## 2. 예시와 추가 이유

```dockerignore
__pycache__/
*.pyc
*.pyo
// 컴파일 캐시로, 이미지에 필요하지 않음
*.log
// 로그 파일은 개발 과정 중 생성된 것으로, 배포에 불필요
.env
// 민감한 환경 변수 파일로, 이미지에 포함되면 보안 위험
.git
.gitignore
// Git 관련 파일은 코드 버전 관리를 위한 것이며 이미지에 불필요
Dockerfile
docker-compose.yml
// 컨테이너 생성에 사용되며, 컨테이너 내부에는 필요 없음
README.md
// 실행에는 필요 없음

항목	이유
__pycache__/, *.pyc, *.pyo	Python 컴파일 캐시로, 이미지에 필요하지 않음
*.log	로그 파일은 개발 과정 중 생성된 것으로, 배포에 불필요
.env	민감한 환경 변수 파일로, 이미지에 포함되면 보안 위험
.git, .gitignore	Git 관련 파일은 코드 버전 관리를 위한 것이며 이미지에 불필요
Dockerfile, docker-compose.yml	컨테이너 생성에 사용되며, 컨테이너 내부에는 필요 없음
README.md	문서 파일로 실행에는 필요 없음