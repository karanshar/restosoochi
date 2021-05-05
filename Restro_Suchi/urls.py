"""Restro_Suchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from.import MenuCategory
from.import Client
from.import MenuCategoryItems

urlpatterns = [
    path('admin/', admin.site.urls),
    # For Admin
    # For Menu Category
    path('restosoochi/', MenuCategory.UserLogin),
    path('checklogin', MenuCategory.UserCheckLogin),
    path('logout/', MenuCategory.UserLogout),
    path('userregister/', MenuCategory.UserRegisterPage),
    path('register', MenuCategory.UserRegister),
    path('Home/', MenuCategory.UserHome),
    path('Products/', MenuCategory.UserProducts),
    path('About/', MenuCategory.UserAbout),
    path('Contact/', MenuCategory.UserContact),
    path('QR/', MenuCategory.QR),

    path('menucategory/', MenuCategory.UserMenuCategory),
    path('database', MenuCategory.UserMenuCategoryDatabase),
    path('menucategorydisplay/', MenuCategory.UserMenuCategoryDisplay),
    path('menucategoryupdate/', MenuCategory.UserMenuCategoryUpdate),
    path('menucategoryeditdelete', MenuCategory.UserMenuCategoryEditDelete),

    # For Menu_Sub_Category
    path('menucategoryitem/', MenuCategoryItems.UserMenuCategoryItem),
    path('menucategoryitemdatabase', MenuCategoryItems.UserMenuCategoryItemDatabase),
    path('menucategoryitemdisplay/', MenuCategoryItems.UserMenuCategoryItemDisplay),
    path('menucategoryitemupdate/', MenuCategoryItems.UserMenuCategoryItemUpdate),
    path('menucategoryitemeditdelete', MenuCategoryItems.UserMenuCategoryItemEditDelete),

    path('menucategorydatajson/', MenuCategory.UserMenuCategoryJson),


    # For Client Site

    path('menu/', Client.Start),
    path('order', Client.Order),
    path('placeorder/', Client.PlaceOrder)


]
