from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='+')
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Java, .Net ToString()
    def __str__(self):
        #return "Custom Post object ({})".format(self.id)
        #return f"Cutom Post object ({self.id})" # Python 3.7 이후
        return self.message
    
    class Meta:
        ordering =  ['-id']
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True},) # post_id 필드가 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
        pass
    
