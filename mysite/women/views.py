from django.core.exceptions import BadRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError, Http404

# Create your views here.
data_db = [
    {'id': 1, 'FIO': 'Буренок Дмитрий', 'interests': 'Рисование, футбол', 'is_smoke': False},
    {'id': 2, 'FIO': 'Горабанёв Кирилл Артёмович', 'interests': 'Бокс, вязание', 'is_smoke': False},
    {'id': 3, 'FIO': 'Капшукова Дарья Руслановна', 'interests': 'Рисование, футбол', 'is_smoke': False},
    {'id': 4, 'FIO': 'Кашаева Раяна', 'interests': 'Бокс, вязание', 'is_smoke': False},
    {'id': 3, 'FIO': 'Миколадзе Антон Алексеевич', 'interests': 'история, литература', 'is_smoke': True},
]

def index(request):
    if (request.GET):
        gett = request.GET
        specifying = ""
        for key in gett:
            specifying += key + ": " + request.GET[key]+ " "
        return HttpResponse(f"<h3> Get request</h3> <p>{specifying}</p>")
    title: str = "Главная страница women"
    intNumber: int = 1234
    floatNumber: float = 1234.5678
    complexNumber: complex = 2+5j
    setickSet: set = {"uno", "dos", "tres"}
    listikList: list = ['one', 2, 'three', 0.4]
    tuplikTuple: tuple = ('единица', 2, ['tri', 'four'])
    dictikDict: dict = {'key1': 'Pervoye znachenye', 'key2': 'Vtoroye znachenye'}
    boolchickBool: bool = True
    data = {'title': title,
            'intNumber': intNumber, 'floatNumber': floatNumber, 'complexNumber': complexNumber,
            'setickSet': setickSet,
            'listikList': listikList,
            'tuplikTuple': tuplikTuple,
            'dictikDict': dictikDict,
            'boolchickBool': boolchickBool,
            'students': data_db}
    return render(request, 'women/index.html', context=data)

def categories(request):
    return HttpResponse("<h2>Статьи по категориям</h2>")

def categories_id(request, catid):
    return HttpResponse(f"<h2>Статьи по категориям {catid} </h2>")

def categories_sl(request, catid):
    return HttpResponse(f'<h2>Статьи по названиям и категориям {catid}</h2>')

def year_archive(request, year):
    if int(year) > 2023 or int(year) < 2000:
        redirect('home')
        #raise Http404()
    else:
        return HttpResponse(f'<h2>В {year} году случилось </h2>')

def listOfStudents(request, studentID):
    theListOfStudents = {1:"Буренок Дмитрий", 2:"Горбанёв Кирил", 3:"Капшукова Дарья", 4:"Кашаева Раяна",
                         5:"Климин Тимур", 6:"Косенков Глеб", 7:"Костин Максим", 8:"Кузенков Богдан",
                         9:"Мишин Александр", 10:"Мишин Алексей", 11:"Миколадзе Антон", 12:"Пешеходько Арсений",
                         13:"Сентюрина Екатерина"}
    if 1 <= studentID <= 13:
        return HttpResponse(f'Студент {theListOfStudents.get(studentID)}')
    elif 13 < studentID:
        return redirect('student', 1)
    elif studentID == 0:
        return redirect('home', permanent=True)

def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неудачный запрос</h1>') #400

def forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>') #403

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Статья не найдена</h1>') #404

def internalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>') #500

def badRequest400(request):
    raise BadRequest

def ise500(request):
    raise asd
