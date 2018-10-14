import random

# Программа выдает рандомно либо туристическую справку, либо астрологический прогноз, либо статью по психологии в популярном женском журнале.

def singular_nouns():
    with open('singular_nouns.tsv') as f:
        nouns = f.read().split('\n')
    adjective = adjectives()
    return adjective + ' ' + random.choice(nouns)

def adjectives():
    with open('adjectives.tsv') as f:
        adjectives = f.read().split('\n')
    return random.choice(adjectives)


place = 1

def places():
    with open('places.tsv') as f:
        places = f.read().split('\n')
    new_place  = random.choice(places)
    return new_place

def amount():
    with open('amount.tsv') as f:
        amount = f.read().split('\n')
    return random.choice(amount)

def verbs_of_visit():
    with open('verbs.tsv') as f:
        verbs = f.read().split('\n')
    return random.choice(verbs)

def sightseeing_places():
    with open('exhibits.tsv') as f:
        exhibits = f.read().split('\n')
    adjective1 = adjectives()
    adjective2 = adjectives()
    while adjective1 == adjective2:
        adjective2 = adjectives()
    noun1 = random.choice(exhibits)
    noun2 = random.choice(exhibits)
    while noun1 == noun2:
        noun2 = random.choice(exhibits)
    with open('cultural_places.tsv') as f:
        cultural_places = f.read().split('\n')
    return 'the ' + random.choice(cultural_places) + ' of ' + adjective1 + ' ' + noun1 + ' and ' + adjective2 + ' ' + noun2



def verbs_of_preference():
    with open('verbs_of_preference.tsv') as f:
        verbs_of_preference = f.read().split('\n')
    return random.choice(verbs_of_preference)

def verbs():
    with open('verbs_inf.tsv') as f:
        verbs_inf = f.read().split('\n')
    return random.choice(verbs_inf)

def adverbs():
    with open('adverbs.tsv') as f:
        adverbs = f.read().split('\n')
    return random.choice(adverbs)

def destinations():
    with open('destinations.tsv') as f:
        destinations = f.read().split('\n')
    return random.choice(destinations)

def affirmative():
    random_amount = amount()
    adj1 = adjectives()
    adj2 = adjectives()
    noun = singular_nouns() + 's'
    destination = destinations()
    if adj1[0].lower() in 'euioa':
        article = 'an'
    else:
        article = 'a'
    if random_amount == 'at every corner':
        return destination + ' is ' + article + ' ' + adj1 + ' city with ' + adj2 + ' ' + noun + ' ' + random_amount + '.'
    else:
        return destination + ' is ' + article + ' ' + adj1 + ' city with ' + random_amount + ' ' + adj2 + ' ' + noun + '.'

def condition():
    noun = singular_nouns()
    if noun[0].lower() in 'euioa':
        article = 'an'
    else:
        article = 'a'
    a_typical_citizen = 'If you are ' + article + ' ' + noun + ', you ' + \
                        adverbs() + ' ' + verbs_of_preference() + ' to ' + verbs() + '.'
    return a_typical_citizen

def question():
    noun = singular_nouns()
    if noun[0].lower() in 'euioa':
        article = 'an'
    else:
        article = 'a'
    return 'Are you ' + article + ' ' + noun + '? '

def negation():
    with open('adjectives.tsv') as f:
        adjectives = f.read().split('\n')
    global place
    return 'But ' + singular_nouns() + ' don\'t ' + verbs_of_preference() + ' to ' + verbs_of_visit() + ' ' + places() + '.'

def imperative():
    place = sightseeing_places()
    verb = verbs_of_visit()
    imperative = ['should', 'must']
    adverbs = ['totally', 'definitely', 'probably']
    openings = ['Then', 'Then why don\'t you ']
    random_opening = random.choice(openings)
    if random_opening == 'Then why don\'t you ':
        result = random_opening + verb + ' ' + place + '? '
    else:
        result = random_opening + ' you ' + random.choice(imperative) + ' ' + random.choice(adverbs) +  ' ' + verb + ' ' + place + '.'
    return result

def travel_guide():
    return affirmative() + '\n' + condition() + ' ' + negation() + '\n' + question() + imperative() + '\n'


def main():
    print ()
    print (travel_guide())
    return 0

if __name__ == '__main__':
    main()

# Are you a little scientist? Then you must totally spend a few days at the Factory of small suitcases and organic fruits.
# Are you a little father? Why don't you visit the Museum of modern spoons and medium size fruits?
# Are you a conservative chess player? Then why don't you spend a few days at the Museum of luxury wallpapers and small pizza boxes.
# Are you a religious dog? Then you must probably try the Museum of forgotten suitcases and royal suitcases.
# Are you a little mother? Then you should definitely go to the Festival of contemporary blankets and ancient pizza boxes.
# Are you a young mother? Then why don't you take a look at the Museum of broken pizza boxes and spoons?
# Are you a young dog? Then you should never visit the Factory of luxury pizza boxes and contemporary spoons.
# Are you a potential dog? Then you should probably visit the Factory of medium size pizza boxes and broken suitcases.
