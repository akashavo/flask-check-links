# First ver from ChatGPT + minimal app from https://render.com/docs/deploy-flask
# Apr-May 2023
# Author/updates: AS

from flask import Flask
app = Flask(__name__)

import requests
import bs4 as bs
# from bs4 import BeautifulSoup

# FUNCTION 
# Will check if "check_url" is one of the 'a' links in the list 'links'
# Will return True or False.
def is_link_in_url (links, check_url) : #{

   # Loop through each link and check if it contains the specified domain
   link_found = False
   for link in links:
      if check_url in link.get('href'):
         link_found = True
         return True

   if not link_found:
      return False
  
#}

@app.route('/check_links')
def check_links(): #{
    # Define the URLs to scrape
    # This is a list of URL+Backlinks pairs to be checked, called url_backlink_pairs - JUST KEEP ADDING PAIRS TO THE LIST:
    url_backlink_pairs = [("https://www.womendailymagazine.com/losing-weight-peptides/", "https://corepeptides.com/peptides/cjc-1295-ipamorelin-10mg-blend/"), 
                   ("https://amirarticles.com/tips-to-gain-weight/", "corepeptides.com/peptides/cjc-1295-ipamorelin-10mg-blend/"), 
                   ("https://artdaily.com/news/121869/The-best-mass-taking-cycles-with-dianabol", "https://corepeptides.com/peptides/ghrp-6-10mg/")]

    for url, backlink in url_backlink_pairs: #{
        # print(f"{backlink}: {url}")

        # Make a GET request to the URL and store the response in a variable
        response = requests.get(url)

        # get and display the server response code
        print("URL: ", url, "Status Code: ", response.status_code)

        # Use Beautiful Soup to parse the HTML content of the response
        soup = bs.BeautifulSoup(response.content, 'html.parser')

        # To Print the title of webpage ::  print(soup.title.string)

        # Find all links on the webpage
        links = soup.find_all('a')

        # CALL Function to check for Backlink:
        # backlink = 'https://corepeptides.com/peptides/cjc-1295-ipamorelin-10mg-blend/'

        if is_link_in_url(links, backlink) :
            print('Found a link to: ', backlink, ' on page: ', url)
        else :
            print('Backlink NOT found on: ', url)

    #}

#}

# TO DOs:
# DONE - get Server_return_code
# - Create DB tables
# - write run results to DB table
