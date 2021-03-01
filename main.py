### Main application script ###
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect 
 
from api.service.camera.routes import router as sample_router
from api.utils.responses import responses

app = FastAPI()

connect(db="trudesk", username="trudesk", password="Trudesk1", host="mongo", authentication_source="admin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(
        sample_router,
        prefix="/camera",
        tags=["Camera"],
        responses=responses
    )
