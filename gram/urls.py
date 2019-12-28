from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('profile/<int:id>',views.profile,name='profile'),
     path('search/', views.search_results, name="search_results"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)