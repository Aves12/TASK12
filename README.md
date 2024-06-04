## Question 1: Design an Image Server

## Assumptions

We have access to a list of restaurants in Mumbai with their menu images available online.
The menu images are in a format that can be easily processed by an OCR (Optical Character Recognition) tool.
We have a database system set up to store the extracted menu items and prices.

## Reason behind assumptions:

We need a list of restaurants to scrape their menu images, which is a reasonable assumption given the scope of the project.
Most menu images are in a format that can be processed by OCR tools, such as JPEG or PNG.
We need a database to store the extracted data, which is a common practice in data storage and retrieval.

## Design:

Image Scraper: Use a web scraping library like BeautifulSoup (Python) or Scrapy (Python) to scrape menu images from restaurant websites or online platforms like Zomato or Swiggy.
OCR Tool: Use an OCR tool like Tesseract (Python) or Google Cloud Vision API to extract text from the menu images.
Data Processing: Write a script to process the extracted text, separating menu items and prices.
Database Storage: Store the extracted data in a database system like MySQL or MongoDB.
