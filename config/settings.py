from pathlib import Path

# 프로젝트의 기본 디렉토리
BASE_DIR = Path(__file__).resolve().parent.parent

# 보안 키
SECRET_KEY = 'django-insecure-ezrvf=(fsir+9l@b)#+xv9vq=!3ou_wld$0m^ar1vnkru6tuuf'

# 디버그 모드
DEBUG = True  # 개발 중에는 True로, 배포 시에는 False로 설정

# 허용된 호스트
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 설치된 앱
INSTALLED_APPS = [
    'corsheaders',  # CORS 설정을 위한 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # API 앱
]

# 미들웨어
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS 관련 미들웨어
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS 설정
CORS_ORIGIN_ALLOW_ALL = True  # 모든 도메인에서 요청 허용 (개발 환경에서만)

# 루트 URL 설정
ROOT_URLCONF = 'config.urls'

# 템플릿 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # 템플릿 디렉토리 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 애플리케이션
WSGI_APPLICATION = 'config.wsgi.application'

# 데이터베이스 설정 (SQLite 사용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 비밀번호 검증
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 언어 및 시간 설정
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 정적 파일 경로
STATIC_URL = 'static/'

# 기본 자동 필드 타입
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
