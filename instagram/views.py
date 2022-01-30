from http.client import HTTPResponse
from pyexpat import model
from django.http import Http404, HttpRequest, HttpResponse
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)


# Create your views here.
# def post_list(request):
#     qs = Post.objects.all()
    
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })

# post_detail = DetailView.as_view(model=Post,
#                                  queryset=Post.objects.filter(is_public=True))   

class PostDetailView(DetailView):
    model = Post
  # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)        
        return qs

post_detail = PostDetailView.as_view()

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     #try:
#     #    post = Post.objects.get(pk=pk)  # Post.DoesNotExists 예외
#     #except:
#     #    raise Http404
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })
