from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as mysql

@xframe_options_exempt
def PlaceOrder(request):
    try:

        return render(request,"placeorder.html", {'srows':'','msg':''})

    except Exception as e:
        print(e)
        return render(request,"placeorder.html", {'srows':'','msg':''})



def Start(request):
    try:
        return render(request,"menupage.html",{'rows':'', 'srows':''})

    except Exception as e:
        print(e)
        return render(request,"menupage.html",{'rows':"", 'srows':"",'msg':''})


@xframe_options_exempt
def Order(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    date = request.POST['date']
    item = request.POST['item']
    plate = request.POST['hf']
    try:
        return render(request,"placeorder.html",{'srows':'', 'msg':'Your Order is Successfully Placed. We will Contact You ASAP...'})

    except Exception as e:
        print(e)
        return render(request,"placeorder.html",{'srows':"" , 'msg':'Error'})
