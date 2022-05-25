from django.contrib import admin
from .models import *

# admin.site.register((
#     Maincategory,
#     Subcategory,
#     Brand,
#     Product,
#     Seller,
#     Buyer,
#     Wishlist,
#     checkout,
#     CheckoutProducts,
#     Newsletter,
#     Contact
# ))



@admin.register(Maincategory)
class MaincategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id','name','username','email','phone','addressline1','addressline2','addressline3','pin','city','state','pic']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','maincategory','subcategory','brand','color','size','baseprice','discount','finalprice','stock','pic1']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id','name','username','email','phone','addressline1','addressline2','addressline3','pin','city','state','pic']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id','buyer','product']

@admin.register(checkout)
class checkoutAdmin(admin.ModelAdmin):
    list_display = ['id','buyer','mode','orderstatus','paymentstatus','total','shipping','final','date']


@admin.register(CheckoutProducts)
class CheckoutProductsAdmin(admin.ModelAdmin):
    list_display = ['id','checkout','name','size','color','price','qty','total','pic']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','status']

