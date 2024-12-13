from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Путь к папке, где находятся изображения
    upload_folder = "C:\\Users\\PC\\PycharmProjects\\pythonProject"

    # Сохранение файла
    file_location = os.path.join(upload_folder, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename, "file_location": file_location}
