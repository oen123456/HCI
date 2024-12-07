from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # 메인 페이지 응답 생성용
from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')  # 템플릿 렌더링

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin URL
    path('api/', include('api.urls')),  # API URL 연결
    path('', home_view, name='home'),  # 기본 경로 처리
]
