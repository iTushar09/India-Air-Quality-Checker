# India Air Quality Checker

A simple Flask web application that allows users to check the Air Quality Index (AQI) of various Indian cities. It utilizes the OpenWeatherMap API to fetch real-time air pollution data.

---

## Features

* **City-wise AQI Search:** Easily search for the Air Quality Index of specific Indian cities.
* **Detailed AQI Information:** Displays the AQI value along with its corresponding category (e.g., Good, Moderate, Poor) and a color-coded indicator for quick understanding.
* **Robust Error Handling:** Provides user-friendly messages for invalid city names, API issues, or network problems.
* **Simple & Clean Interface:** A straightforward user interface built with HTML.

---

## Requirements

Before you begin, ensure you have the following installed:

* Python 3.7+

---

## Setup & Installation

Follow these steps to get the project up and running on your local machine:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/iTushar09/India-Air-Quality-Checker.git](https://github.com/iTushar09/India-Air-Quality-Checker.git)
    cd India-Air-Quality-Checker # Or 'cd mymqtt' if your local folder is named that
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Get an OpenWeatherMap API Key:**
    * Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/).
    * Navigate to the "API keys" tab on your account page to find or generate your API key.

5.  **Set your API key in the application:**
    * Open `ap.py` in your project.
    * Locate the line where the `api_key` is defined and replace `"YOUR_API_KEY"` with your actual OpenWeatherMap API key:

    ```python
    api_key = "YOUR_API_KEY" # Replace with your actual key
    ```

---

## Running the app locally

1.  **Ensure your virtual environment is active.**
2.  **Run the Flask application:**

    ```bash
    python ap.py
    ```

3.  **Open your web browser** and navigate to `http://127.0.0.1:5000` to access the application.

---

## Deployment

You can deploy this Flask application to various platforms such as Heroku, PythonAnywhere, Google Cloud Run, or others that support Flask applications. Remember to configure your API key as an environment variable in a production environment for security.

---

## Project Structure
