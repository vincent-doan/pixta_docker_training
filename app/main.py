from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from convert_to_bw import convert_to_black_and_white

app = FastAPI()

@app.post("/upload")
async def upload_file_and_convert_to_bw(file: UploadFile = File(...)):
    # Create a temporary directory to save uploaded files
    os.makedirs("temp", exist_ok=True)
    
    file_path = os.path.join("temp", file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    output_path = convert_to_black_and_white(file_path, "temp/image_bw.jpg")

    if output_path is None:
        return {"error": "Failed to process the image"}

    return FileResponse(output_path, media_type="image/jpeg", filename="image_bw.jpg")