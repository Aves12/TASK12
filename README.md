Question 1: Design an Image Server
Assumptions
Image Sources: Restaurant websites or public directories provide menu images.
Reason: Most restaurants have their menus available online for customer convenience.
OCR Accuracy: OCR (Optical Character Recognition) technology will have a high success rate in reading text from images.
Reason: Modern OCR tools like Tesseract are highly accurate for clear images with standard fonts.
Database: A relational database like PostgreSQL is suitable for storing structured data (items and prices).
Reason: Relational databases are efficient for structured data and support complex queries.
System Design
Image Scraper: A web scraper to collect menu images from restaurant websites.
Tools: BeautifulSoup, Scrapy
Image Server: A server to receive, store, and serve images.
Framework: Flask or Django
OCR Processor: A service to process images and extract text using OCR.
Tool: Tesseract
Database: A relational database to store extracted items and prices.
Database: PostgreSQL
