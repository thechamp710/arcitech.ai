from django.urls import path
from .views import BlogView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog-list-create'),
    path('blog/<int:content_id>/', BlogView.as_view(), name='blog-detail'),
]
