# bond-controller
![](/assets/Bond-Controller.png)

這是一個可以控制 bond-agent 的專案
This is a project that can control the bond-agent.

## 注意事項
* Python 使用至少 3.11.0 以上
  * 推薦使用 standalone-python
    * Windows
      * x64
        * https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip
      * x86
        * https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-win32.zip
    * Linux
      * https://github.com/25077667/standalone-python
* 此專案在 windows 環境中將強制使用 administrator 權限

## Important Notes
* Python 3.11.0 or higher is required.
  * Recommended to use standalone-python
    * Windows
      * x64
        * https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-amd64.zip
      * x86
        * https://www.python.org/ftp/python/3.11.9/python-3.11.9-embed-win32.zip
    * Linux
      * https://github.com/25077667/standalone-python
* This project will enforce administrator privileges in a Windows environment.

## 如何安裝

* Clone 專案
  
* 使用虛擬環境
  * virtualenv
  
    ```shell
    virtualenv .env
    .env\Scripts\activate
    pip install -r ./requirements.txt
    ```

  * poetry

    ```shell
    poetry shell
    poetry install
    ```

## Installation
* Clone the project
* Use a virtual environment

  * virtualenv

    ```shell
    virtualenv .env
    .env\Scripts\activate
    pip install -r ./requirements.txt
    ```

  * poetry

    ```shell
    poetry shell
    poetry install
    ```


## 如何使用

詳細用法可參考 example.py

```shell
python example.py
```

## Usage

For detailed usage, refer to example.py

```shell
python example.py
```

# License / 授權條款

任何從連結下載的代碼，遵循原始專案的授權條款。
其他部分依據 [GPL-3 授權條款](/LICENSE)。

Any codes were downloaded from links, follow the license of the original project.
Others are under [GPL-3 License](/LICENSE).

# Disclaimer / 免責聲明

本項目是提供給測試人員使用的工具，不是用來進行非法行為的工具。使用者若用於其他用途，需自行承擔風險。
對於使用本項目所造成的任何損害或損失，作者不承擔任何責任。

This project is provided as a tool for testing purposes only and is not intended for illegal activities. Users assume full responsibility for any other uses. The authors are not liable for any damage or loss caused by the use of this project.
