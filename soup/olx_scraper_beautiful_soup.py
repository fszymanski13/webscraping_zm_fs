#Import necessary libraries

from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import time

# Set the boolean parameter to limit the number of pages
limit_links = True  

# Set the start_time to the actual time
start_time = time.time()

# Generate urls to scrape the links from

urls = ["https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/"] + [f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={page}" for page in range(2, 24)]

# Initialize an empty list
extracted_links = []  

# For all url in urls list scrape all the links to the advertisment
for url in urls:
    response = request.urlopen(url)
    soup = BS(response.read(), "html.parser")

    # Find all links under tag 'a' of class 'css-rc5s2u' 
    links = soup.find_all("a", {"class": "css-rc5s2u"})

    # Extract only links that are not from external site (i.e 'www.otodom.pl' -> these links start with 'https:' as the entire link is included)
    # Concatenate the desired links with 'https://www.olx.pl/' to create list of full links
    extracted_links.extend(['https://www.olx.pl/' + link["href"] for link in links if not link["href"].startswith('https:')])

if limit_links: 
    extracted_links = extracted_links[0:101]


# save extracted links to the csv file
df = pd.DataFrame({'Links': extracted_links})
df.to_csv('houses_links_bs.csv', index=False)

# Check the total time of scraping links
links_time = time.time() - start_time
print("Time taken for extracting links and saving them to csv:", links_time)

# Import all the links and save them as 'links' variable (here we could actually do not import the csv but simply use the 'extracted links')
links = pd.read_csv('houses_links_bs.csv')


# Create an empty DataFrame to store scraped data from a website
# Each column represents a specific piece of information about a property listing
scraped_data = pd.DataFrame({
    'Type': [],                  # Type of the property (e.g., apartment, house, etc.)
    'Price': [],                 # Total price of the property
    'Price per m2': [],          # Price per square meter of the property
    'Floor': [],                 # Floor number of the property
    'Furnishing': [],            # Furnishing status of the property
    'Market': [],                # Market status of the property (e.g. aftermarket, new, ect.)
    'Type of building': [],      # Type of building (e.g., block, tenement, ect.)
    'Area': [],                  # Area of the property in square meters
    'Number of rooms': []        # Number of rooms in the property
})

# For all links in 'links' extract the desired informations
for link in links['Links']:
    response = request.urlopen(link)
    soup = BS(response.read(), 'html.parser')

    # Try-except statement to handle potential exceptions or errors that may occur during the execution
    try:
        price = soup.find('h3', {'class':'css-ddweki er34gjf0'}).get_text()
    except:
        price = ''

    try:
        type = soup.find('ul', {'class':'css-sfcl1s'}).li.p.span.get_text()
    except:
        type = ''

    try:
        price_m2 = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.p.get_text()
    except:
        price_m2 = ''

    try:
        floor = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.p.get_text()
    except:
        floor = ''

    try:
        furnishing = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.next_sibling.p.get_text()
    except:
        furnishing = ''

    try:
        market = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.next_sibling.next_sibling.p.get_text()
    except:
        market = ''

    try:
        building = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.get_text()
    except:
        building = ''

    try:
        area = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.get_text()
    except:
        area = ''

    try:
        rooms = soup.find('ul', {'class':'css-sfcl1s'}).li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.get_text()
    except:
        rooms = ''

    # Create a dictionary 'house_data' with the scraped data for the current link
    house_data = { 'Price': price,'Type': type, 'Price per m2': price_m2, 'Floor': floor, 'Furnishing': furnishing,
                  'Market': market, 'Type of building': building, 'Area': area, 'Number of rooms': rooms}

    # Append the scraped data to the DataFrame 'scraped_data'
    scraped_data = scraped_data.append(house_data, ignore_index=True)
    
# Print the resulting DataFrame
print(scraped_data)

# Save the results to the csv 'house_data_bs.csv'
scraped_data.to_csv('house_data_bs.csv', index=False)

# Check the total time of scraping data of houses
scraped_data_time = time.time() - start_time
print("Time taken for scraping house data:", scraped_data_time)

# Check the total time of executuon of the program
total_time = time.time() - start_time
print("Total execution time:", total_time)

scraped_data.head()