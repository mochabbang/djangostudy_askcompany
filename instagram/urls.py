from django.urls import  path, register_converter
from instagram.converters import DayConverter, MonthConverter, YearConvert
from . import views

register_converter(YearConvert, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),    # 포스트(게시판목록의 상세) 내용 확인하는 url
    #re_path(r'(?P<pk>\d+)/$', views.post_detail),
    
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_year'),
]
