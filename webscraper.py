import requests
from bs4 import BeautifulSoup 
import boilerpy3 
from boilerpy3 import extractors 
import csv
from io import StringIO
from html.parser import HTMLParser





url = "https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

#Parsing the title,content, updated time and byline that was requested from the website.
 
title1 = soup.find('h1'),  soup.select('h1')
title2 = soup.find('h2'), soup.select('h2')
updated_time = soup.find('time'), soup.select('time')
byline = soup.find('p.byline'), soup.select('p.byline')



def removing_tags(html, cleaned): 
	soup = BeautifulSoup(html, 'html.parser') # creates a new bs4 object from extracted html data 
	for script in soup (['style','script']):  # removes all javascript and stylesheet code 
		script.extract ()
		script.decompose()

		text = soup.get_text() # gets text 
		lines = (line.strip() for line in text.splitlines()) # breaks into lines and remove leading and trailing space on each line 
		chunks = (phrase.strip() for line in lines for phrase in line.split("")) # break multilines into individual lines for each 
		text = '\n'.join(chunk for chunk in chunks if chunk ) # drops blank lines 
		return text
		
cleaned = (title1,title2,updated_time) 

#the overal purpose of the function is to remove all html tags, scrip and style so that whatever data that is extracted is in text only, nothing else. 
 


extractor = extractors.ArticleExtractor()
content_extracted = extractor.get_content_from_url(url) # This boilerpy extractor extracts all the content from the website and only returns text exculding title,byline and updated time. 


extracted_data ={}

extracted_data =({
	'url' : url, 
	'title' : title1,
	'Content of Article' : content_extracted, 
	'Time written' : updated_time, 
	"byline of the Aricle" : byline 

})

def __init__(self,csv_writer) : 
	self.csv_writer = csv_writer


extraction_file = open('extracted.csv', mode = 'a', encoding = 'utf-8')

csv_writer = csv.writer(extraction_file, delimiter = ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL )
csv_writer.writerow([extracted_data])



		
