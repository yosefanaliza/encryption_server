from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import api.services.caesar as caesar_services
import api.services.fence as fence_services
from utils.endpoint_logger import get_endpoint_logger
from utils.summery_logger import get_summery_logger
import time

router = APIRouter()
endpoint_logger = get_endpoint_logger()
summery_logger = get_summery_logger()


class CaesarRequest(BaseModel):
    text: str
    offset: int
    mode: str


@router.post("/caesar")
def caesar(request: CaesarRequest):
    """
    Caesar cipher encryption/decryption
    Body: { "text": string, "offset": int, "mode": "encrypt"/"decrypt" }
    """
    endpoint_logger.request_received("/caesar", "POST")
    start_time = time.time()

    if request.mode not in ["encrypt", "decrypt"]:
        raise HTTPException(
            status_code=400, detail="Mode must be 'encrypt' or 'decrypt'"
        )

    response = {}

    try:
        if request.mode == "encrypt":
            result = caesar_services.caesar_cipher_encrypt(request.text, request.offset)
            response = {"encrypted_text": result}
        else:
            result = caesar_services.caesar_cipher_decrypt(request.text, request.offset)
            response = {"decrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    handling_time = time.time() - start_time
    endpoint_logger.update_handling_time("/caesar", "POST", handling_time)
    summery_logger.load_summery()

    return response


@router.get("/fence/encrypt")
def fence_encrypt(text: str = Query(..., description="Text to encrypt")):
    """
    fence cipher encryption
    GET /fence/encrypt?text=<text>
    """
    endpoint_logger.request_received("/fence/encrypt", "GET")
    start_time = time.time()

    try:
        result = fence_services.fence_cipher_encrypt(text)
        response = {"encrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    handling_time = time.time() - start_time
    endpoint_logger.update_handling_time("/fence/encrypt", "GET", handling_time)
    summery_logger.load_summery()

    return response


class FenceDecryptRequest(BaseModel):
    text: str


@router.post("/fence/decrypt")
def fence_decrypt(request: FenceDecryptRequest):
    """
    fence cipher decryption
    POST /fence/decrypt
    Body: { "text": "string" }
    """
    endpoint_logger.request_received("/fence/decrypt", "POST")
    start_time = time.time()

    try:
        result = fence_services.fence_cipher_decrypt(request.text)
        response = {"decrypted": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    handling_time = time.time() - start_time
    endpoint_logger.update_handling_time("/fence/decrypt", "POST", handling_time)
    summery_logger.load_summery()

    return response


@router.get("/health")
def health_check():
    return {"status": "healthy"}
