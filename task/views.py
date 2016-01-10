from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from task.models import Restaurant
from task.models import MenuItem

import json

def index(request):
	if request.method == 'GET':
		req_type =  request.GET.get("type", "")
		print req_type
		if req_type == "rest":
			rest_id = request.GET.get("id","")

			rest_name = Restaurant.objects.get(id = int(rest_id))
			menu = []
			menu_items = MenuItem.objects.filter(restaurant = rest_name)
			for each in menu_items:
				menu.append({'Food':each.item,'Price':each.price})

		result = {}
		result={'RestaurantName':rest_name.name,'Menu':menu}

		return HttpResponse(json.dumps(result))

	elif request.method == 'POST':
		return redirect('/')
