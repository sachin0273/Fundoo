from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('label/', views.CreateAndGetLabel.as_view(), name='get_or_create_label'),
    path('note/', views.CreateAndGetNote.as_view(), name='get_or_create_note'),
    path('update_or_delete_note/<note_id>', views.UpdateAndDeleteNote.as_view(), name='update_or_delete_note'),
    path('update_or_delete_label/<label_id>', views.UpdateAndDeleteLabel.as_view(), name='update_or_delete_label'),
    # path('get_label/<user_id>', views.Get_Label.as_view(), name='get_label'),
    # path('get_note/<user_id>', views.Get_All_Note.as_view(), name='all_note'),
    # path('share_note/<note_id>/<str:provider>', views.Share_Note.as_view(), name='share'),
    path('reminder/', views.Reminders.as_view(), name='reminder'),
    path('trash/', views.Trash_Notes.as_view(), name='trash'),
    path('archive/', views.Archive_Notes.as_view(), name='archive'),
=======
    path('label/', views.CreateAndGetLabel.as_view(), name='labels'),
    path('note/', views.CreateAndGetNote.as_view(), name='notes'),
    path('note/<note_id>', views.UpdateAndDeleteNote.as_view(), name='note'),
    path('label/<label_id>', views.UpdateAndDeleteLabel.as_view(), name='label'),
    path('note/reminder/', views.Reminders.as_view(), name='reminder'),
    path('note/trash/', views.Trash_Notes.as_view(), name='trash'),
    path('note/archive/', views.Archive_Notes.as_view(), name='archive'),
    path('note/pagination/', views.pagination, name='pagination'),
    path('note/search/<path>', views.Elastic.as_view(), name='search'),
    # path('note/ddd/',views.DocumentViewSet.as_view(),name='kk'),
>>>>>>> 2f1c5cd5... elastic search done

]
