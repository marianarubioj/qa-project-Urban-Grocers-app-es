import configuration
import data
import requests

from data import headers


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

authtoken = post_new_user(data.user_body)



def post_new_client_kit(kit_body):
    authtoken = post_new_user(data.user_body)
    authToken_new_user = authtoken.json()["authToken"]
    headers_authorization = data.headers.copy()
    headers_authorization["Authorization"] = f'Bearer {authToken_new_user}'
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                      json=kit_body,
                      headers=headers_authorization)
    return response


response_post_new_client = post_new_client_kit(data.kit_body)

