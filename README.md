# bond-controller

這是一個可以控制 bond-agent 的專案
This is a project that can control the bond-agent.

## 注意事項
* Python 使用至少 3.8.0 以上
  * 推薦使用 standalone-python
    * https://github.com/25077667/standalone-python
* 此專案需先行運作 bond-agent

## Important Notes
* Python version should be at least 3.8.0
  * Recommended to use standalone-python
    * https://github.com/25077667/standalone-python
* The bond-agent must be running before using this project

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