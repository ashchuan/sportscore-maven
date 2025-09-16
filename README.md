# Live Cricket Scores

This is a simple Python Flask application that displays live cricket scores by fetching data from an RSS feed.

## Features

*   Fetches live cricket scores from [ESPN Cricinfo RSS feed](https://static.cricinfo.com/rss/livescores.xml).
*   Displays match titles, links, and descriptions in a user-friendly web interface.

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    # If this were a git repository
    # git clone <repository_url>
    # cd cricket-live-scores
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install Flask feedparser requests
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Technologies Used

*   Python
*   Flask
*   feedparser
*   requests
*   HTML
*   CSS (via `index.html` - basic styling)
