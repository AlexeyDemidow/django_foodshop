from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from sell_food.models import Food


class FoodPageView(DetailView):
    """Представление страницы товара"""

    model = Food
    template_name = 'foodpage.html'
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FoodCatalogView(ListView):
    """Представление каталога товаров"""

    queryset = Food.objects.all()
    context_object_name = 'foods'
    template_name = 'catalog.html'


def food_search(request):
    """Представление поиска товаров с помощью AJAX"""

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        res = None
        food = request.POST.get('food').capitalize()
        querry = Food.objects.filter(name__icontains=food)
        if len(querry) > 0 and len(food) >= 0:
            data = []
            for food_item in querry:
                food_view = {
                    'id': food_item.id,
                    'name': food_item.name,
                    'description': food_item.description,
                    'weight': food_item.weight,
                    'price': food_item.price,
                    'pic': str(food_item.pic.url)
                }
                data.append(food_view)
            res = data
        elif len(querry) == 0 and len(food) > 0:
            res = 'Ничего не найдено'
        return JsonResponse({'data': res})
    return JsonResponse({})
