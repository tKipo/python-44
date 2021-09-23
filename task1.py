product = input('Insert the product:\n')
"""
milk == 3
butter == 5
bread == 7
"""
shop_items = {
    'milk': 3,
    'butter': 5,
    'bread': 7
}
print(shop_items.get(product.lower(), -1))
