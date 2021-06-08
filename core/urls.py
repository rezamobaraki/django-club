from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bucket/', views.BucketHome.as_view(), name='bucket_home'),
    path('bucket/delete/<str:key>/', views.BucketDelete.as_view(), name='bucket_delete'),
    path('bucket/download/<str:key>/', views.BucketDownload.as_view(), name='bucket_download'),

]
