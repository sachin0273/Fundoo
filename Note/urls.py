from django.urls import path

from . import views

urlpatterns = [
    path('create_label/', views.Label_Create.as_view(), name='create_label'),
    path('note_create/', views.Note_Create.as_view(), name='note_create'),
    path('note_crud/<note_id>', views.Note_Crud.as_view(), name='note_crud'),
    path('label/<label_id>', views.Label_Crud.as_view(), name='label'),
    path('Label/<user_id>', views.Get_Label.as_view(), name='get_label'),
    path('Note/<user_id>', views.Get_All_Note.as_view(), name='all_note'),
    # path('share_note/<note_id>/<str:provider>', views.Share_Note.as_view(), name='share'),
]
