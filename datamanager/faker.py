import random

from api.models import Provider, Fruit, Bundle
from api.serializers import ProviderSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

location = [
        "Mexico",
        "Madagascar",
        "Espagna",
        "Venezuela",
        "South Africa"
    ]

providers = [
        "Shiftinglight",
        "Granddream",
        "Plumpbasket",
        "Smoothgut"
    ]

fruits = [
        "apple",
        "apricot",
        "avocado",
        "banana",
        "bell pepper",
        "bilberry",
        "blackberry",
        "blackcurrant",
        "blood orange",
        "blueberry",
        "boysenberry",
        "breadfruit",
        "canary melon",
        "cantaloupe",
        "cherimoya",
        "cherry",
        "chili pepper",
        "clementine",
        "cloudberry",
        "coconut",
        "cranberry",
        "cucumber",
        "currant",
        "damson",
        "date",
        "dragonfruit",
        "durian",
        "eggplant",
        "elderberry",
        "feijoa",
        "fig",
        "goji berry",
        "gooseberry",
        "grape",
        "grapefruit",
        "guava",
        "honeydew",
        "huckleberry",
        "jackfruit",
        "jambul",
        "jujube",
        "kiwi fruit",
        "kumquat",
        "lemon",
        "lime",
        "loquat",
        "lychee",
        "mandarine",
        "mango",
        "mulberry",
        "nectarine",
        "nut",
        "olive",
        "orange",
        "pamelo",
        "papaya",
        "passionfruit",
        "peach",
        "pear",
        "persimmon",
        "physalis",
        "pineapple",
        "plum",
        "pomegranate",
        "pomelo",
        "purple mangosteen",
        "quince",
        "raisin",
        "rambutan",
        "raspberry",
        "redcurrant",
        "rock melon",
        "salal berry",
        "satsuma",
        "star fruit",
        "strawberry",
        "tamarillo",
        "tangerine",
        "tomato",
        "ugli fruit",
        "watermelon"
    ]

bundle = [
    "Battling Soldier",
    "Beauty Berserker",
    "Bright Wood Berserker",
    "Diamond Emperess",
    "Diamond Steel Guardian",
    "Fair Dancer Goddess",
    "Police Controller",
    "Screaming Dance Angel",
    "Weeping Attacker",
    "Wind Sailor Policewoman"
]

##############
#  PROVIDER  #
##############

tmp_providers = []

for i in providers:
    tmp = Provider(name = i, location = location[random.randrange(0, len(providers))])
    tmp_providers.append(tmp)
    tmp.save()
    
############
#  FRUITS  #
############

for i in fruits :
    tmp_p = tmp_providers[random.randrange(0, len(tmp_providers))]
    tmp = Fruit(name = i, origin = tmp_p.location, provider = tmp_p, stock = random.randrange(2, 20), price = random.randrange(2, 20))
    tmp.save()