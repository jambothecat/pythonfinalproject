# Things to improve/fix (in order of importance):

# - Code to account for Pinterest's everchanging HTML. The attribute that holds separate
#  pin results (so as of 04/10/2022, it's "Yl- MIw Hb7", but the attribute was named something else in the tutorial I watched.
# The tutorial was made sometime in 2021) always changes as well. If there is no output, that means the HTML
# was changed (unfortunately).
# I think you can imagine how annoying it'd be to have to go into the code, and change it every time
# in order to keep up with Pinterest. My method to finding the updated attribute, as a beginner programmer, was to just compare
# the old HTML in the video I watched, and see what lined up. I've noticed they don't *drastically* change it, they just change
# attribute names.

# - Make different versions for different web browsers available! I think it's as easy
# as just including different folders with different copies of the code and their respective webdrivers. For now,
# I'll just keep it with Chrome and Firefox.

from selenium import webdriver
from selenium.webdriver.support import ui
from bs4 import BeautifulSoup, SoupStrainer 
import csv
import random
import time


BASE_URL = "https://pinterest.com"

class RandomPinGenerator: 
    
    def getPins(self, url, pick):
 
        browser = webdriver.Firefox() # Changing "Chrome" to "Firefox" changes the browser used.
        browser.get(url) 

        html_doc = browser.page_source 
        soup = BeautifulSoup(html_doc, 'html.parser')

        deliciousSoup = soup.prettify() # Makes the HTML easier to read.

        pinUrl = BASE_URL + url


        # pins = soup.find_all("img", {"class","GrowthUnauthPinImage__Image"})
        # Ignore this, this just gives the actual links to the images which I thought could be used for future reference.


        pins = soup.find_all("div", {"class", "Yl- MIw Hb7"})
        
        # print(pins)-> debug

        # This is where original code starts. EVERYTHING ELSE ISN'T MINE AND
        # IS TAKEN FROM "THE HIPPIE HACKER": https://youtu.be/Y7VSjHgd76c
        index = 0
        results = []
        numbers = "0123456789"
        pinLink = ""

        for link in soup.find_all('a'):
            pin = link.get('href')
            for num in numbers:
                if num in pin:
                    results.append(pin)


        random.shuffle(results)

        # print(results) -> debug
        randomPin = str(random.choice(results))

        for chara in randomPin:
            pinLink = pinLink + chara

        finalPin = BASE_URL + pinLink

        # This is where the original code ends.
        
        time.sleep(5)
        browser.close() # Closes the browser after done using.
        
        return print("Here's your random pin:", finalPin) # This output is not in the original code.

    def getSearchParameters(self):
        searchParameters = []
        with open('searchQueries.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                searchParameters.append(row[0].replace(" ", "%20"))
        return searchParameters

    def run(self):

        parameters = self.getSearchParameters()

        for query in parameters: 
            searchUrl = BASE_URL + "/search/pins/?q=" + query

            # gets pin list with url (first argument) and amnt of links to give back (second argument)
            pinList = self.getPins(searchUrl, 1) 

        return self

# Executes the program!
if __name__ == '__main__':
    randomPin = RandomPinGenerator()
    randomPin.run()
