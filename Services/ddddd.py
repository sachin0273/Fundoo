import requests
import json

context = {
    "provider": "facebook",
    "code": "AQDs"
            "-PJaiM4IvsFGzg35wAU04XeP878ooq5WXD2X6Y_p67vG5rQlZQqwnZZDkVjGadO905AwcrcrdQCexKovmtlVjfckmzeqAoKbKbzDYO_qoB8vf4RDmQFxo87lOk3EzdEZivPPYE6XMTeOy7meqzYyjTsOuWNf1u0KPmC3Pep0aw56O8RUzLFNbIli6SIax_P1yj3CCDd-slV9ezbR4CGDpFSfDN-KK6jBmBqnhhLrmp1J2RcUGNpcs1Xn8W7mK_WKXcEk75csGMdi7P7E9xN5lVi3SE93YVwDCtu95BEmNQrmbB3iVwL7Bo1YUJqeDcJw6axsAUmdI9EU-59ycpmsu "
}
response = requests.post('http://localhost:8000/api/login/social/jwt-pair/', json.dumps(context))
# print(json.loadresponse.text))
print(response.status_code)
