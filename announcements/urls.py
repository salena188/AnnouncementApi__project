from django.urls import path

from .views import (announcement_api,announcement_page)

urlpatterns = [

    path('',announcement_page,name='announcement-page'),

    path('api/announcements/',announcement_api,name='announcement-api'
    ),

]