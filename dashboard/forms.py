from django import forms
from product.models import Category, Product, Images, Shop

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "parent": forms.Select(attrs={'class': 'form-control'}),
        }


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "amount": forms.NumberInput(attrs={'class': 'form-control'}),
            "images": forms.Select(attrs={'class': 'form-control'}),
            "category": forms.SelectMultiple(attrs={'class': 'form-control'}),
            "shop": forms.Select(attrs={'class': 'form-control'}),
            "is_active": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = "__all__"
        widgets = {
            "product": forms.Select(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control', 'onchange': 'loadFile(event)'}),
            "is_main": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


