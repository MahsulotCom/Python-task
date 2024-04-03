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


# This function calculates total discount of each product variant. For example, if customer orders 9 of one product,
# discount price is equal to 9 * product_discount
def calc_discount_total_price(product: ProductVariant, quantity: int, user: User):
    today = datetime.now().date()
    total_price = None
    product_discount = Discount.objects.filter(
        product__in=[product.product], start_date__lte=today, end_date__gte=today
    )
    variant_discount = Discount.objects.filter(
        product_variant__in=[product], start_date__lte=today, end_date__gte=today
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


# This function calculated total price of all products ordered. For example, if customer orders 3 balls, 4 shoes,
# the function calculates the sum of the price to be paid for all the products
def calc_order_total_prices(order: Order):
    output_field = DecimalField(max_digits=21, decimal_places=2)
    products = OrderProduct.objects.filter(order=order)
    price = products.aggregate(sum_price=Coalesce(Sum('total_price'), 0, output_field=output_field))
    discount = products.aggregate(sum_discount=Coalesce(Sum('discount_price'), 0, output_field=output_field))
    order.total_price = price['sum_price']
    order.total_discount = discount['sum_discount']
    order.price_to_pay = order.total_price - order.total_discount
    order.save()


# This function calculates the price to be paid for one product, it also updates product variant info in database,
# if the product details are updated.
def update_order_product(user: User, order_product: OrderProduct, quantity: int):
    if order_product.product_variant.quantity < order_product.quantity:
        raise Exception(f"Only {order_product.product_variant.quantity} products left in store! Please order less products!")
    else:
        product_variant = order_product.product_variant
        product_variant.quantity -= order_product.quantity
        product_variant.save(update_fields=['quantity'])
        order = order_product.order
        order_product.quantity = quantity
        order_product.total_price = order_product.product_variant.price * quantity
        order_product.discount_price = calc_discount_total_price(order_product.product_variant, quantity, user)


# this function is used to update order prices, if a product is removed from order
def deleted_order_product(order_product: OrderProduct):
    order = order_product.order
    calc_order_total_prices(order)