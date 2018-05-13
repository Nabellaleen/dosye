# Import from external libraries
from path import Path
from werkzeug.utils import secure_filename


class FilesManagerException(Exception):
    pass


class FolderConfigException(FilesManagerException):

    def __init__(self):
        self.message = (
            "UPLOAD_FOLDER not found - Please check "
            "server configuration: UPLOAD_FOLDER must "
            "exists and have correct rights")

class ForbiddenFileAccessException(FilesManagerException):

    def __init__(self, file):
        self.file = file
        self.message = (
            f"The target file is outside the configured folder: {file}")


class FilesManager:

    files = []

    def __init__(self, folder):
        self.folder = Path(folder)

    def save(self, file):
        file_name = secure_filename(file.filename)
        file_path = self.folder / file_name
        try:
            file.save(file_path)
        except FileNotFoundError:
            raise FolderConfigException
        return file_name

    def get_files(self):
        try:
            return self.folder.files()
        except FileNotFoundError:
            raise FolderConfigException

    def delete(self, filename):
        file = self.folder / filename
        if not file.exists():
            raise FileNotFoundError(2, 'File not found', str(file))

        is_outside_folder = self.folder.relpathto(file).startswith('..')
        if is_outside_folder:
            raise ForbiddenFileAccessException(file)

        file.remove()
