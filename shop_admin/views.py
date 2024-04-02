from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Category
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.



class CategoryListView(ListView):
    queryset=Category.objects.all()
    template_name = 'base.html'
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