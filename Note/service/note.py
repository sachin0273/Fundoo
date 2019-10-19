import json

from rest_framework_simplejwt.state import User

from Note.models import Label
from django.http import HttpResponse

from utils import Smd_Response


class Label_And_Note_Validator:

    def validate_label(self, labels):
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
        except Exception as e:
            smd = {'success': False, 'message': 'something is wrong when validating your label'}
        return smd

    def validate_collaborator(self, collaborators):
        try:
            if len(collaborators) != 0:
                collaborator_list = []
                for collaborator in collaborators:
                    new_collaborator = User.objects.get(email=collaborator)
                    collaborator_list.append(new_collaborator)
                return {'success': True, 'data': collaborator_list}
            else:
                return {'success': 'no_collaborator'}
        except Label.DoesNotExist:
            smd = {'success': False, 'message': 'your collaborator is not valid please try valid collaborator'}
        except Exception:
            smd = {'success': False, 'message': 'something is wrong when validating your collaborator'}
        return smd

    def putvalid(self, data):
        klist = []
        for i in data:
            user_obj = User.objects.get(email=i)
            klist.append(user_obj.id)
            print(user_obj.username)
        return klist

    def labelvalid(self, data):
        llist = []
        for i in data:
            label_obj = Label.objects.get(name=i)
            llist.append(label_obj.id)
        return llist
