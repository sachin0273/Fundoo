import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note, Label
from Note.serializers import NoteSerializers, LabelSerializers
from utils import Smd_Response
from User.decoraters import login_required
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Note_Create(GenericAPIView):
    serializer_class = NoteSerializers

    # permission_classes = (IsAuthenticated,)

    # parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """

        :param request:user request for create a note
        :return:this function is used for create new note and save

        """
        # try:
        # print((request.body))
        collaborator = request.data['collaborator']
        pin = request.data['is_pin']
        # trash = request.data['is_trash']
        # archive = request.data['is_archive']
        label = request.data['label']
        note = request.data['note']
        title = request.data['title']
        image = request.data['image']
        user = request.data['user']
        print(label)
        print(collaborator)
        if label is not None:
            fgh = Label.objects.get(name=label)
            if fgh:
                pkjkj = fgh
            else:
                return Response('not valid note')
        if collaborator is not None:
            hjkkk = User.objects.get(email=collaborator)
            if hjkkk:
                jkjk = hjkkk
            else:
                return Response('not valid user')
        gg = Note.objects.create(user_id=user, title=title, note=note, is_pin=pin,
                                 image=image)
        gg.collaborator.add(jkjk)
        gg.label.add(pkjkj)
        # serializer = NoteSerializers(data=request.data)
        # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        user = request.user
        # f=serializer.data['label']
        # if serializer.is_valid():
        #     print('ffkfkfkfkf')
        # serializer.validated_data['label'] = '1'
        # print('fjifjfjfjfjf')
        # serializer.save()
        # serializer.save()
        # smd = Smd_Response(True, 'successfully note created' + serializer.data, status_code=200)
        # return Response(serializer.errors)
        # logg
        # er.warning('note created')
        # else:
        #     smd = Smd_Response(False, serializer.errors)
        #     logger.warning('not valid input warning from Note.views.note_api')

    # except Exception:
    #     smd = Smd_Response()
    #     logger.warning('something was wrong warning from Note.views.note_api')
    # return smd


class Share_Note(GenericAPIView):

    def get(self, request, note_id, provider, *args, **kwargs):
        """
        :param request:user request for share a note
        :param note_id:here we get note id for share a note
        :param provider:here we get provider for share a note
        :return:this function is used for share a specific note
        """
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


class Note_Crud(GenericAPIView):
    serializer_class = NoteSerializers

    # permission_classes = (IsAuthenticated,)
    # parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, note_id, *args, **kwargs):
        data = Note.objects.get(pk=note_id)
        print(data)
        if data:

            serializer = NoteSerializers(data)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response('not valid id ')

    def put(self, request, *args, **kwargs):

        collaborator = request.data['collaborator']
        pin = request.data['is_pin']
        # trash = request.data['is_trash']
        # archive = request.data['is_archive']
        label = request.data['label']
        note = request.data['note']
        title = request.data['title']
        image = request.data['image']
        user = request.data['user']
        pass

    def delete(self, request, note_id, *args, **kwargs):
        try:
            Note.objects.get(pk=note_id).delete()
            return Response('deleted successfully')
        except Note.DoesNotExist:
            return Response('not exist')
        except Exception:
            return Response('something is wrong')


class Label_Create(GenericAPIView):
    serializer_class = LabelSerializers

    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        """

        :param request:user request for create a note
        :return:this function is used for create new note and save

        """
        try:
            serializer = LabelSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                smd = Smd_Response(True, serializer.data, status_code=200)
                logger.warning('note created')
            else:
                smd = Smd_Response(False, serializer.errors)
                logger.warning('not valid input warning from Note.views.Label_api')
        except Exception:
            smd = Smd_Response()
            logger.warning('something was wrong warning from Note.views.Label_api')
        return smd


class Label_Crud(GenericAPIView):
    serializer_class = LabelSerializers

    def get(self, request, label_id, *args, **kwargs):
        try:
            label = Label.objects.get(pk=label_id)
            if label:
                return Response({'label_id': label.pk, 'label': label.name})
            else:
                return Response('not valid note')
        except Label.DoesNotExist:
            return Response('not valid id')
        except Exception:
            return Response('something is wrong')

    # except Exception:
    #     return Response('something is wrong')

    def put(self, request, label_id, *args, **kwargs):
        try:
            user = request.data['user']
            label = Label.objects.get(pk=label_id, user_id=user)
            if label:
                label.name = request.data['name']
                label.save()
                return Response('successfully note updated')
            else:
                return Response('not valid note_id or user')
        except Label.DoesNotExist:
            return Response('please enter valid id')
        except Exception:
            return Response('something is wrong')

    def delete(self, request, label_id, *args, **kwargs):
        try:
            Label.objects.get(pk=label_id).delete()
            return Response('object deleted successfully')
        except Label.DoesNotExist:
            return Response('label not exist')
        except Exception:
            return Response('somthing is wrong')
