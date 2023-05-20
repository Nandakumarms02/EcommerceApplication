from django.urls import path
from app import views
from django.contrib.auth import views as auth_view
from app.forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm


urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('category-title/<val>',views.CategoryTitle.as_view(),name='category-title'),
    path('product-detail/<int:id>',views.ProductDetail.as_view(),name='product-detail'),
    path('profile/',views.profileview,name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:id>',views.updateAddress,name='updateAddress'),
    

    #login authentication
    path('registration',views.customerregistrationview,name='registration'),
    # buitin path for login--the redirect url is set in settings.py
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    # password-reset--(forgot-password)
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    path('add-to-cart/<int:id>',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('checkout/',views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
    path('orders/',views.orders, name='orders'),
    
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    

    path('search/',views.search,name='search'),


]