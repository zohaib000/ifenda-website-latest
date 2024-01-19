from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("products", products.as_view(), name="products"),
    path("pricing", pricing.as_view(), name="pricing"),
    path("partners", partners.as_view(), name="partners"),
    path("apply_for_partner", apply_for_partner.as_view(), name="apply_for_partner"),
    path("preorder", views.preorder.as_view(), name="preorder"),
    path("about", views.About, name="about"),
    path("contact", views.Contact, name="contact"),
    path("terms", views.Terms, name="terms"),
    path("news", views.news, name="news"),
    path("events", views.events, name="events"),
    # preorder products pages
    path(
        "individual_preorder_products",
        views.individual_preorder_products.as_view(),
        name="individual_preorder_products",
    ),
    path(
        "business_preorder_products",
        views.business_preorder_products.as_view(),
        name="business_preorder_products",
    ),
    # preorder payment pages
    path(
        "individual_preorder_paymentPage",
        views.individual_preorder_paymentPage.as_view(),
        name="individual_preorder_paymentPage",
    ),
    path(
        "business_preorder_paymentPage",
        views.business_preorder_paymentPage.as_view(),
        name="business_preorder_paymentPage",
    ),
    #  pricing pages for free trial
    path(
        "individual_pricing",
        views.individual_pricing.as_view(),
        name="individual_pricing",
    ),
    path(
        "business_pricing",
        views.business_pricing.as_view(),
        name="business_pricing",
    ),
    #    signup pages for both business and individual - when free trial button is
    # clicked
    path(
        "individual_signup",
        views.individual_signup.as_view(),
        name="individual_signup",
    ),
    path(
        "business_signup",
        views.business_signup.as_view(),
        name="business_signup",
    ),
    # about authorization
    path("signup", signup.as_view(), name="signup"),
    path("login", login.as_view(), name="login"),
    # reset passwords urls
    path(
        "request_reset_password",
        request_reset_password.as_view(),
        name="request_reset_password",
    ),
    path(
        "reset_password_response",
        reset_password_response.as_view(),
        name="reset_password_response",
    ),
    path(
        "reset_password_confirm",
        reset_password_confirm.as_view(),
        name="reset_password_confirm",
    ),
]
