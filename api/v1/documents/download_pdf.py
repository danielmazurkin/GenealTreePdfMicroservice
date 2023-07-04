from api import app
import os
from fastapi.responses import FileResponse, JSONResponse


@app.get("/download/{id_people}")
async def download_file(id_people: str):
    """Возвращает последний сформированный PDF файла."""
    path_by_data = os.path.join('./data', id_people, 'out.pdf')
    result_response = None

    if os.path.exists(path_by_data):
        result_response = FileResponse(path_by_data, filename='out.pdf')
    else:
        error_message = {"message": "File not found"}
        result_response = JSONResponse(content=error_message, status_code=404)

    return result_response

