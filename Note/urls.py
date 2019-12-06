from django.urls import path

from . import views

urlpatterns = [
    path('label/', views.LabelView.as_view(), name='labels'),
    path('note/', views.NoteView.as_view(), name='notes'),
    path('note/<note_id>', views.NoteDetailsView.as_view(), name='note'),
    path('label/<label_id>', views.LabelDetailsView.as_view(), name='label'),
    path('note/reminder/', views.Reminders.as_view(), name='reminder'),
    path('note/trash/', views.TrashNotes.as_view(), name='trash'),
    path('note/archive/', views.ArchiveNotes.as_view(), name='archive'),
    path('note/pinned/', views.PinnedNotes.as_view(), name='pin'),
    path('note/pagination/', views.pagination, name='pagination'),
    path('note/search/<search_note>', views.SearchNotes.as_view(), name='search')
]
