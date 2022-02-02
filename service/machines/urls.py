from django.urls import path
from service.machines.views import CompanyView, HomeView, MachineView, ContactUs, WishListView, CategoryView,SearchView, AddToWishListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('company/<id>/', CompanyView.as_view()),
    path('machine/<id>/', MachineView.as_view(), name="machine"),
    path('contact/', ContactUs.as_view()),
    path('category/<id>/', CategoryView.as_view()),
    path('wishlist/', WishListView.as_view()),
    path('addToWishList/<id>/', AddToWishListView.as_view()),
    path('search/', SearchView.as_view()),

]