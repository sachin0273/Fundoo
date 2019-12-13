import json
import re
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from jwt import DecodeError
from utils import Smd_Response
from Note.models import Label

User = get_user_model()


class LabelCollaborators:
    def __init__(self, function):
        self.function = function

    # One-time configuration and initialization.

    def __call__(self, request, *view_args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called
        # print(request.method)
        # print(request.user)
        # print(request)
        # print(requ est.get_full_path())

        try:
            if request.get_full_path() == "/api/note/" and request.method == 'POST' or request.path.startswith(
                    reverse('note', args=[str])) and request.method == 'PUT':
                if request.headers['Content-Type'].split(';')[0] == 'multipart/form-data':
                    request_data = request.POST
                else:
                    request_data = json.loads(request.body)
                if 'label' in request_data or 'collaborator' in request_data:
                    if len(request_data['label']) != 0:
                        label_list = []
                        for label in request_data['label']:
                            print(label)
                            new_label = Label.objects.get(name=label)
                            label_list.append(new_label)
                    if len(request_data['collaborator']) != 0:
                        collaborator_list = []
                        for collaborator in request_data['collaborator']:
                            new_collaborator = User.objects.get(email=collaborator)
                            collaborator_list.append(new_collaborator)
                        response = self.function(request, *view_args, **kwargs)
                    else:
                        response = self.function(request, *view_args, **kwargs)
                else:
                    response = self.function(request, *view_args, **kwargs)
            else:
                return self.function(request, *view_args, **kwargs)
        except Label.DoesNotExist:
            response = Smd_Response(message='your label is not  valid please add label and try')

        except User.DoesNotExist:
            response = Smd_Response(message='for this email id user is not exist')
        except Exception:
            response = Smd_Response(message='something is wrong when validating your label or collaborator')
        return response


def login_required_middleware(get_response):
    def middleware(request):
        try:
            if re.match('^/api/', request.get_full_path()) and not re.match('^/api/token/', request.get_full_path()):
                bearer_token = request.META.get("HTTP_AUTHORIZATION", "")
                if bearer_token.startswith("Bearer"):
                    token = bearer_token.split(' ')
                    jwt.decode(token[1], settings.SECRET_KEY, algorithm="HS256")
                else:
                    response = Smd_Response(message='Bearer is missing in token')
                    return response
            return get_response(request)
        except DecodeError:
            response = Smd_Response(message='not valid token')
            return response
        except Exception:
            response = Smd_Response()
            return response

    return middleware