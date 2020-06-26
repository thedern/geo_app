from django.urls import path
# from .views import home

# urlpatterns = [
#     path('', home, name='home')
# ]

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
