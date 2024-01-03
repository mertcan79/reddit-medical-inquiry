from __future__ import annotations
from .process_post import get_results
from fastapi import APIRouter, Depends, HTTPException

from app.apis.api_a.mainmod import main_func as main_func_a
from app.apis.api_b.mainmod import main_func as main_func_b
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of fastapi-nano. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/processed-results")
def get_processed_results():
    try:
        results = get_results()
        return {"data": results}
    except Exception as e:
        # Handle exceptions and return an appropriate error response
        raise HTTPException(status_code=500, detail=str(e))