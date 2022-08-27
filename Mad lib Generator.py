
from random import randint
import copy

story = (
    "It was a {}, cold November day." +
    "I woke up to the {} smell of {} roasting in the {} downstairs." +
    "I {} down the stairs to see if I could help {} the dinner." +
    "My mom said, See if {} needs a fresh {}." +
    "So I carried a tray of glasses full of {} into the {} room." +
    "When I got there, I couldnt believe my {}! There were {} {} on the {}!"
)    

# create a dictionary to lookup words by type
word_dict = {
    'adjective':['Horrible', 'Best', 'Terrible', 'Terrific', 'Horrifying', 'Morbid', 'Morbin', 'Nice', 'Sweet', 'Succulent'],
    'adjective':['Horrible', 'Best', 'Terrible', 'Terrific', 'Horrifying', 'Morbid', 'Morbin', 'Nice', 'Sweet', 'Succulent'],
    'bird type':['Poultry', 'Chickens', 'Eagles', 'Ducks', 'Flamingo', 'Cockatrice'],
    'room':['Kitchen', 'Bathroom', 'Bedroom', 'Living room', 'Meeting room', 'Rest room', 'Attic'],
    'room':['Kitchen', 'Bathroom', 'Bedroom', 'Living room', 'Meeting room', 'Rest room', 'Attic'],
    'past tense':['Walked', 'Ran', 'Fell', 'Dropped', 'Flew'],
    'verb':['Make', 'Cook', 'Ruin', 'Decimate'],
    'verb-ing':['Falling', 'Dripping', 'Erupting', 'Morbing'],
    'verb-ing':['Falling', 'Dripping', 'Erupting', 'Morbing'],
    'liquid':['Water', 'Lemonade', 'Orange', 'BMilk', 'HMilk', 'Polish'],
    'liquid':['Water', 'Lemonade', 'Orange', 'BMilk', 'HMilk', 'Polish'],
    'relative name':['Kid', 'Finger', 'Paint', 'Hank', 'Walter'],
    'noun':['Floor', 'Roof', 'Ceiling', 'Walls', 'Electronic socket'],
    'body part':['Rectum', 'Urethra', 'Cloaca', 'Mitochondria', 'Retina', 'Eyes']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('bird type', local_dict),
        get_word('room', local_dict),
        get_word('room', local_dict),
        get_word('past tense', local_dict),
        get_word('verb', local_dict),
        get_word('verb-ing', local_dict),
        get_word('verb-ing', local_dict),
        get_word('liquid', local_dict),
        get_word('liquid', local_dict),
        get_word('relative name', local_dict),
        get_word('noun', local_dict),
        get_word('body part', local_dict)
)        
 
print("STORY 1: ")
print(create_story())
print()
print("STORY 2: ")
print(create_story())