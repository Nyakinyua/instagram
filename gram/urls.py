from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    url(r"^$",views.home,name="home"),
    path("news_feed/",views.news_feed,name="news_feed"),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit,name='edit'),
    path('search/', views.search_results, name="search_results"),
     path('one_post/<int:id>',views.one_post,name="one_post"),
    url(r'upload$',views.uploads,name='uploads'),
    url(r'^logout/home$',views.logout_user,name="logout_user"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)