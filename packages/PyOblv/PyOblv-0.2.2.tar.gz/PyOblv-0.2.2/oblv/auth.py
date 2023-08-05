from oblv.exceptions import BadRequestError
from .oblv_client import OblvClient
from .api.auth import authenticate_key_login_apikey_post
from .models import APIKey
from .client import Client
import logging

def authenticate(apikey: str):
    logging.warn("PyOblv is deprecated, and will not be supported in future. Kindly use oblv-ctl (https://pypi.org/project/oblv-ctl/) to access Oblivious APIs.")
    response = authenticate_key_login_apikey_post.sync(client=Client(), json_body=APIKey(apikey))
    return OblvClient(response.token,response.user_id)
