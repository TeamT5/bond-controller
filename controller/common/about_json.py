import json
from typing import Union


class Json:
    @staticmethod
    def load_json(filepath: str) -> dict:
        """
        Load json file.

        :param filepath: [str] json 檔案路徑
        :return: [dict] json 檔案內容
        """
        with open(filepath, "r") as f:
            return json.load(f)

    @staticmethod
    def dump_json(filepath: str, data: Union[dict, str]) -> None:
        """
        Dump json file.

        :param filepath: [str] json 檔案路徑
        :param data: [Union[dict, str]] 檔案內容
        """
        if isinstance(data, dict):
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        elif isinstance(data, str):
            try:
                json.loads(data)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(data)
            except json.JSONDecodeError:
                raise ValueError("Provided string is not a valid JSON.")
        else:
            raise TypeError("Provided data is neither a dict nor a string.")
