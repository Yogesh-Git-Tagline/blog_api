from .models import Blog
from .serializer import BlogSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from .pagination import Paginate


class GetBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = SearchFilter, OrderingFilter
    search_fields = ['title', 'author__username']
    ordering_fields = ['title', 'created_at']
    pagination_class = Paginate


class GetBlog(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class AddBlog(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class EditBlog(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DeleteBlog(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
