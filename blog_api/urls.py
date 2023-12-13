from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.GetBlogs.as_view()),
    path('blog/<int:pk>', views.GetBlog.as_view()),
    path('blog/', views.AddBlog.as_view()),
    path('blog/<int:pk>', views.EditBlog.as_view()),
    path('blog/<int:pk>', views.DeleteBlog.as_view()),
]
