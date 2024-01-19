from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
import time


def getIndividualPricing(model, product_plan):
    obj = model.objects.get(product_plan=product_plan)
    obj_dict = {field.name: getattr(obj, field.name) for field in obj._meta.fields}
    print(obj_dict)
    return obj_dict


def getBusinessPricing(model, product_name):
    obj = model.objects.get(product_name=product_name)
    obj_dict = {field.name: getattr(obj, field.name) for field in obj._meta.fields}
    print(obj_dict)
    return obj_dict


class preorder(View):
    def get(self, request):
        return render(request, "home/preorder.html")


#  preorder product pages
class individual_preorder_products(View):
    def get(self, request):
        product = request.GET.get("product")
        if product == "personal":
            context = getIndividualPricing(Individual_Pricing, "Personal")
            return render(request, "home/individual_preorder_paymentPage.html", context)

        elif product == "family":
            context = getIndividualPricing(Individual_Pricing, "Family")
            return render(request, "home/individual_preorder_paymentPage.html", context)
        return render(request, "home/individual_preorder_products.html")


class business_preorder_products(View):
    def get(self, request):
        product = request.GET.get("product")
        if product == "api":
            context = getBusinessPricing(Business_Pricing, "iFender Defense Api")
            return render(request, "home/business_preorder_paymentPage.html", context)

        elif product == "browser":
            context = getBusinessPricing(Business_Pricing, "iFender Browser Defense")
            return render(request, "home/business_preorder_paymentPage.html", context)
        return render(request, "home/business_preorder_products.html")


#  pricing pages for free trials
class business_pricing(View):
    def get(self, request):
        # product = request.GET.get("product")
        # if product == "api":
        #     context = getBusinessPricing(Business_Pricing, "iFender Defense Api")
        #     return render(request, "home/business_preorder_paymentPage.html", context)

        # elif product == "browser":
        #     context = getBusinessPricing(Business_Pricing, "iFender Browser Defense")
        #     return render(request, "home/business_preorder_paymentPage.html", context)
        return render(request, "home/business_pricing.html")


class individual_pricing(View):
    def get(self, request):
        # product = request.GET.get("product")
        # if product == "api":
        #     context = getBusinessPricing(Business_Pricing, "iFender Defense Api")
        #     return render(request, "home/business_preorder_paymentPage.html", context)

        # elif product == "browser":
        #     context = getBusinessPricing(Business_Pricing, "iFender Browser Defense")
        #     return render(request, "home/business_preorder_paymentPage.html", context)
        return render(request, "home/individual_pricing.html")


#  signup pages for both individual and business
class individual_signup(View):
    def get(self, request):
        return render(request, "home/individual_signup.html")


class business_signup(View):
    def get(self, request):
        return render(request, "home/business_signup.html")


# preorder payment pages for both individual & business
class individual_preorder_paymentPage(View):
    def get(self, request):
        return render(request, "home/individual_preorder_paymentPage.html")


class business_preorder_paymentPage(View):
    def get(self, request):
        return render(request, "home/business_preorder_paymentPage.html")


class signup(View):
    def get(self, request):
        return render(request, "home/signup.html")


class login(View):
    def get(self, request):
        return render(request, "home/login.html")


class home(View):
    def get(self, request):
        return render(request, "home/index.html")


class products(View):
    def get(self, request):
        product = request.GET.get("product")
        if product == "api":
            return render(request, "home/product_api.html")
        return render(request, "home/products.html")


class pricing(View):
    def get(self, request):
        return redirect("individual_pricing")


class partners(View):
    def get(self, request):
        return render(request, "home/partners.html")


class apply_for_partner(View):
    def get(self, request):
        return render(request, "home/partnerForm.html")


# chrome profiles handling
def Contact(request):
    return render(request, "home/contact.html")


def About(request):
    return render(request, "home/about.html")


def Terms(request):
    return render(request, "home/terms.html")


def news(request):
    return render(request, "home/news.html")


def events(request):
    return render(request, "home/events.html")


class request_reset_password(View):
    def post(self, request):
        return redirect("reset_password_response")

    def get(self, request):
        return render(request, "home/request_reset_password.html")


class reset_password_response(View):
    def get(self, request):
        return render(request, "home/reset_password_response.html")


class reset_password_confirm(View):
    def get(self, request):
        return render(request, "home/reset_password_confirm.html")
