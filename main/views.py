from django.shortcuts import render
# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', 'Semser', 'space'],
        'obj': {
            'car': 'mers',
            'age': 18,
            'hobby': 'anime'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')