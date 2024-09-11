# Orphex Case﻿

# Django API for Marketing Data Analysis

## Overview

This Django project provides an API for analyzing marketing data. The API includes endpoints for calculating conversion rates, summarizing status distributions, evaluating category and type performance, and aggregating data for conversion types.

(In the project, data is coming directly from the csv file. I didn't create a database model on purpose. Since it is just a file, access is provided from the csv file in order to use Numpy features directly. As a development idea, an input can be requested from the user and endpoints can work on this input loaded into the database.

## Demo

This project has been deployed at https://mbulut.pythonanywhere.com/swagger/. You can try endpoints directly from the Swagger documentation via the link.

## Project Setup

### Requirements

- Python 3.x
- Django
- Django REST Framework
- pandas

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/bulutMuhammet/orphex_case
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```
   
3. **Migrate:**
    
    A database model has not been created. In order to focus on using Pandas, the data was pulled directly from the csv file.
    ```bash
    python manage.py migrate
    ```

4. **Prepare the data:**

   Ensure that the `mockupinterviewdata.csv` file is placed in the `data/` directory. The file path should be updated if it's in a different location.


5. **Run the server:**
    
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. `/api/conversion-rate/`

**Method:** `GET`

**Description:** Returns the conversion rate for each `customer_id`, along with the highest and lowest conversion rates.

**Example Response:**

```json
{
  "highest_conversion_rate": "14.99703%",
  "lowest_conversion_rate": "0.00333%"
}
```

### 2. `/api/status-distribution/`

**Method:** `GET`

**Description:** Provides a summary of the distribution of status across different types and categories, including total revenue and conversions for each status.

**Example Response:**

```json
[
  {
    "type": "AWARENESS",
    "category": "ELECTRONICS",
    "statuses": {
      "statuses": {
        "ENABLED": {
          "total_revenue": 685217.41,
          "total_conversions": 2379
        },
        "HIDDEN": {
          "total_revenue": 460163.36,
          "total_conversions": 1403
        }
      }
    }
  },
  {
    "type": "AWARENESS",
    "category": "FASHION",
    "statuses": {
      "statuses": {
        "ENABLED": {
          "total_revenue": 502454.54,
          "total_conversions": 2008
        },
        "HIDDEN": {
          "total_revenue": 798898.87,
          "total_conversions": 3111
        }
      }
    }
  },
    ...
]
```

### 3. `/api/category-type-performance/`

**Method:** `GET`

**Description:**  Returns the total revenue and conversions grouped by category and type. Highlights the top-performing category and type combination.
**Example Response:**

```json
[
  {
    "type": "AWARENESS",
    "category": "ELECTRONICS",
    "total_revenue": 1145380.77,
    "total_conversions": 3782,
    "best_performance": false
  },
  {
    "type": "AWARENESS",
    "category": "FASHION",
    "total_revenue": 1301353.41,
    "total_conversions": 5119,
    "best_performance": false
  },
    ...
]
```

### 4. `/api/filtered-aggregation/`

**Method:** `GET`

**Description:**  Description: Exposes aggregated data for rows where the type is `CONVERSION`, returning the average revenue and conversions per `customer_id`.


**Example Response:**

```json
[
  {
    "customer_id": "Customer A",
    "avg_revenue": 26084.475208333333,
    "avg_conversions": 105.14583333333333
  },
  {
    "customer_id": "Customer B",
    "avg_revenue": 24771.766249999997,
    "avg_conversions": 112.19642857142857
  },
  {
    "customer_id": "Customer C",
    "avg_revenue": 24451.51895833333,
    "avg_conversions": 94.60416666666667
  }
]
```

## Project Structure

- `api/`
  - `data_loader.py` - Helper that loads csv data
  - `views.py` - API views
  - `urls.py` - URL routing
- `data/` 
  - `mockupinterviewdata.csv` - The dataset used for analysis
- `requirements.txt` - List of required Python packages
- `manage.py` - Django's command-line utility
