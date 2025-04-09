# Webtoon Info Scraper

## Overview:
This Python project scrapes detailed information from the [Webtoons Originals page](https://www.webtoons.com/en/originals). It collects data like the webtoon's title, author, genre, update schedule, views, rating, age rating, and more. The data is stored in a CSV file for easy access and further analysis, such as building a recommendation system.

## Features:
Extracts all available webtoon links from the Originals page
Visits each individual webtoon page and collects detailed information, including:
- Title – The name of the comic
- Author – Creator(s) of the webtoon
- Genre – The category or theme of the comic
- Update Schedule – When new episodes are released
- Views – Total number of views
- Subscribers – Number of users following the comic
- Rating – Average reader rating
- Age Rating – Suitable audience age group
- Status/Note – Any special notes (e.g., paywall or content status)
Saves all collected data into a structured CSV file named [webtoons_details.csv](./webtoons_details.csv) for easy access and analysis.

## Requirements
- Python 3.x
- requests
- beautifulsoup4
You can install the required libraries using:
```bash
pip install requests beautifulsoup4
```

## Script:
You can find the full scraping script in the file:
[webtoons_scraper.py](./webtoons_scraper).

This Script:
- Fetches the Webtoons Originals main page
- Extracts links to each webtoon
- Visits each page and extracts detailed info
- Writes everything to a CSV file
- Includes a time.sleep(1) delay between requests to prevent overloading Webtoons servers
**Note**: Web page structures can change, so CSS selectors may need to be updated periodically.
  
## Output: 
The script will create a CSV file named webtoons_detailed.csv with the following columns:
- Title
- Author
- Genre
- Link
- Updates
- Views
- Subscribers
- Rating
- Age Rating
- Status

## Future Improvements:
- Clean and normalize the data using SQL (MySQL Workbench)
- Build a content-based recommendation system using this data

