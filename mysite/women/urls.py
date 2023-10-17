from django.urls import path, register_converter

from women.classurl import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter,  "yyyy")

urlpatterns = [
    path('', index, name='home'),
    path('cats/', categories, name='category'),
    path('cats/<int:catid>/', categories_id, name='cati'),
    path('cats/<slug:catid>/', categories_sl, name='catsl'),
    path('articles/<yyyy:year>/', year_archive, name='article'),
    path('students/<int:studentID>', listOfStudents, name='student'),
    path('badreq/', badRequest400),
    path('ise/', ise500),
]
