from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import auth
from django.http import JsonResponse


def UserLogin(request):
    return render(request,"UserLogin.html", {'msg':''})

def UserCheckLogin(request):
    useremail = request.POST['useremail']
    userpass = request.POST['userpass']
    try:
        return render(request, "Dashboard.html", {'msg':''})

    except Exception as e:
        print(e)
        return render(request, "UserLogin.html", {'msg': 'Server Error'})

def UserRegisterPage(request):
    return render(request,"UserRegisterPage.html", {'msg':''})

def UserRegister(request):
    userrestroname= request.POST['userrestroname']
    username= request.POST['username']
    useremail= request.POST['useremail']
    usermob= request.POST['usermob']
    userpass= request.POST['userpass']

    try:
        return render(request,"UserRegisterPage.html",{'msg': 'User Registered Sucessfully'})

    except Exception as e:
        print(e)
        return render(request, "UserRegisterPage.html", {'msg': 'Not Registered'})

def UserLogout(request):
    return render(request,"UserLogin.html", {'msg':'Logout Successfully....'})


def UserHome(request):
    return render(request,"Home1.html", {'msg':''})

def UserProducts(request):
    return render(request,"Products.html", {'msg':''})

def UserAbout(request):
    return render(request,"About.html", {'msg':''})

def UserContact(request):
    return render(request,"Contact.html", {'msg':''})

def QR(request):
    return render(request,"QR.html", {'msg':''})

@xframe_options_exempt
def UserMenuCategory(request):
    try:
        return render(request,"menu_category.html", {'msg':''})
    except Exception as e:
        print(e)
        return render(request,"UserLogin.html", {'msg':'Login First..'})

@xframe_options_exempt
def UserMenuCategoryDatabase(request):
    catname = request.POST['cn']
    catdes = request.POST['cd']

    try:
        return render(request, "menu_category.html", {'msg': 'Category Added Sucessfully..'})

    except Exception as e:
        print(e)
        return render(request, "menu_category.html", {'msg': 'Some Error..'})

@xframe_options_exempt
def UserMenuCategoryDisplay(request):

    try:
        return render(request, "menu_category_display.html", {'rows': ''})

    except Exception as e:
        print(e)
        return render(request, "UserLogin.html", {'msg': 'Login First..'})


@xframe_options_exempt
def UserMenuCategoryUpdate(request):

    try:
        return render(request, "menu_category_update.html", {'row': ''})
    except Exception as e:
        print(e)
        return render(request, "UserLogin.html", {'msg': 'Login First..'})

@xframe_options_exempt
def UserMenuCategoryEditDelete(request):
    response = request.POST['btn']
    catid = request.POST['cid']
    catname = request.POST['cn']
    catdes = request.POST['cd']

    try:
        return UserMenuCategoryDisplay(request)

    except Exception as e:
        print(e)
        return UserMenuCategoryDisplay(request)


def UserMenuCategoryJson(request):
    try:
        return JsonResponse(safe=False)

    except:
        return render(request, "menu_category_item.html", {'msg': 'Login First.......'})