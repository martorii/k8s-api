from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import time
from utils.logger import setup_logger
from utils.preprocessing import extract_content_from_bytes


app = FastAPI()
logger = setup_logger(__name__)


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    logger.info("Working")
    return JSONResponse(content={"status": "healthy"}, status_code=200)


@app.post("/extract_content")
async def extract_content(data: UploadFile):
    """
    Accepts a file upload and returns its content
    """
    try:
        file_as_bytes = await data.read()
        return {
            "file_name": data.filename,
            "content": extract_content_from_bytes(file_as_bytes)
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/idle")
async def idle():
    idle_time: int = 10
    logger.info(f"idling for {idle_time} s...")
    time.sleep(idle_time)
    logger.info(f"Finished")
    return JSONResponse(content={}, status_code=200)
