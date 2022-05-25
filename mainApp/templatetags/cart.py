from django import template
from mainApp.models import Product
register = template.Library()


@register.filter("cartcolor")
def Cartcolor(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        return cart[num][2]
    else:
        return ""


@register.filter("cartsize")
def Cartsize(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        return cart[num][3]
    else:
        return ""


@register.filter('cartQTY')
def CartQTY(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        return cart[num][1]
    else:
        return ""


@register.filter('carttotal')
def Carttotal(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        p = Product.objects.get(id=int(cart[num][0]))
        return cart[num][1]*p.finalprice
    else:
        return ""


@register.filter('cartproductname')
def Cartproductname(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        p = Product.objects.get(id=int(cart[num][0]))
        return p.name
    else:
        return ""


@register.filter("cartproductprice")
def Cartproductprice(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        p = Product.objects.get(id=int(cart[num][0]))
        return p.finalprice
    else:
        return ""


@register.filter("cartproductimage")
def Cartproductimage(request, num):
    cart = request.session.get("cart", None)
    if(cart):
        p = Product.objects.get(id=int(cart[num][0]))
        return p.pic1.url
    else:
        return ""
