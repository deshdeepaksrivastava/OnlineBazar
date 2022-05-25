from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_title="OnlineBazar.com"
admin.site.site_header="OnlineBazar.com"
# admin.site.site_url="OnlineBazar.com"

from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('shop/<str:mc>/<str:sc>/<str:br>/', views.shopPage),
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
    path('profile/', views.profilePage),
    path('updateprofile/', views.updateprofilepage),
    path('add-product/',views.addproduct),
    path('delete-product/<int:num>/',views.deleteproduct),
    path('edit-product/<int:num>/',views.editproduct),
    path('single-product-page/<int:num>/',views.singleproductpage),
    path('add-to-wishlist/<int:num>/',views.addtowishlist),
    path('delete-wishlist/<int:num>/',views.deletewishlist),
    path('add-to-cart/',views.addToCart),
    path('cart/',views.cartpage),
    path('update-cart/<str:id>/<str:num>/',views.updatecart),
    path('delete-cart/<str:id>/',views.deletecart),
    path('checkout/',views.checkoutpage),
    path('confirmation/',views.confirmationpage),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccess),
    path('paynow/<int:num>/',views.paynow),
    path('contact/',views.contactpage),
    path('forget-username/',views.forgetusername),
    path('forget-otp/',views.forgetotp),
    path('forget-password/',views.forgetpassword),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
