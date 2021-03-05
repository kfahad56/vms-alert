
from fastapi import routing, Request
from fastapi.responses import JSONResponse
import requests, json, base64, subprocess, string, random
from os import  path
from fastapi_utils.tasks import repeat_every
from pymongo import MongoClient
from bson.objectid import ObjectId

from api.utils.logs import console_logger
from api.db.models import *
from api.service.camera.serializers import *
from api.utils import responses, utils_models
from config import Config

router = routing.APIRouter()

global db, owner_id, group_id, access_token, ticket_type, ticket_priority

db= None
owner_id= None
group_id= None
access_token= None
ticket_type= None
ticket_priority= None

@router.post("/alert")
async def vms_webhook(payload:VMS):
    try:
        make_folder = 'mkdir images'
        path_check = '/app/videos/images'
        if path.exists(path_check):
            console_logger.debug('Path Exists')
        else:
            subprocess.Popen([make_folder], shell=True, stdout=None, stderr=None)
        imageName = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        imageData = payload.image 
        image_path = f"/app/images/{imageName}.jpg"
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(imageData))
        if all(v is not None for v in [owner_id, group_id, access_token, ticket_type, ticket_priority]):
            image_url = f'![image](/images/{imageName}.jpg)'
            url = Config.ticketing_base_url + "tickets/create"
            headers = {
                'accesstoken': access_token,
                'Content-Type': 'application/json'
            }
            postData = {
                "subject": "Person Detected",
                "issue": image_url,
                "owner": owner_id,
                "type": ticket_type,
                "priority": ticket_priority,
                "group" : group_id
            }
            response = requests.post(url, headers=headers, data=json.dumps(postData))
            # console_logger.debug(response.text)
        return JSONResponse(content= utils_models.DefaultResponseModel(detail="success").dict(), status_code=200)
    except Exception as e:
        return {
            'error_message' : str(e)
        }

@repeat_every(seconds=60)
def check_credentials():
    return_response = None
    global owner_id, group_id, access_token, ticket_type, ticket_priority
    account_collection = db.accounts
    groups_collection = db.groups
    ticket_type_collection = db.tickettypes
    priority_collection = db.priorities
    if account_collection.find_one({"username":"admin"}):
        account = account_collection.find_one({"username":"admin"})
        priority = priority_collection.find_one({"name":"Critical"})
        t_type = ticket_type_collection.find_one({"name":"Issue"})
        
        owner_id = str(account["_id"])
        access_token = str(account["accessToken"])
        ticket_priority = str(priority["_id"])
        ticket_type = str(t_type["_id"])
        
        if groups_collection.find_one({"name":"person"}):
            group = groups_collection.find_one({"name":"person"})
            group_id = str(group["_id"])
        else:
            url = Config.ticketing_base_url + "groups/create"
            headers = {
                'accesstoken': access_token,
                'Content-Type': 'application/json'
            }
            payload = {"name" : "person"}
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:    
                result = response.json()
                group_id = str(result["group"]["_id"])
                return_response = 'successs'
    else:
        return_response ='failure'
    return return_response


@router.on_event('startup')
async def check_id():
    global db
    client = MongoClient('mongodb://trudesk:TruDesk1@mongo')
    db = client.trudesk
    await check_credentials()
    return 'success'
