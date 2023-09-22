from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))

with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = [dict(i) for i in reader]
def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)

    page_stations = paginator.get_page(page_number)
    data = page_stations.object_list
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
         'bus_stations': data,
         'page': page_stations,
    }
    return render(request, 'stations/index.html', context)
