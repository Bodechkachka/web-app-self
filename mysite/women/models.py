from django.db import models

# для хранения ORM- моделей для представления данных из базы данных
# Create your models here.


data_db = [
    {'id': 1, 'full_name': 'Буренок Дмитрий', 'is_smoke': False},
    {'id': 2, 'full_name': 'Горабанёв Кирилл', 'is_smoke': False},
    {'id': 3, 'full_name': 'Капшукова Дарья', 'is_smoke': False},
    {'id': 4, 'full_name': 'Кашаева Раяна', 'is_smoke': False},
    {'id': 5, 'full_name': 'Климин Тимур', 'is_smoke': False},
    {'id': 6, 'full_name': 'Косенков Глеб', 'is_smoke': False},
    {'id': 7, 'full_name': 'Костин Максим', 'is_smoke': False},
    {'id': 8, 'full_name': 'Кузенков Богдан', 'is_smoke': True},
    {'id': 9, 'full_name': 'Мишин Александр', 'is_smoke': False},
    {'id': 10, 'full_name': 'Мишин Алексей', 'is_smoke': False},
    {'id': 11, 'full_name': 'Миколадзе Антон', 'is_smoke': True},
    {'id': 12, 'full_name': 'Пешеходько Арсений', 'is_smoke': True},
    {'id': 13, 'full_name': 'Сентюрина Екатерина', 'is_smoke': False},
]


class Students(models.Model):
    full_name = models.CharField(max_length=50)
    interests = models.TextField(blank=True, default="idk")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_smoke = models.BooleanField(default=False)
    is_profcom = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class FavoriteBooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.CharField(max_length=10)
    is_digit_version = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title