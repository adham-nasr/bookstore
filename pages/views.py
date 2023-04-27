from django.shortcuts import render
from .load import start
from .models import Book
from .helpers import dataToTemplate
from django.contrib.auth.decorators import login_required
from django.views import View


# Create your views here.




def home(request):

    q = list(Book.objects.all())

    data = dataToTemplate(q)
    print(data)

    return render(request,'index.html',{'data':data})

def load_data(request):
    start()
    return render(request,'index.html')


class MybooksView(View):

    def get(self, request, *args, **kwargs):

        user = request.user
        q = list(user.books.all())
        print(q)
        books = dataToTemplate(q)
        print(books)

        return render(request,'mybooks.html',{'data':books})
