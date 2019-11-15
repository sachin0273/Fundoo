import json
import pickle
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from Lib import redis
from Note.models import Label
from Note.models import Note
from django.http import HttpResponse

from Note.serializers import NoteSerializers, NotesSerializer
from utils import Smd_Response
import logging
from utils import smd_response

logger = logging.getLogger(__name__)


class Label_Note_Validator:

    def validate_label(self, labels):
        """

        :param labels:here we pass number of labels
        :return:this function is perform label validation

        """
        try:
            if len(labels) != 0:
                label_list = []
                for label in labels:
                    new_label = Label.objects.get(name=label)
                    label_list.append(new_label)
                return {'success': True, 'data': label_list}
            else:
                return {'success': 'no_labels'}
        except Label.DoesNotExist:
            smd = {'success': False, 'message': 'your label is not valid please add label and try'}
        except Exception:
            smd = {'success': False, 'message': 'something is wrong when validating your label'}
        return smd

    def validate_collaborator(self, collaborators):
        """

        :param collaborators:here we pass number of collaborators
        :return:this function is perform collaborators validation

        """
        try:
            if len(collaborators) != 0:
                collaborator_list = []
                for collaborator in collaborators:
                    new_collaborator = User.objects.get(email=collaborator)
                    collaborator_list.append(new_collaborator)
                return {'success': True, 'data': collaborator_list}
            else:
                return {'success': 'no_collaborator'}
        except User.DoesNotExist:
            smd = {'success': False, 'message': 'your collaborator is not valid please try valid collaborator'}
        except Exception:
            smd = {'success': False, 'message': 'something is wrong when validating your collaborator'}
        return smd

    def validate_collaborator_for_put(self, data):
        """

        :param :here we pass number of labels
        :return:this function is perform label validation

        """
        try:

            collaborator_list = []
            for collaborator in data:
                user_obj = User.objects.get(email=collaborator)
                collaborator_list.append(user_obj.id)
                print(user_obj.username)
            return {'success': True, 'data': collaborator_list}
        except User.DoesNotExist:
            smd = {'success': False, 'message': 'your collaborator is not valid please try valid collaborator',
                   'data': []}
        except Exception:
            smd = {'success': False, 'message': 'something is wrong when validating your collaborator',
                   'data': []}
        return smd

    def validate_label_for_put(self, data):
        """

        :param data:here we pass number of collaborators
        :return:this function is perform collaborators validation

        """
        try:
            label_list = []
            for label in data:
                label_obj = Label.objects.get(name=label)
                label_list.append(label_obj.id)
            return {'success': True, 'data': label_list}
        except Label.DoesNotExist:
            smd = {'success': False, 'message': 'your label is not valid please try valid labels', 'data': []}
        except Exception:
            smd = {'success': False, 'message': 'something is wrong when validating your labels',
                   'data': []}
        return smd


class Listing_Pages:
    def reminder_notes(self, user):
        """

        :param user:this is logged in user
        :return:this function is used for return the reminder notes both fired and upcoming

        """
        try:
            fired_reminder = redis.Get(str(user.username) + 'fired_reminders')
            upcoming_reminder = redis.Get(user.username + 'upcoming_reminders')
            print(user)
            if fired_reminder or upcoming_reminder:
                notes = pickle.loads(fired_reminder)
                notes_upcoming = pickle.loads(upcoming_reminder)

                fired_reminder_serializer = NoteSerializers(notes, many=True)
                upcoming_reminder_serializer = NoteSerializers(notes_upcoming, many=True)

                smd = smd_response(True, 'successfully', data={'fired': fired_reminder_serializer.data,
                                                               'upcoming': upcoming_reminder_serializer.data})
                logger.info('successfully get notes from redis')
                return smd
            fired_reminder_object = Note.objects.filter(user_id=int(user.id), reminder__lte=timezone.now())
            upcoming_reminder_object = Note.objects.filter(user_id=user.id, reminder__gte=timezone.now())
            if fired_reminder_object or upcoming_reminder_object:
                fired_serializer = NoteSerializers(upcoming_reminder_object, many=True)
                upcoming_serializer = NoteSerializers(fired_reminder_object, many=True)

                fired_reminder_notes = pickle.dumps(fired_reminder_object)
                upcoming_reminder_notes = pickle.dumps(upcoming_reminder_object)

                redis.Set(str(user.username) + 'fired_reminders', fired_reminder_notes)
                redis.Set(user.username + 'upcoming_reminders', upcoming_reminder_notes)

                smd = smd_response(True, 'successfully',
                                   data={'fired': fired_serializer.data, 'upcoming': upcoming_serializer.data})
                logger.info('successfully get notes from database')
            else:
                smd = smd_response(False, 'for this user reminder not exists')
        except Note.DoesNotExist:
            smd = smd_response(False, 'please enter valid user for get a note')
            logger.error('note not exist for this note id error from Note.views')
        except ValueError:
            smd = smd_response(False, 'please enter user_id in digits')
        except Exception:
            logger.error('exception occurred while getting all notes error from Note.views')
            smd = smd_response()
        return smd

    def trash_notes(self, user):
        """

        :param user:this is our logged in user
        :return:this function is used for return the all trash notes

        """
        try:
            trash_note_data = redis.Get(user.username + 'trash')

            if trash_note_data:
                notes = pickle.loads(trash_note_data)
                serializer = NoteSerializers(notes, many=True)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from redis')
                return smd
            trash_notes = Note.objects.filter(user_id=int(user.id), is_trash=True)
            if trash_notes:
                serializer = NoteSerializers(trash_notes, many=True)
                note = pickle.dumps(trash_notes)
                redis.Set(user.username + 'trash', note)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from database')
            else:
                smd = smd_response(False, 'please enter valid user id')
        except Note.DoesNotExist:
            smd = smd_response(False, 'please enter valid user for get a note')
            logger.error('note not exist for this note id error from Note.views')
        except ValueError:
            smd = smd_response(False, 'please enter user_id in digits')
        except Exception:
            logger.error('exception occurred while getting all notes error from Note.views')
            smd = smd_response()
        return smd

    def archive_notes(self, user):
        """

        :param user:this is our logged in user
        :return:this function is used for return all archive notes

        """
        try:
            archive_note_data = redis.Get(str(user.username) + 'archive')

            if archive_note_data:
                notes = pickle.loads(archive_note_data)
                serializer = NoteSerializers(notes, many=True)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from redis')
                return smd
            archive_notes = Note.objects.filter(user_id=user.id, is_archive=True)
            if archive_notes:
                serializer = NoteSerializers(archive_notes, many=True)
                note = pickle.dumps(archive_notes)
                redis.Set(user.username + 'archive', note)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from database')
            else:
                smd = smd_response(False, 'please enter valid user id')
        except Note.DoesNotExist:
            smd = smd_response(False, 'please enter valid user for get a note')
            logger.error('note not exist for this note id error from Note.views')
        except ValueError:
            smd = smd_response(False, 'please enter user_id in digits')
        except Exception:
            logger.error('exception occurred while getting all notes error from Note.views')
            smd = smd_response()
        return smd

    def pin_notes(self, user):
        try:
            pinned_note_data = redis.Get(str(user.username) + 'pin')

            if pinned_note_data:
                notes = pickle.loads(pinned_note_data)
                serializer = NotesSerializer(notes, many=True)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from redis')
                return smd
            pinned_notes = Note.objects.filter(user_id=user.id, is_pin=True)
            if pinned_notes:
                serializer = NotesSerializer(pinned_notes, many=True)
                note = pickle.dumps(pinned_notes)
                redis.Set(user.username + 'pin', note)
                smd = smd_response(True, 'successfully', data=serializer.data)
                logger.info('successfully get notes from database')
            else:
                smd = smd_response(False, 'please enter valid user id')
        except Note.DoesNotExist:
            smd = smd_response(False, 'please enter valid user for get a note')
            logger.error('note not exist for this note id error from Note.views')
        except ValueError:
            smd = smd_response(False, 'please enter user_id in digits')
        except Exception:
            logger.error('exception occurred while getting all notes error from Note.views')
            smd = smd_response()
        return smd


def update_redis(user):
    """

    :param user:this is our logged in user
    :return:this function is used update notes in redis

    """
    try:
        all_notes = Note.objects.filter(user_id=int(user.id), is_trash=False, is_archive=False)
        notes = pickle.dumps(all_notes)
        redis.Set(user.username, notes)
    except Exception:
        return False


def label_update_in_redis(user):
    """

    :param user:this our logged in user
    :return:this function is used for update_redis labels in redis

    """
    try:

        labels = Label.objects.get(user_id=user.id)
        all_label = pickle.dumps(labels)
        redis.Set(user.username + 'label', all_label)

    except Exception:
        return False
