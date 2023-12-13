from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.GetBlogs.as_view()),
    path('blog/<int:pk>', views.GetBlog.as_view()),
    path('add-blog/', views.AddBlog.as_view()),
    path('edit-blog/<int:pk>', views.EditBlog.as_view()),
    path('delete-blog/<int:pk>', views.DeleteBlog.as_view()),
]
