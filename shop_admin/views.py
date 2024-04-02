from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Category, Shop, Product
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CategoryListView(ListView):
    queryset=Category.objects.all()
    template_name = 'category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Category.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        context['categories'] = queryset
        return context
    
class CategoryUpdateView(UpdateView):
    queryset=Category.objects.all()
    template_name='update.html'
    fields=['title', 'description', 'parents']
    success_url = reverse_lazy('home_page') 
    
class CategoryDeleteView(DeleteView):
    model=Category
    template_name='delete.html'
    context_object_name='obj'
    success_url = reverse_lazy('home_page') 
    
class ShopListView(ListView):
    queryset=Shop.objects.all()
    template_name = 'shop.html'
    context_object_name = 'shops'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Shop.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        context['shops'] = queryset
        return context
    
class ShopUpdateView(UpdateView):
    queryset=Shop.objects.all()
    template_name='shop_update.html'
    fields=['title', 'description', 'image_url']
    success_url = reverse_lazy('shops_page') 
    
class ShopDeleteView(DeleteView):
    model=Shop
    template_name='delete.html'
    context_object_name='obj'
    success_url = reverse_lazy('shops_page') 
    

class ProductListView(ListView):
    queryset=Product.objects.all()
    template_name = 'product.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        
    
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        
        
  
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'category_asc':
            queryset = queryset.order_by('category')
        elif sort_by == 'category_desc':
            queryset = queryset.order_by('-category')
            
        elif sort_by == 'title_asc':
            queryset = queryset.order_by('title')
        elif sort_by == 'title_desc':
            queryset = queryset.order_by('-title')
            
        elif sort_by == 'description_asc':
            queryset = queryset.order_by('description')
            
        elif sort_by == 'description_desc':
            queryset = queryset.order_by('-description')
            
        elif sort_by == 'amount_asc':
            queryset = queryset.order_by('amount')
            
        elif sort_by == 'amount_desc':
            queryset = queryset.order_by('-amount')
            
        elif sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')
            
        elif sort_by == 'active_asc':
            queryset = queryset.order_by('active')
        elif sort_by == 'active_desc':
            queryset = queryset.order_by('-active')
            
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__range=(min_price, max_price))

        return queryset
    
    
class ProductUpdateView(UpdateView):
    queryset=Product.objects.all()
    template_name='product_update.html'
    fields=['title', 'description', 'amount', 'price', 'active']
    success_url = reverse_lazy('products_page') 
    
class ProductDeleteView(DeleteView):
    model=Product
    template_name='delete.html'
    context_object_name='obj'
    success_url = reverse_lazy('products_page') 