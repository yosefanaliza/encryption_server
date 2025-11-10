from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import api.services.caesar as caesar_services
import api.services.fence as fence_services
from utils.endpoint_logger import get_logger
import time

router = APIRouter()
logger = get_logger()

class CaesarRequest(BaseModel):
    text: str
    offset: int
    mode: str


@router.post('/caesar')
def caesar(request: CaesarRequest):
    """
    Caesar cipher encryption/decryption
    Body: { "text": string, "offset": int, "mode": "encrypt"/"decrypt" }
    """
    logger.request_received('/caesar', 'POST')
    start_time = time.time()

    if request.mode not in ['encrypt', 'decrypt']:
        raise HTTPException(status_code=400, detail="Mode must be 'encrypt' or 'decrypt'")
    

    

    response = {}

    try:
        if request.mode == 'encrypt':
            result = caesar_services.caesar_cipher_encrypt(request.text, request.offset)
            response = {"encrypted_text": result}
        else:
            result = caesar_services.caesar_cipher_decrypt(request.text, request.offset)
            response = {"decrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    handling_time = time.time() - start_time
    logger.update_handling_time('/caesar', 'POST', handling_time)
    
    return response
@router.get('/fence/encrypt')
def fence_encrypt(text: str = Query(..., description="Text to encrypt")):
    """
    Fence cipher encryption
    Query param: text=<string>
    """
    logger.request_received('/fence/encrypt', 'GET')
    start_time = time.time()
    
    try:
        result = fence_services.fence_cipher_encrypt(text)
        response = {"encrypted_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    handling_time = time.time() - start_time
    logger.update_handling_time('/fence/encrypt', 'GET', handling_time)
    
    return response




class FenceDecryptRequest(BaseModel):
    text: str

@router.post('/fence/decrypt')
def fence_decrypt(request: FenceDecryptRequest):
    """
    Fence cipher decryption
    Body: { "text": string }
    """
    logger.request_received('/fence/decrypt', 'POST')
    start_time = time.time()
    
    try:
        result = fence_services.fence_cipher_decrypt(request.text)
        response = {"decrypted": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    handling_time = time.time() - start_time
    logger.update_handling_time('/fence/decrypt', 'POST', handling_time)
    
    return response


@router.get("/health")
def health_check():
    """Health check endpoint"""
    logger.request_received('/health', 'GET')
    start_time = time.time()
    
    response = {"status": "healthy"}
    
    handling_time = time.time() - start_time
    logger.update_handling_time('/health', 'GET', handling_time)
    
    return response