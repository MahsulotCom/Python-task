import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'conf.settings')
import django
django.setup()

import datetime
from apps.category.models import Category
from apps.order.models import Order, OrderProduct
from apps.product.models import *
from apps.shop.models import Shop
from apps.user.models import AddressModel, User



def create_category():
    Category.objects.all().delete()
    category1 = Category.objects.create(title="Mobile Phone")
    category2 = Category.objects.create(title="Iphone", parent=category1)
    category3 = Category.objects.create(title="Samsung", parent=category1)

def create_shop():
    Shop.objects.all().delete()
    Shop.objects.create(title="Mobile Phones", description="This shop sells mobile phones!", image='fake_images/shop.jpg')
    Shop.objects.create(title="Smart Phones", description="This shop sells smart phones!", image='fake_images/shop.jpg')

def create_user_address():
    User.objects.all().delete()
    AddressModel.objects.all().delete()
    address1 = AddressModel.objects.create(city='Tashkent', district='Chilonzor', is_main=True)
    address2 = AddressModel.objects.create(city='Tashkent', district='Shayxontohur')
    customer = User.objects.create(phone_number='+998901111111', password='ABcd123456', gender=User.FEMALE)
    customer.address.set([address1])
    super_admin = User.objects.create(phone_number='+998902222222', password='ABcd123456', gender=User.MALE, role=User.SUPER_ADMIN)
    super_admin.address.set([address1])
    product_admin = User.objects.create(phone_number='+998903333333', password='ABcd123456', gender=User.MALE, role=User.PRODUCT_ADMIN)
    product_admin.address.set([address2])
    category_admin = User.objects.create(phone_number='+998904444444', password='ABcd123456', gender=User.FEMALE, role=User.CATEGORY_ADMIN)
    category_admin.address.set([address2])
    order_admin = User.objects.create(phone_number='+998905555555', password='ABcd123456', gender=User.MALE, role=User.ORDER_ADMIN)
    order_admin.address.set([address1, address2])

def create_attribute_attribute_value():
    Attribute.objects.all().delete()
    attribute1 = Attribute.objects.create(title='RAM')
    attribute2 = Attribute.objects.create(title='Colour')
    AttributeValue.objects.create(attribute=attribute1, value='8 gb')
    AttributeValue.objects.create(attribute=attribute1, value='16 gb')
    AttributeValue.objects.create(attribute=attribute2, value='White')
    AttributeValue.objects.create(attribute=attribute2, value='Black')

def create_product_variant_discount():
    user1 = User.objects.all().first()
    user2 = User.objects.all().last()
    shop = Shop.objects.all().first()
    category1 = Category.objects.all().first()
    category2 = Category.objects.all().last()
    attribute_value = AttributeValue.objects.all().first()
    Product.objects.all().delete()
    Discount.objects.all().delete()
    Order.objects.all().delete()
    product1 = Product.objects.create(title='Iphone 8', shop=shop, image='fake_images/phone1.jpeg', price=3200000.00)
    product2 = Product.objects.create(title='Samsung ~&', shop=shop, image='fake_images/phone2.jpg', price=2200000.00)
    product1.category.set([category1])
    product2.category.set([category2])
    product_variant1 = ProductVariant.objects.create(product=product1, title='iphone 8 gb', price=3500000.00, quantity=25)
    product_variant1.attribute_value.set([attribute_value])
    product_variant2 = ProductVariant.objects.create(product=product2, title='samsung 8 gb', price=3000000.00, quantity=20)
    product_variant2.attribute_value.set([attribute_value])
    ProductVariantImage.objects.create(product_variant=product_variant1, image='fake_images/phone2.jpg')
    ProductVariantImage.objects.create(product_variant=product_variant2, image='fake_images/phone1.jpeg')
    start_date = datetime.date(2024, 3, 20)
    end_date = datetime.date(2024, 5, 5)
    discount1 = Discount.objects.create(name="Discount for holiday!", percent=12, start_date=start_date, end_date=end_date )
    discount2 = Discount.objects.create(name="Discount for Navruz!", percent=12, start_date=start_date, end_date=end_date )
    discount1.product_variant.set([product_variant1])
    discount2.product_variant.set([product_variant2])
    order1 = Order.objects.create(user=user1)
    order2 = Order.objects.create(user=user2)
    OrderProduct.objects.create(order=order1, product_variant=product_variant1, quantity=3)
    OrderProduct.objects.create(order=order2, product_variant=product_variant2, quantity=4)


create_category()
create_shop()
create_user_address()
create_attribute_attribute_value()
create_product_variant_discount()