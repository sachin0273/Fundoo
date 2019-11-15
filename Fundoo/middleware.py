import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse

from utils import Smd_Response
from Note.models import Label


class LabelCollaborators:
    def __init__(self, function):
        self.function = function

    # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.method)
        print(request.user)
        print(request)
        print(request.get_full_path())
        try:
            if request.get_full_path() == "/api/note/" and request.method == 'POST' or request.path.startswith(
                    reverse('note', args=[str])) and request.method == 'PUT':

                request_data = json.loads(request.body)

                if 'label' in request_data or 'collaborator' in request_data:
                    if len(request_data['label']) != 0:
                        label_list = []
                        for label in request_data['label']:
                            new_label = Label.objects.get(name=label)
                            label_list.append(new_label)
                    if len(request_data['collaborator']) != 0:
                        collaborator_list = []
                        for collaborator in request_data['collaborator']:
                            new_collaborator = User.objects.get(email=collaborator)
                            collaborator_list.append(new_collaborator)
                        response = self.function(request)
                    else:
                        response = self.function(request)
                else:
                    response = self.function(request)
            else:
                return self.function(request)
        except Label.DoesNotExist:
            response = Smd_Response(message='your label is not @@@ valid please add label and try')

        except User.DoesNotExist:
            response = Smd_Response(message='for this email id user is not exist')
        except Exception:
            response = Smd_Response(message='something is@@ wrong when validating your label or collaborator')
        return response
