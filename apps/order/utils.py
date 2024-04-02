# Python
from datetime import datetime
from decimal import Decimal

# Django
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

# Project
from apps.order.models import Order, OrderProduct
from apps.user.models import User
from apps.product.models import ProductVariant, Discount

def calc_discount_total_price(product: ProductVariant, quantity: int, user: User):
    today = datetime.now().date()
    total_price = None
    product_discount = Discount.objects.filter(
        products__in=[product.product], start_date__lte=today, end_date__gte=today
    )
    variant_discount = Discount.objects.filter(
        product_variants__in=[product], start_date__lte=today, end_date__gte=today
    )
    discount = product_discount if product_discount.exists() else variant_discount
    if discount.exists():
        discount = discount.first()
        if discount.amount:
            total_price = discount.amount * quantity
        elif discount.percent:
            amount = product.price * discount.percent / 100
            total_price = amount * quantity

    return total_price


def calc_order_total_prices(order: Order):
    output_field = DecimalField(max_digits=21, decimal_places=2)
    products = OrderProduct.objects.filter(order=order)
    price = products.aggregate(sum_price=Coalesce(Sum('total_price'), 0, output_field=output_field))
    discount = products.aggregate(sum_discount=Coalesce(Sum('discount_price'), 0, output_field=output_field))
    order.total_price = price['sum_price']
    order.total_discount = discount['sum_discount']
    order.price_to_pay = order.total_price - order.total_discount
    order.save(update_fields=['total_price', 'total_discount', 'price_to_pay'])


def add_order_product(
        user: User,
        product: ProductVariant,
        quantity: int,
        order: Order = None
):
    if OrderProduct.objects.filter(order=order, product=product).exists():
        raise Exception('Product already exists!')
    OrderProduct.objects.create(
        order=order, product=product, quantity=quantity, total_price=(product.price * quantity),
        discount_price=calc_discount_total_price(product, quantity, user)
    )
    calc_order_total_prices(order)



def update_order_product(user: User, order_product: OrderProduct, quantity: int):
    order = order_product.order
    order_product.quantity = quantity
    order_product.total_price = product.price * quantity
    order_product.discount_price = calc_discount_total_price(order_product.product, quantity, user)
    order_product.save()
    calc_order_total_prices(order)

def deleted_order_product(order_product: OrderProduct):
    order = order_product.order
    calc_order_total_prices(order)