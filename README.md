Last Updated: 04/10/2022


**DISCLAIMER:** If someone else that's not the professor or TA sees this, this is a beginner
Python project! If there's anything we can improve, let us know!

# PART ONE: What is This?
The purpose of this program is to fetch a random pin from the search results of one or more search queries.



# PART TWO: Prerequisites and Things to Keep in Mind

**YOU WILL NEED:**
* Python
* BeautifulSoup
* Google Chrome
* Selenium

**How to Download BeautifulSoup (once Python has been installed):**

!! DOUBLE CHECK IF PIP IS PROPERLY INSTALLED FIRST !!

WINDOWS: "pip install beautifulsoup4" / "python3 -m pip install beautifulsoup4"
MAC OS: "pip3 install beautifulsoup4"
LINUX: "pip install beautifulsoup4"

***Any error with any semblance of "node connection" should be ignored, as it's an error with the webdriver, not the code. If there's
an output with a Pinterest link directly below it, you're good.***

***If there is no link output, then Pinterest changed their HTML. Please send a pull request if this is the case.***

**How to Download Selenium (once Python has been installed):**
!! DOUBLE CHECK IF PIP IS PROPERLY INSTALLED FIRST !!

WINDOWS: "pip install selenium" / "python3 -m pip install selenium"
MAC OS: "pip3 install selenium"
LINUX: "pip install selenium"

Any errors encountered related to Python not being able to find the Selenium module requires you to double check if Selenium is downloaded to the correct path/directory (if you have multiple versions of Python on your computer).




# PART THREE: The Good Stuff

1) Choose browser of your choice. *For Safari, please refer to this tutorial on how to enable the in-browser webdriver. There is no separate webdriver file
for Safari like Chrome or Firefox: https://www.browserstack.com/guide/run-selenium-tests-on-safari-using-safaridriver*
2) Edit "searchQueries.csv" in your program of choice to your desired search query. ONE ROW = ONE SEARCH QUERY
3) Open up the command terminal.

WINDOWS / LINUX:

4) Type "cd [DIRECTORY YOU DOWNLOADED THE CODE IN]".
5) Type "cd pinterestpingenerator".

6) Type "randompin.py".

MAC:

4) Type "python [PATH TO THE DIRECTORY YOU DOWNLOADED THE CODE IN]".
5) Type "python randompin.py".

6) Copy and paste the link output into your browser of choice.
    6a) **IF YOU PUT IN MULTIPLE SEARCH QUERIES**, the program will just run twice. 





# PART FOUR: Credits

Majority of the code is from The Hippie Hacker's Pinterest recipe scraper. Thank you!

LINK: https://youtu.be/Y7VSjHgd76c
