from django.shortcuts import render
from .models import Category
from cart.cart import Cart


def category(request):
    categories = Category.objects.prefetch_related("products").all()
    context = {"categories": categories}
    return context


def cart(request):
    context = {"cart": Cart(request)}
    return context
