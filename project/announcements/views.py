from django.shortcuts import get_object_or_404, redirect, render
from announcements.models import Category
from announcements.models import Announcement

def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})

def list(request, id):
    announcements = Announcement.objects.filter(category_id=id)
    return render(request, "list.html", {"announcements": announcements})

def delete(request, id):
    announcements = get_object_or_404(Announcement, id=id)
    
    announcements.delete()
    return redirect("/")
