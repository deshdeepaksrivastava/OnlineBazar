from django import template
from mainApp.models import CheckoutProducts, checkout
register=template.Library()

@register.filter('checkcolor')
def checkcolor(color,item):
    flag=False
    for i in color.split(","):
        if(i==item):
            flag=True
            break
    return flag

@register.filter('checksize')
def checksize(size,item):
    return item in size

@register.filter('Orderstatus')
def Orderstatus(request,num):
    if(num==0):
        return "Cancelled"
    elif(num==1):
        return "Not Packed"
    elif(num==2):
        return "Packed"
    elif(num==3):
        return "Out For Delivery"
    else:
        return "Delivered"

@register.filter('Paymentstatus')
def Paymentstatus(request,num):
    if(num==1):
        return "Pending"
    else:
        return "Successfull"

@register.filter('PaymentstatusCon')
def PaymentstatusCon(request,num):
    if(num==1):
        return True
    else:
        return False

@register.filter('Orderitem')
def Orderitem(request,num):
    check = checkout.objects.get(id=num)
    p= CheckoutProducts.objects.filter(checkout=check)
    return p


@register.filter('Stock')
def Stock(request,data):
    if(data=="In Stock"):
        return True
    else:
        return False