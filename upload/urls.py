from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('profil/', views.profil, name='profil'),

    # Kawasan Berikat
    path('kawasanberikat/', views.kawasanberikat_view.as_view(),
         name='kawasanberikat'),
    path('kawasanberikat/all', views.kawasanberikat_all_view.as_view(),
         name='kawasanberikat_all_view'),
    path('kawasanberikat/delete/<int:pk>', views.kawasanberikat_delete_view.as_view(),
         name='kawasanberikat_delete'),

    # Upload File
    path('uploadfile/', views.upload_view.as_view(), name='upload_view'),
    path('uploadfile/all', views.upload_all_view.as_view(), name='upload_all_view'),
    path('uploadfile/delete/<int:pk>', views.upload_delete_view.as_view(),
         name='upload_delete'),

    # Login USer
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
