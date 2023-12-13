from .models import Blog
from .serializer import BlogSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class GetBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


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
