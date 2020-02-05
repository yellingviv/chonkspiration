from bs4 import BeautifulSoup
from random import choice
import re
import requests
import json

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

def retrieve_an_catto():
    """get a randomized cat picture from the cat api"""

    response = requests.get('https://api.thecatapi.com/v1/images/search')
    response_json = json.loads(response.text)
    catto_url = response_json[0]['url']

    return catto_url

def mr_sandman():
    """mr sandman bring me a dream a nihilistic cat with ennui"""

    print('your catto is at: ', retrieve_an_catto())
    a_short_novel_nihilist_text = make_text(make_chains(summon_text(quote_mess)))
    print(a_short_novel_nihilist_text)

print('Hello and welcome to CHONKSPIRATION, a service to inspire you with CATTOS and ENNUI')
print('Would you like to receive a nihilistic catto? [Y/N]')
response = input('>>> ')
if response[0].lower() == 'y':
    print('Very good. Summoning your catto...')
    print('...')
    print('...')
    print('...')
    mr_sandman()
else:
    print('Well find then! Good day sir, I SAID good day sir!')
    quit()

# for future reference/next steps:

set_of_all_chain_keys = {'', 'lost', 'cold', 'a', 'blackness', 'décédée', 'jobs', "ain't", 'apparent', 'consequence', 'drink', 'decadence', 'mizeria', 'looked', 'nihilistic', 'longer', 'him', 'interventions', 'little', 'drunk', 'nothingness', 'this', 'dire', 'in', 'observations', 'mysteries', 'reçu', 'peut-être', 'femee', 'set', 'fishing', 'natural', 'ripeness', 'je', 'people', 'children', 'foolish', 'ears', 'should', 'became', 'squandering', 'honorable', 'shadows', 'still', 'souls', 'hallway', 'facuta', 'ask', 'which', 'back', 'tomb', "that's", 'winter', 'pretensions', 'sea', 'sat', 'millionaires', 'window', 'domination', 'illusion', 'mask', 'and', 'out', 'what', 'argue', 'contrary', '–', 'surely', 'thought', 'mud', 'fat', 'men', 'matter', 'miraculous', 'personal', 'glistening', 'regret', 'bury', 'hazy', 'purpose', 'own', 'foremost', 'add', 'possible', 'dispassion', 'veut', 'man', 'deterioration', 'that’s', 'full', 'read', 'choice', 'hear', 'examining', "l'asile", 'strict', 'tried', 'ghoulishly', 'drop', 'endure', 'values', 'into', 'age', 'cross', 'meditate', 'difference', 'hidden', 'staring', 'fit', 'any', 'horror', 'withering', 'opponent', 'ou', '‘mercy’', 'disappear', 'feeling', 'same', 'or', 'can', 'abuse', 'less', 'traced', 'determine', 'found', "we've", 'grief', 'importance', 'wisdom', 'classes', 'suspect', 'imagine', 'want', 'at', 'he', 'blindly', 'nature', 'sound', 'death', 'said', 'actually', 'spend', 'orientation', 'must', 'way', 'squirming', 'deal', 'moralists', 'politics', 'sailing', 'pentru', 'justice', 'provenance', 'things', 'along', 'simplicity', 'movie', 'but', 'pass', 'ignominy', 'have', 'crede-o', 'say', 'four', 'mere', 'unknown', 'treasured', 'best', 'heart', 'no', 'opposing', 'who', 'suffer', 'insects', 'walk', 'his', 'lazy', "we're", 'achievement', 'think', 'here', 'whatever', 'academic', 'gods', 'extinguish', 'shit', 'ca', 'pooled', 'those', 'kind', 'ill-disposed', 'hitler’s', 'my', 'green', "i'll", 'real', 'house', 'worthy', 'alien', 'stinkingest', 'limitless', 'all', 'myops', 'wants', 'television', 'perhaps', 'necessity', '«', 'cat', 'virtue', 'pretended', 'piece', 'function', 'am', 'harm', 'stand', 'namely', 'once', 'almost', 'killing', 'last', 'certainly', 'know', 'you', 'ancient', 'powerful', 'christian', 'meeting', 'else', 'yami', 'sunt', 'happy', 'truth', 'cast', 'judges', 'usefulness', 'fire', 'numerous', 'darken', 'wrong', 'over', 'fear', "wouldn't", 'acoustic', 'generation', 'behavior', 'beneath', 'end', 'past', 'screamed', 'deus', 'afraid', 'upon', 'attention', 'meu', 'sense', 'settled', 'maintains', 'soon', 'universe', 'sky', 'grubs', 'myself', 'more', 'incurable', 'liked', 'god’s', 'years', 'suicide', 'the', 'practical', 'suspended', 'dead', 'waiting', 'absurdity', 'many', 'ignores', 'e', 'night', 'confusion', 'was', 'old', 'era', 'later', 'village', 'our', 'been', 'emptiness', 'illness', 'downtrodden', 'antiquity', 'these', 'particular', 'fall', 'before', 'one', 'most', 'discovers', 'account', 'soft', 'whatsoever', 'consequently', 'surrounded', 'will', 'autumn', 'listened', 'knowing', 'buy', 'see', 'handicap', 'disciples', 'hate', 'however', 'abstractions', 'latter', 'flux', 'hitherto', 'advertising', 'history', 'very', 'between', 'categories', 'burn', 'tunneling', 'beyond', 'himself', 'depression', 'pumping', 'is', 'sins', 'around', 'such', 'hours', 'hand', 'crimes', 'helpless', 'your', 'cannot', "won't", 'how', 'project', 'hint', 'look', "don't", 'portal', 'not', 'worthwhile', 'drawn', 'up', 'demain', 'by', 'stiff', 'arrived', 'heritage', 'war', 'positivist', 'believed', 'crucified', 'mastery', 'wanted', 'food', 'mental', 'we', 'writhing', 'claim', 'self-deception', 'suit', 'society', 'woman', 'form', 'good', 'lived', 'ourselves', 'enemy', 'raised', 'facut', 'another', 'didn’t', 'why', 'everything', 'others', 'doing', 'enigmatic', 'active', 'eu', 'gas', 'alibi', 'murderers', 'si', 'days', 'ceased', 'got', 'fact', 'kill', 'make', 'only', 'rien', 'accepted', 'lacking', 'successful', 'adores', 'collars', 'fragile', 'useful', 'go', 'refrain', 'contradicting', 'otherwise', 'lines', 'they', 'hungry', 'morning', 'affirm', 'circumstances', 'intense', 'mortal', 'seek', 'conceived', 'bit', 'imagined', 'chose', 'hier', 'smartest', 'club', 'de', 'fondul', "god's", 'time', 'transforming', 'noting', 'promoters', 'lack', 'life', 'disturb', 'liberals', 'she', 'perfect', 'primeval', 'none', 'enterrement', 'great', 'indifference', 'campus', 'breath', 'feel', 'mistrustful', 'orders', 'place', 'efficient', 'whose', 'ago', 'were', 'adults', 'speck', 'middle', 'that', 'sufletului', 'worries', 'slaves', 'naught', 'blot', 'likewise', "didn't", 'leaves', 'extremely', 'strongest', 'son', 'truly', 'spirit', 'told', 'trees', 'clothes', 'bids', 'chasing', 'simply', 'couch', 'blanket', 'had', 'crazy', "we'd", 'proof', 'nothing', 'alone', '»', 'stars', 'accepts', 'living', 'times', 'conceptual', 'obtain', 'inland', 'since', 'social', 'gratitude', 'everywhere', 'clinging', 'stay', 'enduring', 'pissed', 'to', 'really', 'from', 'come', 'tree', 'manipulation', 'weightier', 'two', 'logical', 'away', 'dropping', 'woke', 'outlived', 'spare', 'day', 'believes', 'smile', 'need', 'could', 'moment', 'even', 'suspecting', 'worse', 'mercy', 'of', 'recommendation', 'punishments', "things'", 'remains', 'each', 'goal', 'saw', 'o', 'present', 'decisive', 'arrives', 'on', 'stems', 'weeks', 'meaningless', 'further', 'shade', 'impending', '—', 'endured', 'someone', 'innocence', 'resolution', 'care', 'bine', 'cognizant', 'religion', 'faced', 'while', 'maman', 'under', "snowden's", 'shores', 'prayers', 'contemporary', 'person', 'die', 'lot', 'conclusion', "weren't", 'suffering', 'off', 'bored', 'choose', 'their', 'regulated', 'thousand', 'right', "'all", 'begets', 'pas', 'analytical', 'nu', 'tell', 'passing', 'prea', 'certainty', 'philosophy', 'kinds', 'hard', 'nici', 'meditation', 'characterized', 'owes', 'quality', 'télégramme', 'god', 'value', 'non-being', 'letting', 'us', 'confounding', 'nenorocita', 'learning', 'ideals', 'unfortunately', 'them', 'sturdy', 'left', 'ruled', 'young', 'today’s', 'other', 'escape', 'hands', 'growling', 'sunday', 'immemorial', 'prehistory', 'blurs', 'point', 'merely', 'too', 'est', 'thus', 'murder', 'enough', 'put', 'symbol', "he'll", 'heartache', 'about', 'apatia', 'mère', 'potential', 'knows', 'went', 'conviction', 'atoned', 'with', 'work', 'signs', 'inconsistency', 'always', 'sage', 'me', 'white', 'coast', 'sit', 'exist', 'there', 'picture', 'transmitted', 'encountered', 'do', 'finally', "c'était", 'arises', 'ever', 'civilization', 'now', 'originality', 'meaning', "life's", 'peasant', 'working', 'light', 'among', 'useless', 'live', 'an', 'virtually', 'innocent', 'sunny', 'projected', 'interesting', 'proportion', 'when', "who've", 'existence', 'without', 'foolishness', 'made', 'prospect', 'daily', 'impatiently', 'are', 'just', '-', 'be', 'holds', "isn't", 'something', 'itself—', 'rot', 'contradictions', 'never', 'slowly', 'like', 'fingers', 'stiam', "i've", 'space', 'well', 'spiritual', "wasn't", 'un', 'effort', 'peoples', 'hatred', 'there’s', 'entire', 'give', 'boredom', 'turn', 'has', 'oricare', 'i', 'remote', 'may', 'tolerate', "men's", 'deeper', 'everything—even', 'secret', 'mine', 'few', 'desgustul', 'certain', 'criminals', 'sais', 'then', 'culture', 'goodness', 'love', 'acknowledge', 'virus', 'plead', 'either', 'valuable', 'stretching', 'respect', 'phenomena', 'excuse', 'vicarious', 'frantically', 'capable', 'lives', 'for', 'courts', 'fighting', 'rock', 'world', 'premeditation', 'nihilism', 'does', 'wondering', 'anchor', 'jew', 'ar', "j'ai", 'against', 'philosophers', 'touches', 'whereas', 'tables', "hadn't", 'being', 'dignity', 'crime', 'stupidity', 'ideas', 'individual’s', "can't", 'rorschach', 'blood', "'i", 'damn', 'breathe', 'so', 'euthanasia', 'today', 'used', 'anyone', 'modest', "meaning'", 'morte', 'future', 'perpetrated', 'sacrifice', 'if', 'distingués', 'as', 'spreading', 'church', 'grew', '--', 'fi', 'painful', 'weight', 'considered', 'endless', 'program', "winter's", 'sentiments', 'it', 'would', 'somebody', "it's", 'toward', 'cars', 'eyes', 'air', 'because', "aujourd'hui", 'cela', 'worst', 'nobody', 'fight', 'believe', "you'd", 'ne', 'bells', 'gone', 'garbage', 'dim', 'pure', 'bed', 'empty', 'than'}
