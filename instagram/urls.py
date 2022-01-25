from django.urls import  path

from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),    # 포스트(게시판목록의 상세) 내용 확인하는 url
    #re_path(r'(?P<pk>\d+)/$', views.post_detail),
]
