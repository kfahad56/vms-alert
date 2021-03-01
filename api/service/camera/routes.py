
from fastapi import routing, Request
from fastapi.responses import JSONResponse

from api.utils.logs import console_logger
from api.db.models import *
from api.service.camera.serializers import *
from api.utils import responses, utils_models

router = routing.APIRouter()

@router.post("/alert")
async def vms_webhook(request: Request):
    try: 
        payload = await request.body()       
        console_logger.debug(payload)
        return JSONResponse(content= utils_models.DefaultResponseModel(detail="success").dict(), status_code=200)
    except Exception as e:
        return {
            'error_message' : str(e)
        }
