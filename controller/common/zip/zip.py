import os
import zipfile
import base64
from io import BytesIO

from controller.action_config.zip_exclude import ZIP_EXCLUDE_FILES, ZIP_EXCLUDE_DIRS


class ZipTool:
    @classmethod
    def zip_dir(
        cls,
        dir_path: str,
        exclude_files: tuple = (),
        exclude_dirs: tuple = (),
    ) -> str:
        """
        Zip directory.

        :param dir_path: [str] directory path.
        :param exclude_files: [tuple] files to exclude.
        :param exclude_dirs: [tuple] directories to exclude.
        :return: [str] base64 encoded zip data.
        """
        exclude_files += ZIP_EXCLUDE_FILES
        exclude_dirs += ZIP_EXCLUDE_DIRS

        buf = BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zipf:
            ZipTool._walk_and_zip(dir_path, zipf, exclude_files, exclude_dirs)
        buf.seek(0)
        zip_data = buf.getvalue()
        return base64.b64encode(zip_data).decode("utf-8")

    @classmethod
    def _walk_and_zip(
        cls,
        dir_path: str,
        zipf: zipfile.ZipFile,
        exclude_files: tuple = (),
        exclude_dirs: tuple = (),
    ) -> None:
        """
        Walk and zip directory.

        :param dir_path: [str] directory path.
        :param zipf: [zipfile.ZipFile] zipfile object.
        :param exclude_files: [tuple] files to exclude.
        :param exclude_dirs: [tuple] directories to exclude.
        """
        for root, dirs, files in os.walk(dir_path):
            dirs[:] = [dir_ for dir_ in dirs if dir_ not in exclude_dirs]
            for file in files:
                file_path = os.path.join(root, file)
                relative_file_path = os.path.relpath(file_path, start=dir_path)
                if relative_file_path not in exclude_files:
                    zipf.write(file_path, relative_file_path)
