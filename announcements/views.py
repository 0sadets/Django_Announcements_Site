from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from announcements.models import Category, CustomUser
from announcements.models import Announcement
from announcements.forms import AnnouncementForm, CategoryForm, CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.db.models import Q


def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})

def list(request, id):
    category = get_object_or_404(Category, id=id)
    announcements = Announcement.objects.filter(category_id=id)
    return render(request, "list.html", {"announcements": announcements, 'category': category})

def delete(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    category_id = announcement.category.id
    request.session['previous_url'] = request.META.get('HTTP_REFERER', '/')
    announcement.delete()
    return redirect(reverse('list', args=[category_id]))

@login_required   
def delete_cat(request, id):
    category = get_object_or_404(Category, id=id)
    
    category.delete()
    return redirect("/")
@login_required   
def create_cat(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, "create_category.html", {"form":form})
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/")
    
    
@login_required    
def create_ann(request):
    user = request.user
    if request.method == "GET":
        form = AnnouncementForm()
        return render(request, "create_ann.html", {"form": form})

    form = AnnouncementForm(request.POST) 
    if form.is_valid():
        announcement = form.save(commit=False)
        announcement.author = user
        announcement.save()
        print(f"Автор: {request.user}, Форма валідна: {form.is_valid()}")

        return redirect("/")  
    else:
        print("Помилки форми:", form.errors)

    return render(request, "create_ann.html", {"form": form})

    
def details(request, id):
    ann = get_object_or_404(Announcement, id=id)
    return render(request, "details.html", {"item":ann})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLogoutView(LogoutView):
    next_page = '/' 

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Ви успішно вийшли із системи.")
        return super().dispatch(request, *args, **kwargs)
    
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 
            else:
                messages.error(request, 'Невірні дані для входу')
        else:
            messages.error(request, 'Будь ласка, перевірте введені дані')

    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

from django.db.models import Count

@login_required
def user_profile(request):
    user = request.user
    categories = (
        Announcement.objects.filter(author=user)
        .values('category__title', 'category__icon')
        .annotate(total_announcements=Count('id'))
    )
    favorite_announcements = user.favorite_announcements.all()

    return render(request, 'user_profile.html', {
        'user': user,
        'categories': categories,
        'favorite_announcements': favorite_announcements,
    })

@login_required
def user_announcements(request):
    user = request.user
    user_announcements = Announcement.objects.filter(author=user).select_related('category')

    return render(request, 'user_announcements.html', {
        'user': user,
        'user_announcements': user_announcements,
    })
@login_required
def user_announcements_by_category(request, category_title):
    user = request.user
    category = get_object_or_404(Category, title=category_title)
    user_announcements = Announcement.objects.filter(author=user, category=category)

    return render(request, 'user_announcements.html', {
        'user_announcements': user_announcements,
        'category': category,
    })

def user_public_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user_announcements = Announcement.objects.filter(author=user)

    return render(request, 'user_public_profile.html', {
        'profile_user': user, 
        'user_announcements': user_announcements,
    })


@login_required
def edit_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)

    if request.user != announcement.author:
        return redirect('home')  

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('details', announcement.id) 
    else:
        form = AnnouncementForm(instance=announcement)

    return render(request, 'edit_announcement.html', {'form': form, 'announcement': announcement})



def search_result(request):
    query = request.GET.get('q', '').strip() 
    if query:
        words = query.split() 
        filters = Q()
        for word in words:
            filters &= Q(title__icontains=word)  
        results = Announcement.objects.filter(filters)
    else:
        results = []

    return render(request, 'search_result.html', {'results': results, 'query': query})
