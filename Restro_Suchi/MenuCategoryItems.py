from django.shortcuts import render
import pymysql as mysql
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def UserMenuCategoryItem(request):
    try:
        return render(request,"menu_category_item.html", {'msg':''})
    except Exception as e:
        print(e)
        return render(request,"UserLogin.html", {'msg':'Login First..'})


@xframe_options_exempt
def UserMenuCategoryItemDatabase(request):
    catid = request.POST['cid']
    itemname = request.POST['itname']
    itemdes = request.POST['itdes']
    pricef = request.POST['fullp']
    priceh = request.POST['halfp']

    try:
        return render(request, "menu_category_item.html", {'msg': 'Item Added Sucessfully..'})

    except Exception as e:
        print(e)
        return render(request, "menu_category_item.html", {'msg': 'Some Error..'})

@xframe_options_exempt
def UserMenuCategoryItemDisplay(request):
    try:
        return render(request, "menu_category_item_display.html", {'rows':''})
    except Exception as e:
        print(e)
        return render(request,"UserLogin.html", {'msg':'Login First..'})

@xframe_options_exempt
def UserMenuCategoryItemUpdate(request):
    try:
        return render(request, "menu_category_item_update.html", {'row': ''})

    except Exception as e:
        print(e)
        return render(request, "UserLogin.html", {'msg': 'Login First..'})


@xframe_options_exempt
def UserMenuCategoryItemEditDelete(request):
    response = request.POST['btn']
    catid = request.POST['cid']
    itemid = request.POST['itemid']
    itemname = request.POST['itemname']
    itemdes = request.POST['itemdes']
    pricef = request.POST['pf']
    priceh = request.POST['ph']

    try:
            return UserMenuCategoryItemDisplay(request)

    except Exception as e:
        print(e)
        return UserMenuCategoryItemDisplay(request)


