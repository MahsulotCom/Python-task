from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Shop, Product, Category, Order
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer, ProductImageSerializer, OrderSerializer



class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Fetch and serialize images for the retrieved product
        product_images = instance.images.all()
        image_serializer = ProductImageSerializer(product_images, many=True)
        serialized_data = serializer.data
        serialized_data['images'] = image_serializer.data
        return Response(serialized_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        product = Product.objects.filter(
                shop=validated_data['shop'],
                categories__in=validated_data['categories'],
                title=validated_data['title'],
                measure=validated_data['measure'],
                price=validated_data['price']
        ).first()

        if product:
            product.amount = validated_data['amount']
            product.save()
            order = product.update_or_create_order(validated_data['amount'], validated_data['price'])
            order_serializer = OrderSerializer(order)
            return Response(order_serializer.data, status=status.HTTP_200_OK)
        else:
            return super().create(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order.update_product_amount()  # Update product amount after order creation
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order.update_product_amount()  # Update product amount after order update
        return Response(OrderSerializer(order).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        product = instance.product
        self.perform_destroy(instance)
        # Restore product amount when order is deleted
        product.amount += instance.amount
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
