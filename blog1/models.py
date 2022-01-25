from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# SQL 모델 생성 구성
#   python manage.py makemigrations [AppName]
#   python manage.py migrate [AppName]
#       * 정방향이란? 
#           - 원래 순서대로의 모델 클래스 구성 및 테이블 구현
#       * 역방향도 존재!
#           - 역방향은 정방향의 반대로 이전 버전의 테이블 구조 및 스키마로 되돌아간다. (Un-do)
#           - python manage.py migrate [AppName] [Migration-Name]
#       * 마이그레이션 이름 지정 
#           - 전체 이름(파일명)을 지정하지 않더라도, 1개를 판별할 수 있는 일부만 지정해도 판단하에 진행된다.
#           - ex) python manage.py migrate blog 000     # Fail (기본적으로 일치하는 값들 여러개 있을 경우)
#                 python manage.py migrate blog 0001    # OK