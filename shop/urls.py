from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homefn),
    path('register/',registerfn),
    path('login/',loginfn),
    path('addproduct/',addproductfn),
    path('viewcategory/<int:cid>',viewcategoryfn),
    path('viewproduct/<int:pid>',viewproductfn),
    path('editproduct/<int:pid>',editproductfn),
    path('deleteproduct/<int:pid>',deleteproductfn),
    path('search/',searchfn),
    path('logout/',logoutfn),
    path('profile/',profile),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)