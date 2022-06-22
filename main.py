COOK_BOOK = 'cookbook.txt'

with open(COOK_BOOK, mode='r') as file:
    cook_book = {}
    for text in file.read().split('\n\n'):
        dish_name, _, *args = text.split('\n')
        ingredients = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = ingredients

    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    if type(dishes) == list:
        for dish in dishes:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']

    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
