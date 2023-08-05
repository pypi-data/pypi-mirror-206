import json
import logging
import time
import requests
from hdb import util, config

EXPIRY_TIME = 'expiry_time'
TOKEN_ID = 'token_id'
TOKEN_INFO = 'token_info'
TOKEN_INFOS = 'token_infos'
TOKEN_VALUE = 'token_value'
TOKEN_CONFIG = 'token_config'
TOKEN_LIFETIME = 'lifetime_seconds'
GRACE_PERIOD = 'grace_period_ms'


def list_tokens(db_instance: str):
    logging.info('Fetching list of tokens')
    response = requests.get('https://{}/api/2.0/token/list'.format(db_instance))
    token_list = None
    if response.ok:
        token_list = response.json()
    else:
        util.log_response(response, 'unable to fetch list of tokens!')
    response.close()
    return token_list


def get_token_info(token_config: dict, token_list: dict):
    if token_config is None:
        return None
    token_id = token_config[TOKEN_ID]
    if token_list is not None:
        for token in token_list[TOKEN_INFOS]:
            if token[TOKEN_ID] == token_id:
                return token
    return None


def create_token(db_instance: str, token_lifetime: int):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'comment': 'Habu Databricks cli API token',
        TOKEN_LIFETIME: token_lifetime,
    }
    token = None
    response = requests.post('https://{}/api/2.0/token/create'.format(db_instance),
                             headers=headers, data=json.dumps(data))
    if response.ok:
        token = response.json()
    else:
        util.log_response(response, 'Unable to create token!')
    response.close()
    return token


def revoke_token(db_instance: str, token_id: str):
    if token_id is not None:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {TOKEN_ID: token_id}
        response = requests.post('https://{}/api/2.0/token/delete'.format(db_instance),
                                 headers=headers, data=json.dumps(data))
        if not response.ok:
            util.log_response(response, f'Unable to revoke token {TOKEN_ID} : {token_id}!')
        response.close()


def update_auth(db_instance: str, token: dict, config_file: str):
    if token is not None:
        token_val = token[TOKEN_VALUE]
        token_info = token[TOKEN_INFO]
        netrc = config.open_netrc()
        netrc[db_instance] = {
            'login': 'token',
            'password': token_val
        }
        netrc.save()
        token_config = {
            TOKEN_ID: token_info[TOKEN_ID],
            EXPIRY_TIME: token_info[EXPIRY_TIME]
        }
        config.update_config(config_file, TOKEN_CONFIG, token_config)


def update_and_revoke_token(db_instance: str, token: dict, token_config: dict, config_file: str):
    if token is not None:
        update_auth(db_instance, token, config_file)
        # revoke older token if it exists
        if token_config is not None:
            revoke_token(db_instance, token_config.get(TOKEN_ID))


def setup_token(db_instance: str, editable_config_file: str, config_params: dict, res_config: dict):
    token = None
    token_config = res_config[TOKEN_CONFIG]
    token_info = get_token_info(config_params.get(TOKEN_CONFIG), list_tokens(db_instance))
    if token_info is not None:
        time_diff = token_info[EXPIRY_TIME] - int(time.time() * 1000)
        if time_diff < token_config[GRACE_PERIOD]:
            token = create_token(db_instance, token_config[TOKEN_LIFETIME])
    else:
        token = create_token(db_instance, token_config[TOKEN_LIFETIME])
    update_and_revoke_token(db_instance, token, token_config, editable_config_file)
