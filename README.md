# Feed Service

## Requirements

해당 환경에서 테스트를 진행 하였습니다:

|                | Main version (dev) |
|----------------|--------------------|
| Python         | 3.8                |
| Platform       | AMD64/ARM64(\*)    |
| MySQL          | 8.0                |
| docker-compose | v2.5.0             |

## Getting started

### DB 생성

아래 명령어를 입력하여 PostgreSQL 설치 및 실행 합니다

```
docker-compose up
```

### 가상환경 세팅
```
// 가상환경 생성
python3 -m venv .venv

// 가상환경 활성화
source .venv/bin/activate
```


### 의존성 라이브러리 설치

pip 최신화

```bash
 python3 -m pip install --upgrade pip
```

패키지 관리툴 Poetry를 설치 합니다

```bash
# 설치
pip install poetry

# 명령어 입력 후 프로젝트 관련 정보입력
poetry init

# pyproject.toml 에 있는 필요 라이브러리 설치
poetry install
```

DB 테이블 마이그레이션

```
alembic upgrade head
```

## Run server

```
uvicorn main:app --reload
```

- Test
테스트 파일은 해당 프로젝트 root 경로 기준 'app/tests' 하위에 있으며 서비스 로직, API 요청 모두 테스트 코드를 실행하여 단위 테스트를 진행하실 수 있습니다

``` bash
  cd app/tests
  
  # 해당경로 아래 모든 테스트 케이스 실행
  pytest
```

## APIs
게시글의 경우 삭제 요청 시 DB에서 실제로 삭제되는게 아닌 삭제일을 컬럼을 업데이트 하여 관리하며 댓글은 대댓글 까지만 달 수 있도록 구현되어 있습니다. <br />
<br />
키워드 알림은 테이블, 모델, 리포지토리 구성까지 하였으며 키워드 알림 메서드를 호출하도록 하였고 과제 내용에 따라 실제 알림 보내는 기능은 구현하지 않았습니다.

- Swagger path - 127.0.0.1:8000/docs

- 게시글
    - [GET] /api/v1/feeds - 게시글 목록 조회
    - [POST] /api/v1/feeds - 게시글 등록
    - [PATCH] /api/v1/feeds/{feed_id} - 게시글 수정
    - [PATCH] /api/v1/feeds/{feed_id}/remove - 게시글 삭제 

- 댓글
  - [GET] /api/v1/feeds/{feed_id}/replies - 댓글 목록 조회
  - [POST] /api/v1/feeds/{feed_id}/replies - 댓글 생성