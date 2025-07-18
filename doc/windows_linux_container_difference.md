# Windows의 Docker Desktop에서 리눅스 컨테이너와 윈도우 컨테이너의 차이

Docker Desktop for Windows는 두 가지 유형의 컨테이너 런타임을 지원한다: **리눅스 컨테이너**와 **윈도우 컨테이너**. 이 둘은 구조, 호환성, 성능 등 여러 측면에서 차이를 가진다.

---

## 1. 운영 체제 종속성 (OS Dependency)

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
|------|------------------|------------------|
| 커널 | Linux 커널 사용 (가상화 기반) | Windows NT 커널 사용 |
| 실행 환경 | Linux 기반 이미지만 실행 가능 | Windows 기반 이미지만 실행 가능 |
| 호스트 OS | Windows, macOS, Linux 모두 가능 | Windows에서만 가능 (Server Core, Nano Server 기반) |

---

## 2. 실행 방식

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
|------|------------------|------------------|
| Docker Desktop에서의 동작 | WSL 2 또는 Hyper-V 기반 가상 머신 위에서 실행 | Windows 커널과 직접 통합되어 실행 |
| 시스템 리소스 사용 | 가상 머신 내에서 리눅스 환경으로 동작 | 호스트 Windows 커널을 그대로 사용함 |
| 퍼포먼스 | 가상화 오버헤드가 존재할 수 있음 | 기본적으로 네이티브 실행에 가까움 |

---

## 3. 이미지 및 호환성

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
|------|------------------|------------------|
| 이미지 | Ubuntu, Alpine, CentOS 등 Linux용 이미지 사용 | mcr.microsoft.com/windows/servercore 등 Windows용 이미지 사용 |
| 크로스 플랫폼 | X (리눅스와 윈도우 이미지는 호환되지 않음) | X (리눅스 컨테이너와 상호 전환 불가) |
| 호환성 | 대부분의 오픈소스 애플리케이션과 호환 | Windows 기반 애플리케이션에 특화됨 (IIS, .NET Framework 등) |

---

## 4. 전환 방법

Docker Desktop에서 **컨테이너 유형 전환**은 우측 하단 Docker 아이콘 > “Switch to Windows containers” 또는 “Switch to Linux containers” 메뉴를 통해 가능하다.

- 전환에는 Docker 데몬 재시작이 필요하다.
- 동시에 두 환경을 병렬로 실행할 수는 없다.

---

## 5. 사용 사례

| 리눅스 컨테이너 | 윈도우 컨테이너 |
|----------------|------------------|
| Node.js, Python, Java 등 범용 백엔드 개발 | 기존 Windows 서버 애플리케이션 이식 |
| 마이크로서비스 기반 개발 환경 | 레거시 .NET Framework 기반 시스템 |
| CI/CD 환경 구성 | Windows 전용 실행 환경이 필요한 경우 |

---

## 6. 요약

- **리눅스 컨테이너**는 WSL2 기반의 가상 머신 위에서 실행되며, 범용성과 커뮤니티 지원이 뛰어나다.
- **윈도우 컨테이너**는 Windows 커널에서 직접 실행되며, Windows 환경에 특화된 애플리케이션을 지원한다.
- 두 컨테이너는 상호 호환되지 않으며, 필요에 따라 전환이 필요하다.

---

## 참고

- [Docker 공식 문서: Windows Containers](https://docs.docker.com/desktop/windows/)
- [Microsoft: Windows and Linux Containers](https://learn.microsoft.com/en-us/virtualization/windowscontainers/)

