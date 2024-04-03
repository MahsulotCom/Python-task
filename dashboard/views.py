from django.db.models import Q, Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CategoryForm, ProductForm, ShopForm, ImageForm
from product.models import Category, Product, Shop, Images


def login_required_decorator(func):
    return login_required(func, login_url="dashboard:login_page")


# Sign Up
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard:login_page")
    template_name = "dashboard/signup.html"


# Login
def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            response = redirect("dashboard:home")
            return response

    return render(request, "dashboard/login.html")


# Logout
@login_required_decorator
def logout_page(request):
    logout(request)
    response = redirect("dashboard:login_page")
    return response


# home page
@login_required_decorator
def home_page(request):
    return render(request, "dashboard/index.html")


#  CATEGORY CONFIGURATION
@login_required_decorator
def category_list(request):
    query = request.GET.get('q')
    categories = Category.objects.all()

    if query:
        categories = categories.filter(
            Q(id__icontains=query) |
            Q(title__icontains=query) |
            Q(parent_category__title__icontains=query)
        )

    context = {
        "categories": categories,
    }
    return render(request, "dashboard/category/list.html", context=context)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:category_list')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/category/form.html', context=context)


@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:category_list')

    context = {
        'form': form,
        'model': model
    }
    return render(request, 'dashboard/category/form.html', context=context)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()

    return redirect("dashboard:category_list")


#  SHOP CONFIGURATION
@login_required_decorator
def shop_list(request):
    query = request.GET.get('q')
    shops = Shop.objects.all().order_by('-created_at')

    if query:
        shops = shops.filter(
            Q(title__icontains=query)
        )

    context = {
        "shops": shops,
        "query": query
    }
    return render(request, "dashboard/shop/list.html", context=context)


@login_required_decorator
def shop_create(request):
    model = Shop()
    form = ShopForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:shop_list')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/shop/form.html', context=context)


@login_required_decorator
def shop_edit(request, pk):
    model = Shop.objects.get(pk=pk)
    form = ShopForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:shop_list')

    context = {
        'form': form,
        'model': model
    }
    return render(request, 'dashboard/shop/form.html', context=context)


@login_required_decorator
def shop_delete(request, pk):
    model = Shop.objects.get(pk=pk)
    model.delete()

    return redirect("dashboard:shop_list")


# PRODUCT CONFIGURATION
@login_required_decorator
def product_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'created_at')
    active_flag = request.GET.get('is_active', 'all')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(id__icontains=query) |
            Q(title__icontains=query)
        )

    if sort_by == 'orders':
        products = products.annotate(order_count=Count('order')).order_by('-order_count', 'price')
    else:
        products = products.order_by(sort_by, '-created_at')

    if active_flag == 'is_active':
        products = products.filter(is_active=True)
    elif active_flag == 'inactive':
        products = products.filter(is_active=False)

    if min_price is not None:
        products = products.filter(price__gte=min_price)
    if max_price is not None:
        products = products.filter(price__lte=max_price)

    context = {
        "products": products,
        "sort_by": sort_by,
        "active_flag": active_flag,
        "min_price": min_price,
        "max_price": max_price
    }
    return render(request, "dashboard/product/list.html", context=context)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:product_list')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/product/form.html', context=context)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        return redirect('dashboard:product_list')

    context = {
        'form': form,
        'model': model,
    }
    return render(request, 'dashboard/product/form.html', context=context)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()

    return redirect("dashboard:product_list")


#  IMAGE CONFIGURATION
@login_required_decorator
def image_list(request):
    images = Images.objects.all()

    context = {
        "images": images,
    }
    return render(request, "dashboard/image/list.html", context=context)


@login_required_decorator
def image_create(request):
    model = Images()
    form = ImageForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:image_list')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/image/form.html', context=context)


@login_required_decorator
def image_edit(request, pk):
    model = Images.objects.get(pk=pk)
    form = ImageForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('dashboard:image_list')

    context = {
        'form': form,
        'model': model
    }
    return render(request, 'dashboard/image/form.html', context=context)


@login_required_decorator
def image_delete(request, pk):
    model = Images.objects.get(pk=pk)
    model.delete()

    return redirect("dashboard:image_list")
