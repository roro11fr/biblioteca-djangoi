from django.forms import DateTimeField
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm, BookForm, SearchF, SearchU
from .models import Book, Inchiriere
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone



@login_required
def library_page(request):
    formf = SearchF()
    books = Book.objects.all()

    if request.method == 'POST':
        formf = SearchF(request.POST)
        if formf.is_valid():
            search_q = formf.cleaned_data.get('q')
            if search_q:
                books = Book.objects.filter(name__icontains=search_q)
        return render(request, 'library.html', {'formf': formf, 'books': books})
    else:
        return render(request, 'library.html', {'formf': formf})
 


def welcome_page(request):
    return render(request, 'welcome.html')

def signin_page(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, "authentication/signin.html", {'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            # cere permisiune la admin sa se inregistreze
            user.is_active = False;
            user.save()
            messages.success(request, 'Inregistrarea ta a fost trimisa catre un admin.')
            login(request, user)
            return redirect('welcome')
        else:
             return render(request, "authentication/signin.html", {'form':form})


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('library')
            else:
                messages.success(request, 'Eroare de logare, încearcă din nou...')
                return redirect('login')
        else:
            messages.error(request, 'Username și/sau parolă lipsesc.')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})


@login_required
def logout_user(request):
    logout(request)
    next_param = request.GET.get('next', None)

    if next_param:
        return redirect(next_param)
    else:
        messages.success(request, "Ai fost delogat")
        return redirect('welcome')
    

def register_user(request):
    return render(request, ('authentication/register_user.html'), {})


def cautare_carte(request):
    formf = SearchF()
    books = Book.objects.all()

    if request.method == 'POST':
        formf = SearchF(request.POST)
        if formf.is_valid():
            search_q = formf.cleaned_data.get('q')
            if search_q:
                books = Book.objects.filter(name__icontains=search_q)
        return render(request, 'adminSee/cautare.html', {'formf': formf, 'books': books})


    else:
        return render(request, 'adminSee/cautare.html', {'formf': formf})
 



def cautare_user(request):
    form = SearchU()
    useri = User.objects.all()
    if request.method == 'POST':
        form = SearchU(request.POST)
        if form.is_valid():
            search_q = form.cleaned_data.get('u')
            if search_q:
                useri = User.objects.filter(username__icontains=search_q)
        return render(request, 'adminSee/useri.html', {'form': form, 'useri': useri})


    else:
        return render(request, 'adminSee/useri.html', {'form': form})
 

def show_user(request, user_id):
    user = User.objects.get(pk = user_id)
    return render(request, 'adminSee/show_user.html',{'user':user})

def delete_utilizator(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if(request.method == "POST"):
        user.delete()
        messages.success(request, 'Utilizatorul a fost sters cu succes')
        return redirect('useri')
    return render(request, 'adminSee/show_user.html', {'user': user})


def dezactivate_utilizator(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, 'Profile disabled cu succes')
    return redirect('useri')


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'adminSee/add_book.html', {'form': form})
    
    if request.method == 'POST':
        form = BookForm(request.POST) 
        if form.is_valid():
            author = form.data['author']
            name = form.data['name']

            if not Book.objects.filter(author=author, name=name).exists():
                book = form.save(commit=False)
                book.save()
                messages.success(request, 'Cartea a fost inregistrata')
            else : 
                messages.warning(request, 'Cartea există deja în bibliotecă')

            return redirect('adaugare')
        else: 
            return render(request, 'adminSee/add_book.html', {'form': form})




def show_carte(request, book_id):
    book = Book.objects.get(pk = book_id)
    return render(request, 'inchiriere_carte.html',{'book':book})


def  inchiriaza_carte(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if(request.method == "POST"):

        if not book.is_available:
            messages.warning(request, 'Această carte a fost deja închiriată.')
            return redirect('library')

        user = request.user
        book.is_available = False
        book.save()

        inchiriere = Inchiriere.objects.create(user=user, book=book)
        messages.success(request, 'Cartea a fost inchiriata cu succes')
        return redirect('library')
    return render(request, 'inchiriere_carte.html', {'book':book})


def raportare_carti(request):
    inchirieri = Inchiriere.objects.all()
    books = Book.objects.all()
    return render(request, "adminSee/raportare.html", {'inchirieri': inchirieri, 'books':books})
