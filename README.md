# bond-controller

這是一個可以控制 bond-agent 的專案

## 注意事項
* Python 使用至少 3.8.0 以上
* 此專案需先行運作 bond-agent

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

## 如何使用

詳細用法可參考 example.py

```shell
python example.py
```