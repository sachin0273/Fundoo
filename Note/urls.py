from django.urls import path

from . import views

urlpatterns = [
    path('label/', views.CreateAndGetLabel.as_view(), name='labels'),
    path('note/', views.CreateAndGetNote.as_view(), name='notes'),
    path('note/<note_id>', views.UpdateAndDeleteNote.as_view(), name='note'),
    path('label/<label_id>', views.UpdateAndDeleteLabel.as_view(), name='label'),
    path('note/reminder/', views.Reminders.as_view(), name='reminder'),
    path('note/trash/', views.Trash_Notes.as_view(), name='trash'),
    path('note/archive/', views.Archive_Notes.as_view(), name='archive'),
    path('note/pinned/', views.Pinned_Notes.as_view(), name='pin'),
    path('note/pagination/', views.pagination, name='pagination'),
    path('note/search/<search_note>', views.SearchNotes.as_view(), name='search')
]
