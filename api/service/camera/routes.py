import subprocess, glob, botocore, os
from botocore.exceptions import NoCredentialsError
from os import access, path
from typing import List
from fastapi import routing, Depends, Header,HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.param_functions import Query
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from pymongo.mongo_client import MongoClient

from api.utils.logs import console_logger
from api.db.models import *
from api.service.camera.serializers import *
from api.utils import responses, utils_models
from config import Config

router = routing.APIRouter()

@router.post("/alert")
async def shinobi_webhook(request: Request):
    try: 
        payload = await request.body()       
        console_logger.debug(payload)
        return JSONResponse(content= utils_models.DefaultResponseModel(detail="success").dict(), status_code=200)
    except Exception as e:
        return {
            'error_message' : str(e)
        }
