from django.shortcuts import render
from .models import User
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'form.html')


def data(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('document')
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'data.html', context)


def user(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    return render(request, 'data.html',{'fname': fname, 'lname':lname})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'result.html', context)
