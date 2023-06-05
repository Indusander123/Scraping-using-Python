import requests
from bs4 import BeautifulSoup

# Sending a GET request to website
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787" #Given website url
response = requests.get(url)

# Creating BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Finding the "Search Postings" heading
postingsHeading = soup.find('h2', text="Search Postings")

# Find the parent div containing the postings
postingsDiv = postingsHeading.find_next('div')

# Find all the postings within the div
postings = postingsDiv.find_all('div', class_='result_div')

# Extracting the desired fields from the postings
resultlist = []
for posting in postings[:5]:
    est_value_notes = posting.find('div', class_='est_value_notes').text.strip()
    description = posting.find('div', class_='description').text.strip()
    closing_date = posting.find('div', class_='closing_date').text.strip()

    resultlist.append({
        'Est. Value Notes': est_value_notes,
        'Description': description,
        'Closing Date': closing_date
    })

# Print the result
for i in resultlist:
    print(i)

