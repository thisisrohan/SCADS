from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>avlb app homepage</h1>")


def detail(request, court_id):
    return HttpResponse("<h1>This is court number :  " + str(court_id) + "</h1>")

def apnd_table(request, time, rpi_data, court_pk):
	court = Court.objects.filter(pk = court_pk)
	table = court.table_set.get(pk = request.POST['table'])
	table.abc.append((time, rpi_data))
	court.is_occupied = rpi_data
	return
