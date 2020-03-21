from bs4 import BeautifulSoup
from random import choice
import re
import requests
import json

mood_list = ['nihilism', 'sad', 'heartbreak', 'death', 'fear', 'time', 'change', 'reflection', 'hope']

def how_you_feelin(mood):
    """scrape the goodreads quote page for the mood submitted"""

    to_scrape = "https://www.goodreads.com/quotes/tag?utf8=✓&id=" + mood
    scraped = requests.get(to_scrape)
    soup = BeautifulSoup(scraped.content, 'html.parser')
    cleaned = soup.prettify()
    quote_mess = soup.find_all(class_='quoteText')

    return quote_mess

def summon_text(quote_mess):
    """create vat of pureed soup from the lumpy chowdery soup"""

    # clean up to get an individual quote out of the poorly formatted soup
    # goodreads does not format their webpages in a way that is scraping-friendly
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
    # without this step, we would end up with random punctuation and unreliable chaining
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
            # just checking if we have a first person word or not
            if word != 'I' or word[:2] != "I'":
                word_list.append(word.lower())
            else:
                word_list.append(word)

    return word_list


def make_chains(word_list):
    """okay let's make this magic happen"""

    chains = {}
    for index in range(0, len(word_list) - 2):
        # only making small chains because I like maximum absurdity
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


def retrieve_an_catto():
    """get a randomized cat picture from the cat api"""

    response = requests.get('https://api.thecatapi.com/v1/images/search')
    response_json = json.loads(response.text)
    catto_url = response_json[0]['url']

    return catto_url

def mr_sandman(mood):
    """mr sandman bring me a dream, send me a nihilistic cat with ennui"""

    quote_mess = how_you_feelin(mood)
    a_short_novel_emotional_text = make_text(make_chains(summon_text(quote_mess)))
    print(a_short_novel_emotional_text)
    print('your catto is at: ', retrieve_an_catto())


print('Hello and welcome to CHONKSPIRATION, a service to inspire you with CATTOS and SAD FEELINGS')
print('Would you like to receive a darkly humorous catto? [Y/N]')
response = input('>>> ')
if response[0].lower() == 'y':
    print('Cats have limited emotions. Here is the current range: ', mood_list)
    print('What emotion would you like to experience?')
    mood = input('>>> ')
    print('Very good. Summoning your catto...')
    print('...')
    print('...')
    print('...')
    mr_sandman(mood)
else:
    print('Well fine then! Good day sir, I SAID good day sir!')
    quit()
