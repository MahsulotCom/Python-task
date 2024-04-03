from fastapi import HTTPException


def roll_verification(user, function):
    allowed_functions_for_shop_admin = ['all_shop', 'one_shop', 'shop_add', 'shop_update',
                                        'shop_delete']
    allowed_functions_for_product_admin = ['all_product', 'one_product', 'product_add', 'product_update',
                                           'product_delete']
    allowed_functions_for_category_admin = ['all_category', 'one_category', 'category_add', 'category_update',
                                            'category_delete']

    if user.roll == "Admin":
        return True
    elif user.roll == "Shop_admin" and function in allowed_functions_for_shop_admin:
        return True
    elif user.roll == "Category_admin" and function in allowed_functions_for_category_admin:
        return True
    elif user.roll == "Product_admin" and function in allowed_functions_for_product_admin:
        return True
    raise HTTPException(status_code=400, detail='Sizga ruhsat berilmagan!')
