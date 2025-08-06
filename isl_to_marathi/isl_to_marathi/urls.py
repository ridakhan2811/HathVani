from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  


urlpatterns = [
    path('', views.index, name='home'),
    path('predict/', views.predict_api, name='predict_api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
