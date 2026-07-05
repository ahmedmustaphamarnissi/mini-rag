from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings
import os


base_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1" , "data"]
)

@base_router.get("/upload/{project_id}")
async def upload_date(project_id : str , file : UploadFile , app_settings:Settings = Depends(get_settings)):
    return True