from bs4 import BeautifulSoup
import urllib.request

#edikte
# tutorial: https://oxylabs.io/blog/python-web-scraping 
# Homelink: https://edikte.justiz.gv.at/edikte/edikthome.nsf
# Versteigerungen: https://edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suche!OpenForm&subf=vex
# javascript -> webscraping selenium

# List with google queries I want to make
desired_google_queries = ['tree' , 'men', 'yvou', 'should', 'load', 'from']

for query in desired_google_queries:
    # Constracting http query
    url = 'http://google.com/search?client=firefox-b-d&q=' + query
    # For avoid 403-error using User-Agent
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    # Parsing response
    soup = BeautifulSoup(html, 'html.parser')
    # Extracting number of results
    resultStats = soup.find(id="resultStats")
    print(resultStats)
  
    