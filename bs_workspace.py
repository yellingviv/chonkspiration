from bs4 import BeautifulSoup
import re

scraped = open('nihilism.html')

soup = BeautifulSoup(scraped, 'html.parser')
cleaned = soup.prettify()

# this is the class <div class="quoteText">
# use soup.find_all(class_="") to search by CSS class

quote_mess = soup.find_all(class_='quoteText')

quotes = []
for quote in quote_mess:
    to_trim = str(quote)
    trimmed = to_trim[30:]
    this_quote = ''
    for char in trimmed:
        if char == '<':
            break
        else:
            this_quote = this_quote + char
    quotes.append(this_quote)

word_list = []
for quote in quotes:
    purged = quote.replace("\n", '')
    clean_word = ''
    for char in quote:
        if char


cleaned_up = re.sub(r'(\.|,|:|;|\?|!)', '', cleanest)
