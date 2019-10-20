import json
from Lib import redis
import pickle
import logging
from rest_framework.validators import UniqueValidator
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
from users.decoraters import login_required
from django.contrib.auth.models import User
from .service.note import Label_And_Note_Validator

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

        try:
            print(request.data)
            collaborator = request.data['collaborator']
            print(collaborator)
            pin = request.data['is_pin']
            trash = request.data['is_trash']
            archive = request.data['is_archive']
            label = request.data['label']
            print([label])
            note = request.data['note']
            title = request.data['title']
            image = request.data['image']
            user = request.data['user']
            validate_label = Label_And_Note_Validator().validate_label([label])
            if not validate_label['success']:
                return HttpResponse(json.dumps(validate_label), status=400)
            validate_collaborator = Label_And_Note_Validator().validate_collaborator([collaborator])
            if not validate_collaborator['success']:
                return HttpResponse(json.dumps(validate_collaborator), status=400)
            note_create = Note.objects.create(user_id=user, title=title, note=note, is_pin=pin,
                                              image=image, is_trash=trash, is_archive=archive)
            if validate_label['success'] == True:
                for labels in validate_label['data']:
                    note_create.label.add(labels)

            if validate_collaborator['success'] == True:
                for collaborators in validate_collaborator['data']:
                    note_create.collaborator.add(collaborators)

            redis.Del(user)
            smd = Smd_Response(True, 'successfully note created', status_code=200)
        except Exception:
            smd = Smd_Response()
            logger.warning('something was wrong warning from Note.views.note_api')
        return smd


# class Share_Note(GenericAPIView):
#
#     def get(self, request, note_id, provider, *args, **kwargs):
#         """
#         :param request:user request for share a note
#         :param note_id:here we get note id for share a note
#         :param provider:here we get provider for share a note
#         :return:this function is used for share a specific note
#         """
#         try:
#             note = Note.objects.get(pk=int(note_id))
#             if provider == 'twitter':
#                 url = 'https://twitter.com/intent/tweet?text=' + note.note
#                 return redirect(url)
#             elif provider == 'reddit':
#                 url = 'https://www.reddit.com/submit?title=' + note.note
#                 return redirect(url)
#             else:
#                 smd = Smd_Response(False, 'please provide twitter or reddit provider for share a note', [])
#         except Note.DoesNotExist:
#             smd = Smd_Response(False, 'please provide valid note_id', [])
#         except ValueError:
#             smd = Smd_Response(False, 'please provide note_id in number', [])
#         except Exception:
#             smd = Smd_Response()
#         return smd


class Note_Crud(GenericAPIView):
    serializer_class = NoteSerializers

    # permission_classes = (IsAuthenticated,)

    # parser_classes = (MultiPartParser, FormParser,)

    def put(self, request, note_id, *args, **kwargs):

        try:
            request_data = json.loads(request.body)
            print(request_data)
            if "collaborator" in request_data:
                collaborators = request_data['collaborator']
                result = Label_And_Note_Validator().validate_collaborator_for_put([collaborators])
                if not result['success']:
                    return HttpResponse(json.dumps(result))
                request_data['collaborator'] = result
            if "label" in request_data:
                labels = request_data['label']
                label_result = Label_And_Note_Validator().validate_label_for_put([labels])
                if not label_result['success']:
                    return HttpResponse(json.dumps(label_result))
                request_data['label'] = label_result
            update_note = Note.objects.get(pk=int(note_id))
            serializer = NoteSerializers(instance=update_note, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                user = request.user
                redis.Del(user.id)
                smd = Smd_Response(True, 'successfully note updated', status_code=200)
            else:
                smd = Smd_Response(False, serializer.errors)
        except Exception:
            smd = Smd_Response()
            logger.warning('something was wrong warning from Note.views.note_api')
        return smd

    def delete(self, request, note_id, *args, **kwargs):
        try:
            Note.objects.get(pk=int(note_id)).delete()
            user = request.user
            redis.Del(user.id)
            smd = Smd_Response(False, 'note deleted successfully', status_code=200)
        except Note.DoesNotExist:
            smd = Smd_Response(False, 'please enter valid note_id')
        except ValueError:
            smd = Smd_Response(False, 'please enter note_id in digits')
        except Exception:
            smd = Smd_Response()
        return smd


class Get_All_Note(GenericAPIView):

    def get(self, request, user_id, *args, **kwargs):
        try:
            note_data = redis.Get(user_id)
            if note_data:
                notes = pickle.loads(note_data)
                serializer = NoteSerializers(notes, many=True)
                smd = Smd_Response(True, 'successfully', data=serializer.data, status_code=200)
                return smd
            all_notes = Note.objects.filter(user_id=int(user_id))
            if all_notes:
                serializer = NoteSerializers(all_notes, many=True)
                note = pickle.dumps(all_notes)
                redis.Set(user_id, note)
                smd = Smd_Response(True, 'successfully', data=serializer.data, status_code=200)
            else:
                smd = Smd_Response(False, 'please enter valid user id')
        except Note.DoesNotExist:
            smd = Smd_Response(False, 'please enter valid user for get a note')
        except ValueError:
            smd = Smd_Response(False, 'please enter user_id in digits')
        except Exception:
            smd = Smd_Response()
        return smd


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
                user = serializer.data['user']
                redis.Del(str(user) + 'label')
                smd = Smd_Response(True, 'label successfully created', status_code=200)
                logger.warning('label created')
            else:
                smd = Smd_Response(False, serializer.errors)
                logger.warning('not valid input warning from Note.views.Label_api')
        except Exception:
            smd = Smd_Response()
            logger.warning('something was wrong warning from Note.views.Label_api')
        return smd


class Label_Crud(GenericAPIView):
    serializer_class = LabelSerializers

    # authentication_classes = (IsAuthenticated,)

    def put(self, request, label_id, *args, **kwargs):
        try:
            user = request.data['user']
            label = Label.objects.get(pk=int(label_id), user_id=user)
            if label:
                label.name = request.data['name']
                label.save()
                redis.Del(str(user) + 'label')
                smd = Smd_Response(True, 'label updated successfully', status_code=200)
            else:
                smd = Smd_Response(False, 'please enter valid label id or user id ')
        except Label.DoesNotExist:
            smd = Smd_Response(False, 'please enter valid label id or user id ')
        except ValueError:
            smd = Smd_Response(False, 'please enter label id in digits')
        except Exception:
            smd = Smd_Response()
        return smd

    def delete(self, request, label_id, *args, **kwargs):
        try:
            Label.objects.get(pk=int(label_id)).delete()
            user = request.user
            redis.Del(str(user.id) + 'label')
            smd = Smd_Response(False, 'label deleted successfully', status_code=200)
        except Label.DoesNotExist:
            smd = Smd_Response(False, 'please enter valid label_id ')
        except Exception:
            smd = Smd_Response()
        return smd


class Get_Label(GenericAPIView):

    def get(self, request, user_id, *args, **kwargs):
        try:
            data = redis.Get(str(user_id) + 'label')
            if data:
                hh = pickle.loads(data)
                serializer = LabelSerializers(hh, many=True)
                smd = Smd_Response(True, 'successfully', data=serializer.data, status_code=200)
                return smd
            label = Label.objects.filter(user_id=int(user_id))
            if label:
                serializer = LabelSerializers(label, many=True)
                fg = pickle.dumps(label)
                redis.Set(str(user_id) + 'label', fg)
                smd = Smd_Response(True, 'successfully', data=serializer.data, status_code=200)
            else:
                smd = Smd_Response(False, 'not valid user id please enter valid user_id')
        except Label.DoesNotExist:
            smd = Smd_Response(False, 'for this user id label not available please enter valid user_id')
        except ValueError:
            smd = Smd_Response(False, 'please enter user id in digits')
        except Exception:
            smd = Smd_Response()
        return smd
