from django.contrib import admin
from django.urls import path
from medicine_delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_medicine/', views.GetMedicineDetails.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]
