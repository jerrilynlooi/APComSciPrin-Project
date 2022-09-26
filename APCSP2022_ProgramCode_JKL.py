# AP COMPUTER SCIENCE PRINCIPLES
# PERFORMANCE TASK 2022

# This program is written in python language

# instructions for basic input of the game
def howToPlay():
    print("""HOW TO PLAY:
Enter text according to the prompt to progress the story!
When you see this \">>>\" symbol, simply press the ENTER key.
    
Try it now to start the game!""")
    cont()
    
# function prints a string in a nice box
def text(stringList):
        lineLen = len(max(stringList, key=len))
        text = " __" + lineLen*("_") + "__ \n"
        text += "|  " + lineLen*(" ") + "  |\n"
        for string in stringList:
            text += "|  " + string + (lineLen - len(string))*(" ") + "  |\n"
        text += "|__" + lineLen*("_") + "__|\n"
        return print(text)
# function prints a speech bubble from someone other than YOU
def speech(stringList, speaker):
        lineLen = len(max(stringList, key=len))
        text = " __" + lineLen*("_") + "__ \n"
        text += "/  " + lineLen*(" ") + "  \\\n"
        for string in stringList:
            text += "|  " + string + (lineLen - len(string))*(" ") + "  |\n"
        text += "\\  " + lineLen*("_") + "__/\n"
        text += " \\/\n" + speaker + "\n"
        return print(text)
# function prints a speech bubble from YOU
def selfSpeech(string):
        lineLen = len(string)
        text = "           __" + lineLen*("_") + "__ \n"
        text += "          /  " + lineLen*(" ") + "  \\\n"
        text += "          |  " + string + "  |\n"
        text += "          \\__" + lineLen*("_") + "  /\n"
        text += lineLen*(" ") + "             \\/\n"
        text += lineLen*(" ") + "            YOU\n"
        return print(text)
# function lets the user pause before continuing with the story
def cont():
    cont = input(">>>")

# function prompts multiple choice, as well as checks for invalid inputs
def pick(n):                            # takes 1 parameter of how many options to let user pick from
    ask = ""                            # create String ask to hold output string
    optionsList = []                    # create List optionsList to hold options
    for x in range(1,n+1):              # loop from 1 to n
        optionsList.append(str(x))          # adds valid options to list
    if x == 1:                          # if n = 1
        ask += "\"1\""                      # set string to be "1"
    else:                               # elif n != 1
        for x in range(1,n):                # loop through 1 to n-1
            ask += "\""+str(x)+"\", "           # add the option to string
        ask += "OR \""+str(n)+"\" "          # adds last option to string
    pick = input("TYPE "+ask)           # adds "TYPE " at beginning of string
    while pick not in optionsList:      # check condition that user input is in optionsList
        pick = input("INVALID, TRY "+ask)   # prompt input again if invalid
    return (int(pick)-1)                # return list index for reference in other methods
    
# function runs an ask-and-answer dialogue
# prompts user to pick what to say, and gives answer accordingly
# also returns the index of chosen dialogue
def dialogue(shownOptions,optionsList,answersList, speaker):
    if shownOptions == ["-"]:
        shownOptions = optionsList
    numberedOptions = []
    for string in shownOptions:
        numberedOptions.append(f"{str(shownOptions.index(string)+1)}. {string}")
    text(numberedOptions)
    x = pick(len(optionsList))
    selfSpeech(optionsList[x])
    cont()
    speech(answersList[x], speaker)
    return x

# a list of ASCII art
itemsArt = ["""
    Berries from Berry
    
             -=-.__.--
               /    \\
             //      \\\\
           //       _.- =-._
       _.-= =-._  /'    \\/  '\\
     /'   \/    '\\            |
    |             |           |
    |             |\\         /
     \\          // "-.___.-"
       "-.___.-"         
""",
"""
    Badger Bob's Misty Flower
    
       ._  /-   -.
      (  \\/  \\/   )
      _\\   \\/     /  
    /      . ::  /-.
   (   /   ::._     )
    \\ / (    /\\\\    / 
     \\   \\  /  \\\\ \\/    
           V    \\\\
""",
"""
    A Dusty Pebble
    
          __....____
        /'          "'\\
       /  =..          \\
     /      '"-    \\    |
    | .=.          /    /
    \\..__    ____/__--_/
         ''''
""",
"""
    Random Duck Feather
    
            .-'"'"\\ 
         "\\/  /   \\/,
       .\\/   /   \\/"
     '\\    //   /'
   '\\    //   /'
    \\  //  /"
    \\//..-   
    /
""",
"""
    Kero's Lily Pad
    
        _._      _._
      /'   \\    /   '\\
     (       \\/       ) 
    (        :         )
    |         :        |
     \\        :       /
      '._    :     _.'  
         '"-====-"'   
""",
"""
    A Rare Rabbit Token
    
         _.-====-._      
      .'            '.
     /   ('\\    /')   \\ 
    |     \\ |__| /     |
    |     /      \\     |
     \\   (_ > .< _)   /
      '._  ""  ""  _.'  
         '"-====-"'   
""",
"""
    A Burrow Twig
    
   ("'")    
  (\\\\ )")   ('"")     
 ( \\.\\   ) (  // )
  (\\  \\  ) (/'/ )
    \\. \\  /  /
      \\ \/  /
      / './
     /  ./    
    |___/        
""",
"""
    Rie's Big Carrot
    
     /\\/\\/\\/\\/\\
     \\\\___   //
     /'   "" '\\
    / ___      \\
    \\  __      /
     \\  --    /
      \\     ./
       \\   ./
        \\__/ 
"""]

# create object to orient functions around
class Player:
    def __init__(self, Name, Type, Movement, favFood, Bag, Locations):
        self.name = Name
        self.type = Type
        self.move = Movement
        self.food = favFood
        self.bag = Bag
        self.loc = Locations
    
    # function sets the player name based on user input
    def pickName(self):
        text(["Welcome to The Forest!","","What is your name?"])
        string = input("NAME: ")
        while string.strip(" ") == "":
            string = input("INVALID, What is your name? ")
        return string
    # function sets the creature type based on user input
    def pickType(self):
        text([f"Nice to meet you, {self.name}!","","What forest creature are you?","",
            "1. Squirrel","2. Deer","3. Bird"])
        types = ["Squirrel","Deer","Bird"]
        moveTypes = ["scurry","prance","fly"]
        choose = pick(3)
        self.move = moveTypes[choose]
        return types[choose]
    
    # function adds item to self.bag and displays text
    def acquire(self,item):
        self.bag.append(item)
        text([f"You acquire -{item}-"])
        cont()

    # function presents user with locations to go to
    def Map(self):
        if len(self.loc) == 0:
            return self.end()
        where = ["Where to next?",""]
        for x in range(len(self.loc)):
            where.append(f"{x+1}. {self.loc[x]}")
        text(where)
        go = pick(len(self.loc)) 
        self.pickRoute(self.loc.pop(go)) # also removes chosen location from list
    # function chooses which route to run based on entered string
    def pickRoute(self,location):
        text([f"Going to {location}!"])
        cont()
        if location == "Big Tree":
            self.route1()
        elif location == "Forest Pond":
            self.route2()
        elif location == "Burrow":
            self.route3()
    
    # function starts the game
    def start(self):
        self.name = self.pickName()
        self.type = self.pickType()
        text(["Wonderful!","",f"{self.name} the {self.type}...","It has a nice ring to it!"])
        cont()
        text(["Here in The Forest, you can","travel to different locations,","meet other creatures, and pick","up trinkets on the way!","","Let's meet your first friend!"])
        cont()
        self.routeO()
    
    def routeO(self):
        r0Character = "Berry the Bear"
        speech(["Hey! I'm Berry, your local Forest guide!"], r0Character)
        A = dialogue(["-"],[f"Hi, I'm {self.name}!","Who are you?! Where am I?!","Do you like berries?"],
        [[f"Nice to meet you {self.name}!","","Hey, I always wondered",f"What are {self.type}s\' favorite food?"],
        ["I- I\'m Berry!","and we're in the Forest!","","Are you okay?"],
        ["Of course, it's my favorite!","",f"Say, as a {self.type}, what's your favorite food?"]],
        r0Character)
        if A == 1:
            A1 = dialogue(["-"],["Oh, my bad. I got confused for a second.","This isn't real. It's a simulation!"],
            [["All good! How about I get you","a snack to feel better?","","What's your favorite food?"],
            ["...sure. Maybe I can get you","something to help you calm down","","What's your favorite food?"]],r0Character)
        shownFood = ["Berries"]
        foodOptions = ["I really like berries!"]
        foodAnswers = [["No way!","","Since you're just like me, here's","a few to bring on your travels!"]]
        if self.type == "Squirrel":
            shownFood.extend(("Clovers","Mushrooms"))
            foodOptions.extend(("I love snacking on clovers!","Mushrooms! They're the best."))
            foodAnswers.extend((["That's a lucky snack!"],["Delicious! Just be careful"," of poisonous shrooms..."]))
        elif self.type == "Deer":
            shownFood.extend(("Ferns","Roots"))
            foodOptions.extend(("Ferns are my favorite!","Roots! You can't go wrong with them."))
            foodAnswers.extend((["Ferns! How nutritious!"],["That's right! Nothing better","than some fresh spuds."]))
        elif self.type == "Bird":
            shownFood.extend(("Seeds","Nectar"))
            foodOptions.extend(("Seeds! They are crunchy!","I love to drink nectar!"))
            foodAnswers.extend((["Crunchy indeed! I like em too."],["Sounds sweet! But it", "doesn't beat honey!"]))
        self.food = shownFood[dialogue(shownFood,foodOptions,foodAnswers,r0Character)]
        if self.food == "Berries":
            self.acquire("Berries")
        speech(["You know what? I think you", "can explore on your own!","","Here, take this map!"],r0Character)
        cont()
        self.Map()
    
    def route1(self):
        r1Character = "??? the Badger"
        text([f"Welcome to the Big Tree!","","Around the base of the tree,","you come across a sad-looking","badger."])
        r1A = dialogue(["-"],["Hi there!","Are you okay?","..."],
        [["Hi."],["Not really."],["...hi"]],r1Character)
        r1B = dialogue(["-"],["What's your name?","What's wrong?","Do you live here?"],
        [["What's your name first?"],["I'm hungry..."],["No, but my favorite snacks","are around here..."]],r1Character)
        r1Character = "Bob the Badger"
        listA = ["Hey, would you mind helping","me reach my snacks?","","The name is Bob."]
        if r1B == 0:
            dialogue(["-"],[f"I'm {self.name} the {self.type}!",f"{self.name}."],
            [["You seem nice.","I'm Bob."],["Hi. I'm Bob"]],r1Character)
            listA.remove(listA[2])
            listA.remove(listA[2])
        cont()
        speech(listA,r1Character)
        assist = True
        r1c = dialogue(["-"],["Sure!","Where are your snacks?","No."],
        [["Why thank you! They are the flowers", "right up there. The branch is too","high for me to reach"],
        ["Right up there! On","that high branch.","","Thank you so much!"],["..."]],r1Character)
        cont()
        if r1c == 1:
            r1c1 = dialogue(["-"],["You're welcome!","I never said I'd help."],[["These are my favorite flower bulbs!"],["..."]],r1Character)
            if r1c1 == 1:
                assist = False
        elif r1c == 2:
            assist = False
        if assist == True:
            if self.type == "Deer":
                text(["You use your deer height to reach the","branch and retrive Bob's snacks."])
                cont()
            else:
                text([f"You {self.move} to the branch and retrieve", "the flower bulbs for Bob."])
                cont()
            speech(["Thank you so, so much!","","Here is something for your troubles."], r1Character)
            self.acquire("Misty Flower")
        elif assist == False:
            text(["With tears in his eyes, Bob the","Badger runs away, kicking up the dirt.","","That wasn't very nice of you."])
            self.acquire("Dusty Pebble")
        self.Map()

    def route2(self):
        r2Character = "???? the Frog"
        text([f"Welcome to the Forest Pond!","","Approaching the pond, you spot","a green frog seated on a lilypad."])
        r2A = dialogue(["-"],["Hello!","Ribbit!","Quack!"],[["Hi! Hi!"],["Ribbit? Ribbit!"],["..."]], r2Character)
        text(["The frog hops forward from the","lily pad to the sand by pond."])
        cont()
        r2Character = "Kero the Frog"
        if r2A == 2:
            speech(["I'm no duck-duck! I'm Kero!"],r2Character)
        r2B = dialogue(["-"],[f"I'm {self.name}!","RIBBIT?!","quack."],[["Kero is Kero!"],["Ribbit. Kero ribbit?"],["No quack!"]], r2Character)
        if r2B == 2:
            text(["Kero dives into the lake with","a splash, leaving you alone.","","What a strange encounter."])
            cont()
            self.acquire("Duck Feather")
        else:
            text(["Kero sticks his froggy tongue","out at you with a smile."])
            cont()
            speech(["Kero likes you!","Kero give present!"], r2Character)
            self.acquire("Lily Pad")
        self.Map()
    
    def route3(self):
        r3Character = "??? the Rabbit"
        text([f"Welcome to the Burrow!","","You peer upon the round","hole in the ground."])
        listB = ["Is anyone there?","Hellooooo?","AAAAAA!"]
        listB2 = ["1. Is anyone there?","2. Hellooooo?","3. AAAAAA!"]
        listC = [["Here!"],["Hi there!"],["Shhhh! We're trying to sleep!"]]
        text(listB2)
        r3A = pick(len(listB2))
        selfSpeech(listB[r3A])
        cont()
        text(["A pair of white fluffy bunny ears","pop out of the Burrow's entrance,","followed by a rabbit's head."])
        speech(listC[r3A],r3Character)
        if r3A == 2:
            r3A1 = dialogue(["-"],["Oh! My bad.","..."],
            [["It's okay, we're awake now."],["Yep! Just like that."]],r3Character)
        r3Character = "Rie the Rabbit"
        r3B = dialogue(["-"],["Who lives here in the burrow?","Can I come in?","Do rabbits like berries?"],
        [["Rie lives here! Me! Me","and my many brothers","and sisters!"],["No! Only Rie and Rie's","family allowed in burrow!"],
        ["Berries? Rie likes berries!","","Do you have some berries?"]], r3Character)
        if r3B == 2:
            listD1 = ["No","Yes"]
            listD2 = ["Sorry, I don't have any berries","I do! Here, have some!"]
            listD3 = [["It's okay! No need!"],["Sweet! Thank you, thank you!"]]
            if "Berries" not in self.bag:
                listD1.remove(listD1[1])
                listD2.remove(listD2[1])
                listD3.remove(listD3[1])
            r3B2 = dialogue(listD1,listD2,listD3,r3Character)
            if r3B2 == 1:
                text(["How fortunate you had berries to share!"])
                self.acquire("Rabbit's Token")
        speech([f"{self.type}! Would you like to meet my brother?"],r3Character)
        r3c = dialogue(["-"],["Sure!","I'm fine...","No."],[["Marvelous!"],
        ["Aw, too bad. Well then,","be on your way!"],["...","","You're too big to fit","down burrow anyways!"]], r3Character)
        if r3c != 0:
            self.acquire("Burrow Twig")
        else:
            text(["Rie the Rabbit pops down the entrance and","almost instantly reappears with another bunny."])
            cont()
            speech([f"This is for you, {self.type}!"],"Ronald the Rabbit")
            self.acquire("Big Carrot")
        self.Map()

    def end(self):
        r0Character = "Berry the Bear"
        text([f"You {self.move} your way back","to the beginning where you","had met your first friend."])
        cont()
        text(["Let's take a look at what","you've collected today!"])
        for item in self.bag:
            self.display(item)
            cont()
        speech([f"Wow, {self.name}!","" "You've had an eventful day! I'm","happy you came to the Forest!"],r0Character)
        cont()
        text(["Your eyes close as the sun sets."])
        cont()
        print(f"Hope you enjoyed your day as a {self.type}!\n Thank you for playing!")
        pass
    
    def display(self,item):
        itemsList = ["Berries","Misty Flower","Dusty Pebble","Duck Feather","Lily Pad","Rabbit's Token","Burrow Twig","Big Carrot"]
        print(itemsArt[itemsList.index(item)])

howToPlay()
Player = Player("","","","",[],["Big Tree","Forest Pond","Burrow"])
Player.start()
