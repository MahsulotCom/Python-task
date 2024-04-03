from django.db.models import Q
from django.shortcuts import render, redirect

from app.forms import EditShopForm, EditProductForm
from app.models import Shop, Product, Category

# Shop view

def shop_view(request):
    shops = Shop.objects.all()
    query = request.GET.get('query')
    if query:
        shops = shops.filter(Q(title__icontains=query))
    return render(request=request,
                  template_name='app/shop.html',
                  context={'shops': shops})


# ------------------------------------------------------------------------------------------

# Products view
def products_view(request):
    products = Product.objects.all()
    query = request.GET.get('query')

    # Filter by title (existing logic)
    if query:
        products = products.filter(Q(title__icontains=query))

    # Filter by price range (new logic)
    price_range = request.GET.get('price_range')
    if price_range:
        try:
            min_price, max_price = map(int, price_range.split('-'))
            if max_price == -1:
                products = products.filter(price__gte=min_price)
            else:
                products = products.filter(price__range=(min_price, max_price))
        except ValueError:
            pass  # Handle potential invalid price range format

    return render(request=request,
                  template_name='app/products.html',
                  context={'products': products})


# ------------------------------------------------------------------------------------------

# Edit shop view

def edit_shop(request, shop_id):
    shop = Shop.objects.filter(id=shop_id).first()

    if request.method == 'POST':
        form = EditShopForm(
            data=request.POST,
            files=request.FILES,
            instance=shop
        )
        if form.is_valid():
            shop = form.save(commit=False)
            shop.save(update_fields=["image", "title", "description"])
            return redirect("index")

    form = EditShopForm(instance=shop)
    return render(request=request, template_name='app/edit_shop.html',
                  context={"form": form})


# ------------------------------------------------------------------------------------------

# Edit product view
def edit_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    shops = Shop.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = EditProductForm(
            data=request.POST,
            files=request.FILES,
            instance=product
        )
        if form.is_valid():
            product = form.save(commit=False)
            # Handle category separately
            product.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect("products")
    else:
        form = EditProductForm(instance=product, initial={'category': product.category.all()})

    return render(request=request, template_name='app/edit_product.html',
                  context={"form": form,
                           "shops": shops,
                           "categories": categories})


# ------------------------------------------------------------------------------------------


# Categories view

def categories_view(request):
    categories = Category.objects.all()
    query = request.GET.get('query')
    if query:
        categories = categories.filter(Q(title__icontains=query) |
                                       Q(parent__title__icontains=query))

    return render(request=request,
                  template_name='app/categories.html',
                  context={'categories': categories})

# ------------------------------------------------------------------------------------------

# 