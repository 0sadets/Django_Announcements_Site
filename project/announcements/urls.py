from django.urls import path
from announcements import views


urlpatterns = [
    path("", views.index, name='index'),
    path("list/<int:id>", views.list, name='list'),
    path("delete/<int:id>", views.delete, name='delete'),
    path("delete_cat/<int:id>", views.delete_cat, name='delete_cat'),
    path("create_category/", views.create_cat, name="create_category"),
    path("create_ann/", views.create_ann, name="create_ann"),
    path("details/<int:id>", views.details, name='details'),
    path("register/", views.register, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/announcements/', views.user_announcements, name='user_announcements'),
    path('profile/category/<str:category_title>/', views.user_announcements_by_category, name='user_announcements_by_category'),
    path('user/<int:user_id>/', views.user_public_profile, name='user_profile'),  
    path('edit/<int:announcement_id>/', views.edit_announcement, name='edit_announcement'),
    path('search/', views.search_result, name='search_result'),
]