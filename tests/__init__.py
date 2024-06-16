from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

__all__ = ["BaseModel"]

storage = FileStorage()
storage.reload()

BaseModel.sorage = storage
