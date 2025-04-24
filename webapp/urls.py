"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 


    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('feature_selection/', views.feature_selection, name="feature_selection"),
    path('classification/', views.classification, name="classification"),

    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('dttrain/', views.dttrain, name="dttrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('lrtrain/', views.lrtrain, name="lrtrain"),
    path('evaluation/', views.evaluation, name="evaluation"),

    path('hrlogin/', views.hrlogin, name="hrlogin"),
    path('hrlogout/', views.hrlogout, name="hrlogout"),
    path('hrloginaction/', views.hrloginaction, name="hrloginaction"),
    path('hrhome/', views.hrhome, name="hrhome"),
    
    path('u_loginaction/', views.userloginaction, name="n_loginaction"),
    path('u_signup/', views.signuppage, name="n_signup"),
    
    path('u_userhome/', views.userhomedef, name="userhomedef"),
    path('u_userlogout/', views.userlogoutdef, name="userlogoutdef"),
    path('u_viewprofile/', views.viewprofilepage, name="n_viewprofile"),

    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('updatepwd/', views.updatepwd, name="updatepwd"),
    


    path('attrition/', views.attrition, name="attrition"),

    path('fileupload/', views.fileupload, name="fileupload"),
    path('viewfiles/', views.viewfiles, name="viewfiles"),
    path('viewfile/<str:op>/', views.viewfile, name="viewfile"),
    path('fileupdate/<str:op>/', views.fileupdate, name="fileupdate"),
    path('fileupdateaction/', views.fileupdateaction, name="fileupdateaction"),
    path('chgaccess/<str:op>/', views.chgaccess, name="chgaccess"),
    path('chgaccessaction/', views.chgaccessaction, name="chgaccessaction"),
    
    path('filedownload/', views.filedownload, name="filedownload"),
    path('delete/<str:op>/', views.delete, name="delete"),
    path('search/', views.search, name="search"),
    path('newmail/', views.newmail, name="newmail"),
    path('inbox/', views.inbox, name="inbox"),
    path('viewemp/', views.viewemp, name="viewemp"),    
    path('viewmail/<str:op>/', views.viewmail, name="viewmail"),
    

   
]
