# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import sys



first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'BeenieWeenie'",
"Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
'Mergatroid', '"Mr Peabody"', 'OilCan',
'Oinks', 'Old Scratch',
'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
"Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt',
'Johnson',
'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'SugarGold',
'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks')

while True:
    firstname=random.choice(first)
    lastname=random.choice(last)
    print("{} {}".format(firstname, lastname), file=sys.stderr)
    print("\n\n")
    
    tryagain=input("Press n to exit \n\n")
    if tryagain.lower()=="n":
        break
    input("\nPress Enter to exit.")