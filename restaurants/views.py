from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def restaurants_list(request):
	return render(request, 'html_task.html')
