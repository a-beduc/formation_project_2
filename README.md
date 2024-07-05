# formation-project-2_BooksToScrape-DataExtractor

Second project for the online course of Python application development on OpenClassroom.

## Description

This project extracts data from the website: [books.toscrape.com](https://books.toscrape.com/index.html).
It creates a .csv file per category of books containing the following information:

- product_page_url
- universal_product_code
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

As an option, the extractor allows you to download images of the book covers and store them in an appropriate directory.

## Installation

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)

### Steps to Install

1. Clone the project or download the files to your local machine.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the DataExtractor

1. From the terminal, navigate to the project directory.
2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. Execute the script:
    ```bash
    python main.py
    ```