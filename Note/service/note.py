import json

from django.contrib.auth.models import User

from Note.models import Label
from django.http import HttpResponse

from utils import Smd_Response


class Label_And_Note_Validator:

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
        except Exception :
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
