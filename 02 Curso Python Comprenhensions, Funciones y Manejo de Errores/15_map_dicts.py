def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

items = [
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

new_items = list(map(add_taxes, items))
print(items)
print(new_items)