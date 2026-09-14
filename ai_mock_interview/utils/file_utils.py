import os
import tempfile
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = (
    os.path.join(tempfile.gettempdir(), "ai_mock_interview_uploads")
    if os.getenv("VERCEL") == "1"
    else "uploads"
)

def save_file(file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(path)
    return path