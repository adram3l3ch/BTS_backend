from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime, timedelta
from bson.json_util import dumps

# Create your views here.
from .models import Booking

@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        existing_booking = Booking.find_one({
            'vehicle.number':data["vehicle"]['number'],
            'date':data["date"]
            })
        if existing_booking:
            return JsonResponse({'error':True,'message':'Vehicle no exists for given date'},status = 403)
        else:
            Booking.insert_one(data)
            return JsonResponse({'error':False,'message':'Booking Successful'},status = 201)
    else:
        return JsonResponse({'error':True,'message':'invalid request'},status = 400)

@csrf_exempt
def get_bookings(request):
    if request.method == 'GET':
        cutoff_date = datetime.utcnow() - timedelta(days=7)
        Booking.delete_many({"date": cutoff_date.strftime('%d/%m/%Y')})
        date = request.GET.get('date') 
        bookings = Booking.find({"date":date})
        bookings_json = dumps(bookings)
        return JsonResponse({'error':False,'message':'Success',"data":json.loads(bookings_json)},status = 200)
    else:
        return JsonResponse({'error':True,'message':'invalid request'},status = 400)






