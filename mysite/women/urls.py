from django.urls import path, register_converter

from django.conf import settings
from django.conf.urls.static import static

from women.classurl import FourDigitYearConverter
from women.views import *

register_converter(FourDigitYearConverter,  "yyyy")

urlpatterns = [
    path('', index, name='home'),
    path('cats/', categories, name='category'),
    path('cats/<int:catid>/', categories_id, name='cati'),
    path('cats/1/', categories_id, name='cati/1'),
    path('cats/<slug:catid>/', categories_sl, name='catsl'),
    path('articles/<yyyy:year>/', year_archive, name='article'),
    path('students/<int:studentID>', listOfStudents, name='student'),
    path('students/1', listOfStudents, name='student/1'),
    path('datatypes/', dataTypes, name='dt'),
    path('badreq/', badRequest400),
    path('ise/', ise500),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
