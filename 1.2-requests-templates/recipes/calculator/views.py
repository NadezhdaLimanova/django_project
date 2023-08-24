from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    serving = int(request.GET.get('serving', 1))
    new_dict = {}
    for ingr, amount in DATA.items():
        new_dict[ingr] = {}
        for new_k, new_v in amount.items():
            new_dict[ingr][new_k] = round(new_v * serving, 3)

    context = {
        'recipe': new_dict['omlet'],
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    serving = int(request.GET.get('serving', 1))
    new_dict = {}
    for ingr, amount in DATA.items():
        new_dict[ingr] = {}
        for new_k, new_v in amount.items():
            new_dict[ingr][new_k] = round(new_v * serving, 3)

    context = {
        'recipe': new_dict['pasta'],
    }
    return render(request, 'calculator/index.html', context)

def sandwich(request):
    serving = int(request.GET.get('serving', 1))
    new_dict = {}
    for ingr, amount in DATA.items():
        new_dict[ingr] = {}
        for new_k, new_v in amount.items():
            new_dict[ingr][new_k] = round(new_v * serving, 3)

    context = {
        'recipe': new_dict['sandwich'],
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
