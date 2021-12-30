from pprint import pprint

dishes = []
cook_book = {}


def get_data(file_name):
    n = 0
    person_count = int()
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            dishes.append(line.strip())
            cook_book[dishes[n]] = []
            ingredients = int(file.readline())
            for line_ingredients in range(ingredients):
                ing_list = []
                dish = {}
                for word in file.readline().split(' | '):
                    ing_list.append(word)
                dish["ingredient_name"] = ing_list[0]
                dish["quantity"] = ing_list[1]
                dish["measure"] = ing_list[2]
                cook_book[dishes[n]].append(dish)
            n += 1
            file.readline().strip()
    return cook_book


result = get_data('recipes.txt')
pprint(result)
print()
print()
print()


def get_shop_list_by_dishes(dishes, person_count):
    ing_list = {}
    q = int()

    for dish in dishes:
        if dish in cook_book.keys():
            for ing in cook_book[dish]:
                if ing['ingredient_name'] not in ing_list.keys():
                    ing_list[ing['ingredient_name']] = {}
                    q = int(ing['quantity']) * person_count
                    ing_list[ing['ingredient_name']] = {'quantity': q, 'measure': ing['measure']}
                else:
                    q = int(ing['quantity']) * person_count
                    o = q + ing_list[ing['ingredient_name']]['quantity']
                    ing_list[ing['ingredient_name']] = {'quantity': o, 'measure': ing['measure']}
        else:
            print('error')


    print(ing_list)


get_shop_list_by_dishes(['Фахитос','Запеченный картофель'], 2)



