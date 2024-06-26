from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('', views.index, name="index"),
    path('registration',views.registration,name="registration"),
    path('newspaper',views.newspaper,name="newspaper"),
    path('pomplet',views.pomplet,name="pomplet"),
    path('writer',views.writer,name="writer"),
   # path('index',views.index,name="index"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('horror',views.horror,name="horror"),
    path('action',views.action,name="action"),
    path('devotional',views.devotional,name="devotional"),
    path('instagram',views.instagram,name="instagram"),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

