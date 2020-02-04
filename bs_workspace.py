from bs4 import BeautifulSoup
from random import choice
import re

scraped = open('nihilism.html')

soup = BeautifulSoup(scraped, 'html.parser')
cleaned = soup.prettify()
quote_mess = soup.find_all(class_='quoteText')

def summon_text(quote_mess):
    """create giant text blob from the soup"""

    # clean up to get an individual quote out of the poorly formatted soup
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

    # clean up the line breaks and unnecessary punctuation
    quote_list = []
    for quote in quotes:
        cleaned = quote.replace("\n", '')
        purged = re.sub(r'(\.|,|:|;|\(|\)|\"|\?|”|“|!)', '', cleaned)
        quote_list.append(purged)

    # create a final clean list of all the words available
    word_list = []
    for index in range(0, len(quote_list) - 1):
        quote = quote_list[index]
        words = quote.split(' ')
        for word in words:
            if word != 'I' or word[:2] != "I'":
                word_list.append(word.lower())
            else:
                word_list.append(word)

    return word_list


def make_chains(word_list):
    """okay let's make this magic happen"""

    chains = {}
    for index in range(0, len(word_list) - 2):
        key = tuple(word_list[index:index + 2])
        if key not in chains:
            chains[key] = [word_list[index + 2]]
        else:
            chains[key].append(word_list[index + 2])
    return chains


def make_text(chains):

    words = []
    key_block = choice(list(chains.keys()))

    for key in key_block:
        words.append(key)

    for index in range (0, 20):
        if key_block in chains:
            new_key = list(key_block[1:])
            new_random = choice(chains.get(key_block))
            new_key.append(new_random)
            words.append(new_random)
            key_block = tuple(new_key)
        else:
            break

    return " ".join(words)


a_short_novel_nihilist_text = make_text(make_chains(summon_text(quote_mess)))
print(a_short_novel_nihilist_text)
