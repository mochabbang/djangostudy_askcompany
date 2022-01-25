from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.
'''
    Django App Admin 사이트 등록방법 3가지
'''
# 1. admin.site.register([Model Name])
# admin.site.register(Post)

# 2. Model Admin 객체를 받아 생성된 클래스를 파라미터로 전달
#class PostAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Post, PostAdmin)

# 3. 데코레이션 적용 
@admin.register(Post)                   #Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
           return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    # 인자없는 함수 속성 admin사용
    def message_length(self, post):
        return f"{len(post.message)} 글자"
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass