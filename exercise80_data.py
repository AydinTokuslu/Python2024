# Create a code that extracts data from a website. You will extract a
# table from the website. And from that table you will extract columns
# about the data types in Python and their mutability. You will extract
# information from the following website:

# https://en.wikipedia.org/wiki/Python_(programming_language)

# The following table (next page) is what you will extract from the website.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


# Sending an HTTP request to fetch the content of the page
response = requests.get(url)

# If the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the relevant data (you might need to inspect the HTML structure for this)
    # For the specific table you mentioned (Python's data types and their mutability)
    table = soup.find('table', {'class': 'wikitable'})

    # Extracting all rows in the table
    rows = table.find_all('tr')

    # Create a list to store the data
    table_data = []

    # Loop through each row and extract the columns (cells)
    for row in rows[1:]:  # Skipping the header row
        cols = row.find_all('td')
        if len(cols) > 1:  # Ensure the row has the right number of columns
            data = {
                'Data Type': cols[0].get_text(strip=True),
                'Mutability': cols[1].get_text(strip=True),
                'Description': cols[2].get_text(strip=True),
            }
            table_data.append(data)

    # Convert the list of data into a DataFrame (table)
    df = pd.DataFrame(table_data)

    with open("wikipedia.csv", mode='a', encoding="utf-8") as file:
        #file.write(df)
        file.writelines(df+" "+"\n")
        # mail_list.append(file)
        # print(mail_list)
        file.close()

    # Display the DataFrame
    print(df)

    with open("wikipedia.csv", mode='r', encoding="utf-8") as file:
        files = file.read().split()
        for i in files:
            print(i)
        file.close()

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)