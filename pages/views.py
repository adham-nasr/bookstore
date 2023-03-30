from django.shortcuts import render
from .load import start
from .models import Book
from .helpers import dataToTemplate
# Create your views here.




def home(request):

    q = list(Book.objects.all())

    data = dataToTemplate(q)
    print(data)

    return render(request,'index.html',{'data':data})

def load_data(request):
    start()
    return render(request,'index.html')



