from django.db import models

# Create your models here.
from db_connection import db
Booking = db["Booking"]


#  {
#     vehicle : {
#         number : "sadsadasd",
#         driver_name:"sdfsdfsdfds"
#     },
#     name : "sasdasa",
#     date : "07/12/2024",
#     plant : "sfdsffsd",
#     booking_id:"asda"
#  }