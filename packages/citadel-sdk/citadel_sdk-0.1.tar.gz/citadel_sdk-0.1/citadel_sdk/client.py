import base64
import requests
import os
import json
import sys
import time
import urllib.request, urllib.parse, urllib.error

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

#handler = logging.FileHandler('mylog.log')
handler = logging.StreamHandler(sys.stdout)
# create a logging format
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

from cryptography.fernet import Fernet

##### utils
def _server_error(resp):
    if "error" in resp:
        return True
    
    return False

def _encrypt(data, key_filename=None):
    if key_filename is None:
        key = Fernet.generate_key()
    else:
        with open(key_filename, "rb") as f:
            key = f.read()

    fernet = Fernet(key)
    if not isinstance(data, bytes):
        data = data.encode("utf-8")
    token = fernet.encrypt(data)

    return token, key

def _decrypt(encrypted_data, key_filename):
    with open(key_filename, "rb") as f:
        key = f.read()

    fernet = Fernet(key)
    if not isinstance(encrypted_data, bytes):
        encrypted_data = encrypted_data.encode("utf-8")
    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data

def _load_config_file(config=dict(), filename=None):
    if filename.startswith("~"):
        filename = os.path.expanduser(filename)

    if os.path.isfile(filename):
        json_data = {}
        with open(filename, "r") as json_file:
            try:
                filecontent = json_file.read()
                json_data = json.loads(filecontent)
                config.update(json_data)
            except Exception:
                raise

    return config

##### end utils


class CitadelServiceClient(object):
    '''
    The Citadel management service client can be used to interact with the Citadel service.
    It enables the following:
    - uploading, downloading, listing and deleting assets (datasets, models, code, test)
    - creating, listing, starting, checking and deleting training sessions
    - downloading trained models after a training session
    - consenting to participate in training sessions

    '''

    def __init__(self, config_filename="citadel_settings.json"):
        '''
        Initializes the service client.

        Args:
            config_filename (string): the config filename path to be used; default: "citadel_settings.json"

        Note:
            The config should contain the following:
            - citadel_url (string): the Citadel management service URL
            - citadel_user (string): the email address of the user
            - citadel_password (string): the password of the user
            - citadel_name (string): the name of the user for signing up (optional; only used for when registering)
            - proxies (dictionary): a dictionary of proxy addresses

        '''
        log.info("Using configuration file: %s", config_filename)
        config = _load_config_file(filename=config_filename)
        log.debug(config)
        self._url = str(config.get('citadel_url', None))
        self._email = config.get('citadel_user', None)
        self._password = config.get('citadel_password', None)
        self._name = config.get('citadel_name', "")
        
        if not self._url or not self._email or not self._password:
            raise Exception("Missing configuration parameter(s).")

        self._token = None
        self._proxies = config.get('proxies', None)

        self._s = requests.Session()

        if self._proxies:
            self._s.proxies.update(self._proxies)

        self._s.verify=False
        self._s.max_redirects = 10

        log.info("Citadel service at: %s", self._url)

    def disconnect(self):
        self._token = None
        if self._s is not None:
            self._s.close()

    def _action(self, action, data_to_send={}):
        data_to_send["user_email"] = self._email
        if self._token is not None:
            data_to_send["user_token"] = self._token

        data_to_send["action"] = action

        log.debug(str(data_to_send)[0:255])

        result = self._s.post(self._url, json=data_to_send)
        response = result.json()
        if _server_error(response):
            raise Exception("Server error: {}".format(response["error"]))
        
        return response

    def register(self):
        '''
        Register the user for the Citadel service.
        Uses the configuration specified when initializing the client.

        Returns:
            `True` when successful; `False` otherwise.

        '''
        log.info("Registering user: %s (%s)", self._email, self._name)

        data_to_send = {}
        data_to_send["user_password"] = self._password
        data_to_send["user_name"] = self._name

        try:
            resp = self._action("register", data_to_send)
            log.info(resp["message"])
        except Exception as exc:
            return False

        return True

    def login(self):
        '''
        Login the user for the Citadel service.
        Uses the configuration specified when initializing the client.

        Returns:
            `True` when successful; `False` otherwise

        '''
        log.info(f"Logging in: %s", self._email)

        data_to_send = {}
        data_to_send["user_password"] = self._password

        try:
            resp = self._action("login", data_to_send)
            log.debug(resp)
            self._token = resp['user_token']
        except Exception as exc:
            return False

        return True

    def delete_user(self):
        '''
        Delete the user from the Citadel service.
        Uses the configuration specified when initializing the client.

        Returns:
            `True` when successful; `False` otherwise

        '''
        log.info(f"Deleting user account: %s", self._email)

        try:
            resp = self._action("delete_user")
            log.info(resp["message"])
            self._disconnect()
        except Exception as exc:
            return False

        return True

    def list_assets(self, asset_type):
        '''
        List the assets for this user.

        Args:
            asset_type (string): one of "code", "model", "dataset" or "test"

        Returns:
            A dictionary with this user's assets with their `id` (as key), `asset_type`, `name` and `description`
        
        '''
        assert asset_type in ["code", "model", "dataset", "test"]

        try:
            resp = self._action("list_" + asset_type + "s")
            log.debug(resp)
        except Exception as exc:
            return {}

        return resp[asset_type + "s"]

    def list_models(self):
        '''
        List the model assets for this user.

        Returns:
            A dictionary with this user's models with their `id` (as key), `asset_type`, `name` and `description`

        '''
        return self.list_assets("model")

    def list_codes(self):
        '''
        List the code assets for this user.
        The code assets can be about 1) model updating, 2) model training and 3) data preparation.

        Returns:
            A dictionary with this user's code assets with their `id` (as key), `asset_type`, `name` and `description`
        
        '''
        return self.list_assets("code")

    def list_tests(self):
        '''
        List the test data assets for this user.

        Returns:
            A dictionary with this user's test data assets with their `id` (as key), `asset_type`, `name` and `description`
        
        '''
        return self.list_assets("test")

    def list_datasets(self):
        '''
        List the dataset assets for this user.

        Returns:
            A dictionary with this user's datasets with their `id` (as key), `asset_type`, `name` and `description`

        '''
        return self.list_assets("dataset")

    def delete_asset(self, asset_type, asset_id):
        '''
        Delete an asset for this user.

        Args:
            asset_type (string): one of "code", "model", "dataset" or "test"
            asset_id (string): The id of the asset to be deleted

        Returns:
            True` when successful; `False` otherwise
        
        '''
        assert asset_type in ["code", "model", "dataset", "test"]

        data_to_send = {}
        data_to_send["id"] = asset_id

        try:
            resp = self._action("delete_" + asset_type, data_to_send)
            log.info(resp["message"])
        except Exception as exc:
            return False

        return True

    def delete_model(self, model_id):
        '''
        Delete a model asset for this user.

        Args:
            model_id (string): The id of the model asset

        Returns:
            Boolean: `True` when successful; `False` otherwise

        '''
        return self.delete_asset("model", model_id)

    def delete_code(self, code_id):
        '''
        Delete a code asset for this user.

        Args:
            code_id (string): The id of the code asset

        Returns:
            Boolean: `True` when successful; `False` otherwise

        '''
        return self.delete_asset("code", code_id)

    def delete_test(self, test_id):
        '''
        Delete a test data asset for this user.

        Args:
            test_id (string): The id of the model asset

        Returns:
            Boolean: `True` when successful; `False` otherwise

        '''
        return self.delete_asset("test", test_id)

    def delete_dataset(self, dataset_id):
        '''
        Delete a dataset asset for this user.

        Args:
            dataset_id (string): The id of the dataset asset

        Returns:
            Boolean: `True` when successful; `False` otherwise

        '''
        return self.delete_asset("dataset", dataset_id)

    def upload_asset(self, asset_type, name, description, data, should_encrypt=True):
        '''
        Create and upload an asset for this user.

        Args:
            asset_type (string): one of "code", "model", "dataset" or "test"
            name (string): the name of the asset
            description (string): the description of the asset
            data (string or bytes): the raw data of the asset
            should_encrypt (boolean): whether the asset should be encrypted before uploading (`True` by default)

        Returns:
            id (string): The id of the asset uploaded
        
        Note:
            When `should_encrypt` is `True`, then a new random key is generated and stored in a file in `asset_keys` folder.
            The name of the file will be "`asset_type`_`asset_id`.key".
            When `download_asset` is later called with `should_decrypt=True`, then the keyfile will be used.

        '''
        assert asset_type in ["code", "model", "dataset", "test"]

        if should_encrypt:
            encrypted_data, key = _encrypt(data)

        data_to_send = {}
        data_to_send["name"] = name
        data_to_send["description"] = description
        data_to_send["data"] = encrypted_data.decode()

        try:
            resp = self._action("create_" + asset_type, data_to_send)
            log.debug(resp)
        except Exception as exc:
            return None

        # extract asset id, so that we can store the key
        asset_id = resp["id"]
        key_filename = "asset_keys/" + asset_type + "_" + asset_id + ".key"
        with open(key_filename, "wb") as f:
            f.write(key)

        # TODO: chunking
        # TODO: chunking of the data with "upload_asset_data"

        return asset_id

    def upload_model(self, name, description, data):
        '''
        Upload a model asset for this user.

        Args:
            name (string): the name of the model
            description (string): the description of the model
            data (string or bytes): the raw data of the model

        Returns:
            id (string): The id of the model uploaded

        '''
        return self.upload_asset("model", name, description, data)

    def upload_code(self, name, description, data):
        '''
        Upload a code asset for this user.
        The code asset can be about 1) model updating, 2) model training and 3) data preparation.

        Args:
            name (string): the name of the code
            description (string): the description of the code
            data (string or bytes): the raw data of the code

        Returns:
            id (string): The id of the model uploaded

        '''
        return self.upload_asset("code", name, description, data)

    def upload_test(self, name, description, data):
        '''
        Upload a test data asset for this user.

        Args:
            name (string): the name of the test data
            description (string): the description of the test data
            data (string or bytes): the raw data of the test data

        Returns:
            id (string): The id of the test data uploaded

        '''
        return self.upload_asset("test", name, description, data)

    def upload_dataset(self, name, description, data):
        '''
        Upload a dataset asset for this user.

        Args:
            name (string): the name of the dataset
            description (string): the description of the dataset
            data (string or bytes): the raw data of the dataset

        Returns:
            id (string): The id of the dataset uploaded

        '''
        return self.upload_asset("dataset", name, description, data)

    def download_asset(self, asset_type, asset_id, should_decrypt=True):
        '''
        Download an asset for this user.

        Args:
            asset_type (string): one of "code", "model", "dataset" or "test"
            id (string): The id of the asset
            should_decrypt (boolean): whether the asset should be decrypted after downloading (`True` by default)

        Returns:
            The raw data of the asset downloaded (bytes)
        
        Note:
            When `should_decrypt` is `True`, then a keyfile in folder `asset_keys` will be used.
            The name of the file will be "`asset_type`_`asset_id`.key".
            The keyfile will be automatically created when `upload_asset()` is called with `should_encrypt=True`.

        '''
        assert asset_type in ["code", "model", "dataset", "test"]

        data_to_send = {}
        data_to_send["id"] = asset_id

        # TODO: chunking

        resp = self._action("download_" + asset_type, data_to_send)

        # use asset id, so that we can get the key and decrypt

        asset_data = resp[asset_type]
        key_filename = "asset_keys/" + asset_type + "_" + asset_id + ".key"
        if should_decrypt:
            asset_data = _decrypt(asset_data, key_filename)
        log.debug(resp)

        return asset_data

    def download_model(self, model_id):
        '''
        Download a model asset for this user.

        Args:
            model_id (string): The id of the model

        Returns:
            The raw data of the model downloaded (bytes)

        '''
        return self.download_asset("model", model_id)
    
    def download_code(self, code_id):
        '''
        Download a code asset for this user.
        The code assets can be about 1) model updating, 2) model training and 3) data preparation.

        Args:
            code_id (string): The id of the code

        Returns:
            The raw data of the code downloaded (bytes)

        '''
        return self.download_asset("code", code_id)

    def download_test(self, test_id):
        '''
        Download a test data asset for this user.

        Args:
            test_id (string): The id of the test data

        Returns:
            The raw data of the test data downloaded (bytes)

        '''
        return self.download_asset("test", test_id)
    
    def download_dataset(self, dataset_id):
        '''
        Download a dataset asset for this user.

        Args:
            dataset_id (string): The id of the dataset

        Returns:
            The raw data of the dataset downloaded (bytes)

        '''
        return self.download_asset("dataset", dataset_id)

    def create_training_session(self, model_id, code_training_id, code_updating_id, code_preparation_id, test_data_id, dataset_owners):
        '''
        Create a training session for this user.

        Args:
            model_id (string): the id of the model asset to be trained in this training
            code_training_id (string): the id of the code asset to be used in this training (for training)
            code_updating_id (string): the id of the code asset to be used in this training (for model updating)
            code_preparation_id (string): the id of the code asset to be used in this training (for data preparation)
            test_data_id (string): the id of the test data asset to be used in this training (for testing)
            dataset_owners (list of strings): the email addresses of the dataset owners to participate in this training

        Returns:
            id (string): The id of the training session created
        
        Note:
            The dataset owners should have created an account.
            It is assumed that the model owner and dataset owners have exchanged information about which datasets to be used.
            The dataset owners will specify which datasets should be used in this training when they give their consent.

        '''
        data_to_send = {}
        data_to_send["model_id"] = model_id
        data_to_send["code_training_id"] = code_training_id
        data_to_send["code_updating_id"] = code_updating_id
        data_to_send["code_preparation_id"] = code_preparation_id
        data_to_send["test_data_id"] = test_data_id
        data_to_send["dataset_owners"] = dataset_owners

        try:
            resp = self._action("create_training_session", data_to_send)
            log.debug(resp)
        except Exception as exc:
            return False

        return resp["id"]

    def get_pending_consents(self):
        '''
        Retrieve pending participation invitations in a training session for this user.

        Returns:
            A dictionary of pending invitations with information about the model owner, list of invited dataset owners and training session id

        '''
        try:
            resp = self._action("get_pending_consents")
            log.debug(resp)
        except Exception as exc:
            return {}

        return resp["pending_consents"]

    def accept_training_session(self, training_id, dataset_id):
        '''
        Accept a training session and give consent for participation in a training as a dataset owner.

        Args:
            training_id (string): the id of the training session to participate
            dataset_id (string): the id of the dataset to contribute to the training session
        
        Returns:
            `True` when successful; `False` otherwise

        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id
        data_to_send["dataset_id"] = dataset_id

        try:
            resp = self._action("accept_training_session", data_to_send)
            log.info(resp["message"])
        except Exception as exc:
            return False

        return True

    def get_training_session_consents(self, training_id):
        '''
        Get the consent flags of the training session.

        Args:
            training_id (string): the id of the training session
        
        Returns:
            The consent flags from the dataset owners of the training session (dictionary)

        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id
        
        try:
            resp = self._action("get_training_session_consents", data_to_send)
            log.debug(resp)
        except Exception as exc:
            return {}

        return resp["consent_status"]
        
    def list_training_sessions(self):
        '''
        List the training sessions for this user.

        Returns:
            A list with this user's training session ids
        
        '''
        try:
            resp = self._action("list_training_sessions")
            log.debug(resp)
        except Exception as exc:
            return {}

        return resp["training_sessions"]

    def get_training_session_details(self, training_id):
        '''
        Get the details of the training session.

        Args:
            training_id (string): the id of the training session
        
        Returns:
            The details of the training session (dictionary)
        
        Note:
            The details include the asset ids for model, code and test data, participating dataset owners, their consents and their dataset ids and its status.

        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id

        try:
            resp = self._action("get_training_session_details", data_to_send)
            log.debug(resp)
        except Exception as exc:
            return None
        
        return resp["training"]

    def get_training_session_status(self, training_id):
        '''
        Get the status of the training session.

        Args:
            training_id (string): the id of the training session
        
        Returns:
            The status of the training session (string); one of "created", "running", "stopped", "finished"

        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id

        try:
            resp = self._action("get_training_session_status", data_to_send)
            log.debug(resp)
        except Exception as exc:
            return None

        return resp["status"]
    
    def download_trained_model(self, training_id, should_decrypt=True):
        '''
        Download the trained final model from a training session for this user.

        Args:
            training_id (string): The id of the training session, in which the model was trained

        Returns:
            The raw data of the trained model downloaded (bytes)

        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id

        # TODO: chunking

        resp = self._action("download_trained_model", data_to_send)

        # TODO: double check later on
        asset_type = "model"
        asset_data = resp["trained_model"]
        asset_id = resp["id"]
        key_filename = "asset_keys/" + asset_type + "_" + asset_id + ".key"
        if should_decrypt:
            asset_data = _decrypt(asset_data, key_filename)
        log.debug(resp)

        return asset_data

    def delete_training_session(self, training_id):
        '''
        Delete a training session for this user.

        Args:
            training_id (string): The id of the training session to be deleted

        Returns:
            `True` when successful; `False` otherwise
        
        '''
        data_to_send = {}
        data_to_send["training_id"] = training_id

        try:
            resp = self._action("delete_training_session", data_to_send)
            log.info(resp)
        except Exception as exc:
            return False
        
        return True

    def start_training_session(self, training_id):
        '''
        Start a training session for this user.

        Args:
            training_id (string): the id of the training session
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not implemented yet.

        '''
        return False
    
    def upload_asset_key(self, asset_type, asset_id, asset_key=None):
        '''
        Remotely attest to the key storage enclave and upload the decryption key of an asset for this user.

        Args:
            asset_type (string): one of "code", "model", "dataset" or "test"
            asset_id (string): the id of the asset
            asset_key (string or bytes): the key to upload (optional; if not given, the client will try to read the key from the file "`asset_keys`/`asset_type`_`asset_id`.key"
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not (fully) implemented yet (missing remote attestation and encryption).

        '''
        assert asset_type in ["code", "model", "dataset", "test"]

        if not asset_key:
            # get the asset key
            key_filename = "asset_keys/" + asset_type + "_" + asset_id + ".key"
            with open(key_filename, "rb") as f:
                asset_key = f.read()

        if not isinstance(asset_key, bytes):
            asset_key = asset_key.encode("utf-8")

        # TODO: attest to the Key Storage Enclave
        # TODO: extract public key of the Key Storage Enclave
        # TODO: use the public key to encrypt the asset key
        encrypted_asset_key = asset_key.decode()

        data_to_send = {}
        data_to_send["asset_id"] = asset_id
        data_to_send["encrypted_asset_key"] = encrypted_asset_key

        try:
            resp = self._action("upload_key_" + asset_type, data_to_send)
            log.debug(resp)
        except Exception as exc:
            return False

        return True

    def upload_model_key(self, model_id, model_key=None):
        '''
        Remotely attest to the key storage enclave and upload the decryption key of a model for this user.

        Args:
            model_id (string): the id of the model
            model_key (string or bytes): the key to upload (optional; if not given, the client will try to read the key from the file "`asset_keys`/model_`asset_id`.key"
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not (fully) implemented yet (missing remote attestation and encryption).

        '''
        return self.upload_asset_key("model", model_id, model_key)

    def upload_code_key(self, code_id, code_key=None):
        '''
        Remotely attest to the key storage enclave and upload the decryption key of a code asset for this user.

        Args:
            code_id (string): the id of the code
            code_key (string or bytes): the key to upload (optional; if not given, the client will try to read the key from the file "`asset_keys`/code_`asset_id`.key"
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not (fully) implemented yet (missing remote attestation and encryption).

        '''
        return self.upload_asset_key("code", code_id, code_key)

    def upload_test_key(self, test_id, test_key=None):
        '''
        Remotely attest to the key storage enclave and upload the decryption key of a test asset for this user.

        Args:
            test_id (string): the id of the test
            test_key (string or bytes): the key to upload (optional; if not given, the client will try to read the key from the file "`asset_keys`/test_`asset_id`.key"
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not (fully) implemented yet (missing remote attestation and encryption).

        '''
        return self.upload_asset_key("test", test_id, test_key)

    def upload_dataset_key(self, dataset_id, dataset_key=None):
        '''
        Remotely attest to the key storage enclave and upload the decryption key of a dataset for this user.

        Args:
            dataset_id (string): the id of the dataset
            dataset_key (string or bytes): the key to upload (optional; if not given, the client will try to read the key from the file "`asset_keys`/dataset_`asset_id`.key"
        
        Returns:
            `True` when successful; `False` otherwise

        Note:
            Not (fully) implemented yet (missing remote attestation and encryption).

        '''
        return self.upload_asset_key("dataset", dataset_id, dataset_key)
