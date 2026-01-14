from typing import Any
from fastapi import APIRouter, HTTPException
from api.schemas import TextRequest, UpdateConfigRequest
from config.setup import prompt_system_service, history_service, config_service

router = APIRouter()


@router.post("/generate_answer")
async def generate_response(req: TextRequest) -> Any:

    response_type, response_data = prompt_system_service.process_prompt(req.prompt)

    if response_type == "rejected":
        raise HTTPException(status_code=400, detail=response_data["message"])

    return response_data


@router.get("/retrieve_history")
async def get_history() -> Any:
    return history_service.get_full_history()


@router.patch("/system_prompt_config")
async def config_system_prompt(request: UpdateConfigRequest) -> Any:

    try:
        config_service.update_config(
            section=request.section, key=request.key, value=request.value
        )
        return {"status": "success", "message": "Settings Updated"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
