from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
   
    path('',views.searcher,name='aptwebinator-search'),
    path('home/',views.home,name='aptwebinator-home'),
    # path('Tutorials/',views.Tutorials,name='aptwebinator-Tutorials'),
    # path('Reviews/',views.Reviews,name='aptwebinator-Reviews'),
    # path('Information/',views.Information,name='aptwebinator-Information'),
    # path('News/',views.News,name='aptwebinator-News'),
    # path('Socialmedia/',views.Socialmedia,name='aptwebinator-Socialmedia'),
    # path('Shopping/',views.Shopping,name='aptwebinator-Shopping'),
    # path('Others/',views.Others,name='aptwebinator-Others'),
    path('piechart/',views.piechart,name='aptwebinator-piechart')

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)