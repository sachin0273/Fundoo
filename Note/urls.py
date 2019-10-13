from django.urls import path

from . import views

urlpatterns = [
    path('Note/', views.Note_View.as_view(), name='Note'),
    path('share_note/<note_id>/<str:provider>', views.Share_Note.as_view(), name='share'), ]
