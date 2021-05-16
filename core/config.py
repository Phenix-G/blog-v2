from pathlib import Path

from pydantic import BaseSettings
from starlette.config import Config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


# class Settings(BaseSettings):
#     ENVIRONMENT: str = None
#
#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'
#         case_sensitive = True
ENVIRONMENT = 'development'

DATABASES = {
    'development': {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'fastapi',
    },
    'production': {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'production',
    },
    'test': {
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'test',
    },
}
# settings = Settings()
