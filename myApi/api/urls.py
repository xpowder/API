from django.urls import path
from .views import *

urlpatterns = [
    path("job/", JobView.as_view(), name='job-list-create'),
    path("job/<int:pk>/", JobView.as_view(), name='job-list-create'),

]
