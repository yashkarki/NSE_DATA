# Stock Yaari Assignment

This project provides an API to fetch historical stock index data within a specified range. The API allows you to filter the data based on various criteria such as index name, date range, and specific price ranges.

## Project URL
[Stock Yaari Assignment](https://yashkarki.pythonanywhere.com/)

## Stock API URL (POST Request)
[Stock API Endpoint](https://yashkarki.pythonanywhere.com/api/stock_index)

### Request: POST
Payload:
```json
{
    "index_name": "NIFTY_50",
    "start_date": "2023-04-05",
    "end_date": "2024-02-01",
    "open_lowest": 19750,
    "open_highest": 21000,
    "high_lowest": 19850,
    "high_highest": 22000,
    "low_lowest": 18000,
    "low_highest": 20000,
    "close_lowest": 19900,
    "close_highest": 23000,
    "shares_traded_lowest": 203559874,
    "shares_traded_highest": 352810261,
    "turnover_lowest": 19659.17,
    "turnover_highest": 30069.78
}

Response:{
    "start-date": "2023-04-05",
    "end-date": "2024-02-01",
    "data": [
        {
            "id": 114,
            "date": "2023-07-19",
            "open_price": 19802.95,
            "high_price": 19851.7,
            "low_price": 19727.45,
            "close_price": 19833.15,
            "shares_traded": 259660464,
            "turnover": 26447.9,
            "index": 1
        },
        ...
    ],
    "pagination": {
        "page": 1,
        "total_pages": 9,
        "total_rows": 216
    },
    "ranges": {
        "open": {
            "lowest": 19750,
            "highest": 21000
        },
        "high": {
            "lowest": 19850,
            "highest": 22000
        },
        "low": {
            "lowest": 18000,
            "highest": 20000
        },
        "close": {
            "lowest": 19900,
            "highest": 23000
        },
        "shares_traded": {
            "lowest": 203559874,
            "highest": 352810261
        },
        "turnover": {
            "lowest": 19659.17,
            "highest": 30069.78
        }
    }
}

## To Run Project Locally

### Navigate to NSE_DATA directory
```bash
cd NSE_DATA


### To create virtual environment 
python3 -m venv .venv

### To activate virtual environment
. .venv/bin/activate

### To install the modules
pip3 install -r requirements.txt

### To import data on models from csv file 
python3 manage.py getdata
