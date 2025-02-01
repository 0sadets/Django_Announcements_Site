
from django import forms
from announcements.models import Category, Announcement, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

icons = [
    ('fa-solid fa-house', 'House'),
    ('fa-solid fa-comment', 'Comment'),
    ('fa-solid fa-cart-shopping', 'Shopping Cart'),
    ('fa-solid fa-book', 'Book'),
    ('fa-solid fa-gear', 'Gear'),
    ('fa-solid fa-gift', 'Gift'),
    ('fa-solid fa-handshake', 'Handshake'),
    ('fa-solid fa-gamepad', 'Gamepad'),
    ('fa-solid fa-shop', 'Shop'),
    ('fa-solid fa-building', 'Building'),
    ('fa-solid fa-power-off', 'Power Off'),
    ('fa-solid fa-icons', 'Icons'),
    ('fa-solid fa-train', 'Train'),
    ('fa-solid fa-radio', 'Radio'),
    ('fa-solid fa-route', 'Route'),
    ('fa-solid fa-puzzle-piece', 'Puzzle Piece'),
    ('fa-solid fa-umbrella-beach', 'Beach Umbrella'),
    ('fa-solid fa-dumbbell', 'Dumbbell'),
    ('fa-solid fa-tractor', 'Tractor'),
    ('fa-solid fa-taxi', 'Taxi'),
    ('fa-solid fa-tablet-screen-button', 'Tablet Button'),
    ('fa-solid fa-plane-up', 'Plane Up'),
    ('fa-solid fa-person-rifle', 'Person with Rifle'),
    ('fa-solid fa-person-swimming', 'Swimming Person'),
    ('fa-solid fa-heart-pulse', 'Heart Pulse'),
    ('fa-solid fa-flask-vial', 'Flask Vial'),
    ('fa-solid fa-paw', 'Paw'),
    ('fa-solid fa-dog', 'Dog'),
    ('fa-solid fa-cat', 'Cat'),
    ('fa-solid fa-children', 'Children'),
    ('fa-solid fa-carrot', 'Carrot'),
    ('fa-solid fa-candy-cane', 'Candy Cane'),
    ('fa-solid fa-camera', 'Camera'),
    ('fa-solid fa-wrench', 'Wrench'),
    ('fa-solid fa-bell', 'Bell'),
    ('fa-solid fa-cog', 'Cog'),
    ('fa-solid fa-cloud', 'Cloud'),
    ('fa-solid fa-lightbulb', 'Lightbulb'),
    ('fa-solid fa-laptop', 'Laptop'),
    ('fa-solid fa-lock', 'Lock'),
    ('fa-solid fa-microphone', 'Microphone'),
    ('fa-solid fa-moon', 'Moon'),
    ('fa-solid fa-paper-plane', 'Paper Plane'),
    ('fa-solid fa-phone', 'Phone'),
    ('fa-solid fa-camera-retro', 'Retro Camera'),
    ('fa-solid fa-pencil', 'Pencil'),
    ('fa-solid fa-sun', 'Sun'),
    ('fa-solid fa-ambulance', 'Ambulance'),
    ('fa-solid fa-anchor', 'Anchor'),
    ('fa-solid fa-bicycle', 'Bicycle'),
    ('fa-solid fa-briefcase', 'Briefcase'),
    ('fa-solid fa-bus', 'Bus'),
    ('fa-solid fa-camera-movie', 'Camera Movie'),
    ('fa-solid fa-cloud-sun', 'Cloud Sun'),
    ('fa-solid fa-dice', 'Dice'),
    ('fa-solid fa-dragon', 'Dragon'),
    ('fa-solid fa-fire', 'Fire'),
    ('fa-solid fa-fingerprint', 'Fingerprint'),
    ('fa-solid fa-glass-cheers', 'Glass Cheers'),
    ('fa-solid fa-hat-cowboy', 'Cowboy Hat'),
    ('fa-solid fa-ice-cream', 'Ice Cream'),
    ('fa-solid fa-kiwi-bird', 'Kiwi Bird')
]



class CategoryForm(forms.ModelForm):
  
    title = forms.CharField(max_length=512, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    icon = forms.ChoiceField(choices=icons, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Category
        fields = ['title', 'icon']

    
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"
        exclude = ['created_at', 'is_active', 'author']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter title"}),
            "desc": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter description"}),  # Виправлено
            "image": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter image URL"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Location"}),
            "price": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter price"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я користувача"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть вашу електронну пошту'}),
    )
    phone_number = forms.CharField( 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть вашу номер телефону'}),
    )
    social_link = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть посилання на вашу соціальну мережу'}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Підтвердіть пароль'}),
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'social_link', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ім\'я користувача'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
    )



# class AnnouncementForm(forms.ModelForm):
#     class Meta:
#         model = Announcement
#         fields = ['title', 'desc', 'price', 'location', 'image', 'category']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'desc': forms.Textarea(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'location': forms.TextInput(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#         }




    