from django.core import paginator
from django.shortcuts import render,get_object_or_404
from .models import Cars
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def cars(request):
    cars=Cars.objects.order_by('-created_date')
    model_search=Cars.objects.values_list('model',flat=True).distinct()
    city_search=Cars.objects.values_list('city',flat=True).distinct()
    year_search=Cars.objects.values_list('year',flat=True).distinct()
    body_style=Cars.objects.values_list('body_style',flat=True).distinct()
    paginator=Paginator(cars,3)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    data={
        'cars':paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
    }
    return render(request, 'pages/cars.html',data)

def car_detail(request,id):
    single_car=get_object_or_404(Cars,pk=id)

    data={
       'single_car':single_car
    }
    
    return render(request, 'pages/car_detail.html',data)
def search(request):
    cars=Cars.objects.order_by('-created_date')
    model_search=Cars.objects.values_list('model',flat=True).distinct()
    city_search=Cars.objects.values_list('city',flat=True).distinct()
    year_search=Cars.objects.values_list('year',flat=True).distinct()
    body_style=Cars.objects.values_list('body_style',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        if body_style:
            cars=cars.filter(body_style__iexact=body_style)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)
    data={
        'cars':cars,
         'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
    }
    
    return render(request, 'pages/search.html',data)