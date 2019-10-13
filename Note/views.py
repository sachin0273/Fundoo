import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note
from Note.serializers import NoteSerializers
from utils import Smd_Response
from login.decoraters import login_required


class Note_View(GenericAPIView):
    serializer_class = NoteSerializers

    permission_classes = (IsAuthenticated,)
    # parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            serializer = NoteSerializers(data=request.data)
            user = request.user
            print(user)
            if serializer.is_valid():
                serializer.validated_data['user'] = user
                serializer.save()
                smd = Smd_Response(True, 'successfully note created', status_code=200)
            else:
                smd = Smd_Response(False, serializer.errors)
        except Exception:
            smd = Smd_Response()
        return smd


class Share_Note(GenericAPIView):

    def get(self, request, note_id, provider, *args, **kwargs):
        try:
            note = Note.objects.get(pk=int(note_id))
            if provider == 'twitter':
                url = 'https://twitter.com/intent/tweet?text=' + note.note
                return redirect(url)
            elif provider == 'reddit':
                url = 'https://www.reddit.com/submit?title=' + note.note
                return redirect(url)
            else:
                smd = Smd_Response(False, 'please provide twitter or reddit provider for share a note', [])
        except Note.DoesNotExist:
            smd = Smd_Response(False, 'please provide valid note_id', [])
        except ValueError:
            smd = Smd_Response(False, 'please provide note_id in number', [])
        except Exception:
            smd = Smd_Response()
        return smd
