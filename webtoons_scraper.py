import requests
from bs4 import BeautifulSoup
import re
import csv
import time

# Step 1: Load the collected links from the previous step
url = "https://www.webtoons.com/en/originals"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Extract links from the Originals page
links = []
webtoon_links = soup.find_all('a', class_="daily_card_item")

for webtoon in webtoon_links:
    link = webtoon.get("href")
    if link:
        links.append(link)

print(f"Number of links extracted: {len(links)}")

# Step 2: Function to extract data from individual webtoon pages
def extract_webtoon_data(link):
    try:
        response = requests.get(link)
        if response.status_code != 200:
            print(f"Failed to access {link}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title_tag = soup.find('h1', class_="subj")
        title = title_tag.get_text().strip() if title_tag else "N/A"

        # Extract author (multiple possible class names)
        author = "N/A"
        author_tag = soup.find('h3', class_="title")
        if author_tag:
            author = author_tag.get_text().strip()

        # Extract genre
        genre = "N/A"
        genre_tag = soup.find('h2', class_=re.compile(r'genre'))
        if genre_tag:
            genre = genre_tag.get_text().strip()

        # Extract age rating
        age_rating = "N/A"
        age = soup.find('p', class_= "age_text")
        if age:
            age_rating = age.get_text().strip() 

        # Extract when Updated
        updates = "N/A"
        update_tag = soup.find('p', class_="day_info")
        if update_tag:
            updates = update_tag.get_text().strip()

        # Extract views, subscribers, and rating
        views = "N/A"
        subscribers = "N/A"
        rating = "N/A"
        stats = soup.find_all('li')

        for stat in stats:
            # Check for views
            label = stat.find('span')
            value = stat.find('em', class_="cnt")

            if label and value:
                label_text = label.get_text().strip()
                if "view" in label_text.lower():
                    views = value.get_text().strip()
                elif "subscribe" in label_text.lower():
                    subscribers = value.get_text().strip()
                elif "grade" in label_text.lower():
                    rating = value.get_text().strip()

            # Note
            status = "N/A"
            author_note = soup.find('div', class_="detail_paywall")
            if author_note:
                # Remove the <span class="ico_note"> and extract the rest of the text
                span_tag = author_note.find('span', class_="ico_note")
                if span_tag:
                    span_tag.extract()  # Remove "NOTE" span
                status = author_note.get_text(strip=True)



        print(f"Title: {title}, Author: {author}, Genre: {genre}, Updates: {updates}, Views: {views}, Subscribers: {subscribers}, Rating: {rating}, Age Rating: {age_rating}, Status: {status}")

        return [title, author, genre, link, updates, views, subscribers, rating, age_rating, status]
    
    except Exception as e:
        print(f"Error processing {link}: {e}")
        return None

# Step 3: Scrape data from each link and store in a CSV
webtoons_data = []

for link in links:  
    data = extract_webtoon_data(link)
    if data:
        webtoons_data.append(data)
    time.sleep(1)  # Pause to avoid getting blocked

# Step 4: Save to CSV
with open("webtoons_detailed.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Genre", "Link", "Updates", "Views", "Subscribers", "Rating", "Age Rating", "Status"])
    writer.writerows(webtoons_data)

print("Webtoons detailed data saved to webtoons_detailed.csv")
