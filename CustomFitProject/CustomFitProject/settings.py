
import json
import os
from pathlib import Path
from django.core.mail import send_mail #메일인증

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = os.path.join(BASE_DIR, 'customFit', 'ProductDB.csv')

secret_file = os.path.join(BASE_DIR, 'secret_key.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    return secrets[setting]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    # 추가한 패키지
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',

    'django_filters',

    'corsheaders',

    # 생성한 앱 추가
    'accounts',
    'customFit',
    'myPage',
    
]

AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 추가
    'allauth.account.middleware.AccountMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
]

# 추가 
REST_FRAMEWORK = { 
	'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication', 
    'rest_framework.authentication.SessionAuthentication', #여기꼭추가
    ],
}

# CORS 설정
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React 앱이 실행되는 도메인 추가
]

# 특정 HTTP 메소드만 허용 (필요에 따라 추가/수정)
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# 특정 헤더만 허용 (필요에 따라 추가/수정)
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

ROOT_URLCONF = 'CustomFitProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'CustomFitProject.wsgi.application'

# DATABASES 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#메일인증 코드 꼭 추가!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP 서버
EMAIL_PORT = 587  # TLS 포트
EMAIL_USE_TLS = True  # TLS 사용
EMAIL_USE_SSL = False  # SSL 사용 안 함
EMAIL_HOST_USER = 'fitcustom0@gmail.com'  # Gmail 주소
EMAIL_HOST_PASSWORD = 'tiww xlwl vtit ilho'  # Gmail 비밀번호
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 기본 발신자 이메일

send_mail(
    'Test Subject',
    'This is a test message.',
    'fitcustom0@gmail.com',
    ['recipient-email@example.com'],
    fail_silently=False,
)
#공지에서 이미지 확인 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')