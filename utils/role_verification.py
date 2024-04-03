from fastapi import HTTPException


def roll_verification(user, function):
    allowed_functions_for_shop_admin = ['all_shops', 'one_shop', 'add_shop', 'update_shop',
                                        'delete_shop']
    allowed_functions_for_product_admin = ['all_products', 'one_product', 'add_product', 'update_product',
                                           'delete_product']
    allowed_functions_for_category_admin = ['all_categorys', 'one_category', 'add_category', 'update_category',
                                            'delete_category']

    if user.roll == "Admin":
        return True
    elif user.roll == "Shop_admin" and function in allowed_functions_for_shop_admin:
        return True
    elif user.roll == "Category_admin" and function in allowed_functions_for_category_admin:
        return True
    elif user.roll == "Product_admin" and function in allowed_functions_for_product_admin:
        return True
    raise HTTPException(status_code=400, detail='Sizga ruhsat berilmagan!')
