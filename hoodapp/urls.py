from django.urls import path,re_path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index, name= "index"),
    path('login/',LoginView.as_view(next_page='index'), name="login"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(next_page ="index"), name="logout"),
    path('profile/',views.profileView, name="profile"),
    path('search/',views.search_business,name ='search'),
    path('post/',views.post,name ='post'),
    path('Bussiness_Post/',views.business_post, name='business_post')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    
