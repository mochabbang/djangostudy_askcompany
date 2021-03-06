from django.urls import re_path, path, register_converter


from . import views

class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(YearConverter, "year")

app_name = "instagram"      # URL Reverse에서 namespace 역할을 맞게 된다

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),    # 포스트(게시판목록의 상세) 내용 확인하는 url
    #re_path(r'(?P<pk>\d+)/$', views.post_detail),
    #path('archives/<int:year>', views.archives_year)
    #re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
    
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_year'),
]
