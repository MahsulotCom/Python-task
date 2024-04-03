from django import forms

from app.models import Shop, Product, ProductImage


class EditShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'description', 'image']


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "shop",
            "amount",
            "price",
            "is_available"]



