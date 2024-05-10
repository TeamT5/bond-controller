import requests

from controller.common.logger.info_logger_handle import Logger


class ResponseMethod:
    @staticmethod
    def __get_headers_and_logger(response: requests.Session) -> dict:
        """
        Get headers from response and log it.

        :param response: [requests.Session] 回應資料的物件
        :return: [dict] 回應資料的 headers 資料
        """
        headers = response.headers

        Logger.info(headers)
        response.raise_for_status()

        return headers

    @staticmethod
    def __get_text_and_logger(response: requests.Session) -> str:
        """
        Get text from response and log it.

        :param response: [requests.Session] 回應資料的物件
        :return: [str] 回應資料的文字內容
        """
        text = response.text
        Logger.info(text)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # 處理請求失敗的情況
            print("HTTP請求錯誤:", e)
        except requests.exceptions.RequestException as e:
            # 處理其他請求相關的異常
            print("請求錯誤:", e)

        return text

    @staticmethod
    def __get_content_and_logger(response: requests.Session) -> str:
        """
        Get content from response and log it.

        :param response: [requests.Session] 回應資料的物件
        :return: [str] 回應資料的內容
        """
        content = response.content

        Logger.info(content)
        response.raise_for_status()

        return content

    @staticmethod
    def __get_json_and_logger(response: requests.Session) -> dict:
        """
        Get json from response and log it.

        :param response: [requests.Session] 回應資料的物件
        :return: [str] 回應資料的 json 內容
        """
        json = response.json()

        Logger.info(json)
        response.raise_for_status()

        return json

    @staticmethod
    def __get(url: requests.Session, *args, **kwargs) -> requests.Session:
        """
        Get response from url.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [requests.Session] 回應資料的物件
        """
        return requests.get(url, *args, **kwargs)

    @staticmethod
    def __post(url: requests.Session, *args, **kwargs) -> requests.Session:
        """
        Post response to url.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return:  [requests.Session] 回應資料的物件
        """
        return requests.post(url, *args, **kwargs)

    @classmethod
    def get_response(cls, url: requests.Session, *args, **kwargs) -> requests.Session:
        """
        Get response from url.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return:  [requests.Session] 回應資料的物件
        """
        response = cls.__get(url, *args, **kwargs)
        response.raise_for_status()

        return response

    @classmethod
    def post_response(cls, url: requests.Session, *args, **kwargs) -> requests.Session:
        """
        Post response to url.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return:  [requests.Session] 回應資料的物件
        """
        response = cls.__post(url, *args, **kwargs)
        response.raise_for_status()

        return response

    @classmethod
    def get_header(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get headers from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的 headers 資料
        """
        return cls.__get_headers_and_logger(cls.__get(url, *args, **kwargs))

    @classmethod
    def post_header(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get post headers from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的 headers 資料
        """
        return cls.__get_headers_and_logger(cls.__post(url, *args, **kwargs))

    @classmethod
    def get_text(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get text from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的文字內容
        """
        return cls.__get_text_and_logger(cls.__get(url, *args, **kwargs))

    @classmethod
    def post_content(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get post content from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的內容
        """
        return cls.__get_content_and_logger(cls.__post(url, *args, **kwargs))

    @classmethod
    def get_content(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get content from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的內容
        """
        return cls.__get_content_and_logger(cls.__get(url, *args, **kwargs))

    @classmethod
    def post_text(cls, url: requests.Session, *args, **kwargs) -> str:
        """
        Get post text from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [str] 回應資料的文字內容
        """
        return cls.__get_text_and_logger(cls.__post(url, *args, **kwargs))

    @classmethod
    def get_json(cls, url: requests.Session, *args, **kwargs) -> dict:
        """
        Get json from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [dict] 回應資料的 Json 內容
        """
        return cls.__get_json_and_logger(cls.__get(url, *args, **kwargs))

    @classmethod
    def post_json(cls, url: requests.Session, *args, **kwargs) -> dict:
        """
        Get post json from response and log it.

        :param url: [requests.Session] 請求的網址
        :param args: [all] args
        :param kwargs: [all] kwargs
        :return: [dict] 回應資料的 Json 內容
        """
        return cls.__get_json_and_logger(cls.__post(url, *args, **kwargs))
