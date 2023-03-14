# import modules
import random
import time
import sys
import math
import replit
from replit import db

#import music for game
from replit import audio

#source = audio.play_file('sound.mp3')

coins = 0
pimonMoveSet = '''Option 1: Tackle
Option 2: Quick Attack
Option 3: Leaf Edge
Option 3: Razor Wind'''

radiuSealMoveSet = '''Option 1: Tackle
Option 2: Quick Attack
Option 3: Bubble
Option 4: Water Squirt'''

sirCumferenceMoveSet = '''Option 1: Tackle
Option 2: Quick Attack
Option 3: Flame Fist
Option 4: Fire Charge'''

# game starts
print(
  "Hello New Adventurer! My name is Professor Baobab, and welcome to the world of POKEMON!"
)
time.sleep(2.3)
print("This is a bit different though... It is also the world of MATH!")
time.sleep(2.3)
print('Credit to LEA SHIN and FINN USON who made the pokemon artwork!')
time.sleep(2.3)

print()

#ask for name
userNameBeforeUpper = input("Now, what is your name? (Only use words) ")
if userNameBeforeUpper == 'lorelei':
  print('< 3')
elif userNameBeforeUpper == 'Lorelei':
  print('< 3')
elif userNameBeforeUpper == 'ace':
  print('FLAME FIST ACE!!!!')
elif userNameBeforeUpper == 'Ace':
  print('Ace filled the empty void in my chest ;)')
elif userNameBeforeUpper == 'ACE':
  print('Ace is fire -Liz Bardzell')
else:
  time.sleep(2)
  print()
  print('...')
  time.sleep(2)

userName = userNameBeforeUpper.upper()

print()

#ask for gender
userGender = input("Okay " + userName + ", are you a boy, girl, or other? ")

userGender_Lower = userGender.lower()

if userGender_Lower == 'boy':
  print("Okay, so you are a boy!")
  print()
  time.sleep(2.5)

elif userGender_Lower == 'girl':
  print("Okay, so you are a girl!")
  print()
  time.sleep(2.5)

else:
  print("Ok " + userName +
        ", so you go by another gender! That's all right! We accept everyone!")
  print()
  time.sleep(2.5)

#starter pokemon loop
while True:
  starterPokemonBeforeUpper = input(
    '''There are three starter pokemon in this region! 
Pi-Mon is the leafy fairy Pokémon, and is commonly hunted down by wandering Travelers. They are most useful for storing emergency food.'
Radiuseal, the water seal Pokémon is commonly a lonely Pokémon, they prefer solitude than anything else.
SirCumference the fire hedgehog pokemon! It is very hard and durable.
Which pokemon will you choose?: ''')

  starterPokemon = starterPokemonBeforeUpper.upper()

  if starterPokemon == 'RADIUSEAL':
    pokemon = "RADIUSEAL"
    print("Ok! So you picked the water seal pokemon!")
    print()
    time.sleep(1)
    break

  elif starterPokemon == 'PI-MON':
    pokemon = "PI-MON"
    print("Ok! So you picked emergency food!")
    print()
    time.sleep(3)
    break

  elif starterPokemon == 'SIRCUMFERENCE':
    pokemon = 'SIRCUMFERENCE'
    print("Ok! So you picked the fire hedgehog pokemon!")
    print()
    time.sleep(1)
    break

#adventure START
print("On with your adventure!")
print()
time.sleep(1.5)
print(
  "Uh oh! There's a fork in the road! Would you like to turn right, left, or forward?"
)
directionDecision = input()
directionDecisionLowered = directionDecision.lower()


#the first battle code
def rightBattle():
  print()
  print(
    "You will need to answer this math question to get through: If a circle's diameter is 6, find the area using 3.14 as pi. Answer to the nearest hundreth. (Hint: the area of a circle is pi times radius squared!)"
  )
  answerRight = input()
  if answerRight == '28.26':
    print(
      'Correct! You may pass through. Did you also know that irrational numbers are numbers that cannot be put into a simple fraction? '
    )
    print()
    time.sleep(2)
    print('You see grass ahead')
    weedleMoves = ['Poison Sting', 'Bug Bite', 'String Shot']
    poke1 = 'Pikachu'
    global userHealth
    userHealth = 25
    weedleHealth = 20
    scratch = 'SCRATCH'
    quickAttack = 'QUICK ATTACK'
    thunderShock = 'THUNDER SHOCK'
    tackle = 'TACKLE'

    preEngageFight = input('Would you like to go into the grass? Yes or No? ')
    engageFight = preEngageFight.lower()
    if engageFight == 'yes':
      print('Wild POKEMON has been encountered!')
      time.sleep(2)
      print()
      wildPokemon = []
      print('Wild WEEDLE:')
      time.sleep(1)
      print('Health:', weedleHealth)
      time.sleep(2)
      print()
      print('''Your Pokemon:
      ''', pokemon)
      pokemonDecisionBefore = input("What pokemon will you like to choose? ")

      pokemonDecision = pokemonDecisionBefore.upper()

      if pokemonDecision == pokemon:
        print()
        time.sleep(1.5)
        print(pokemon)
        time.sleep(1)
        userHealth = str(userHealth)
        print('Health:', userHealth)
        time.sleep(2)
        print()

        while weedleHealth > 0:
          weedleDamage = random.randint(1, 10)
          userDamage = random.randint(5, 15)
          decision = input('''What move would you like to use?
          Option 1: Tackle
          Option 2: Quick Attack
          Option 3: Thunder Shock
          Option 4: Scratch
          (Input a number for the move you want to use.): ''')
          print()
          if decision == '1' or decision == 'tackle' or decision == 'Tackle':
            print('User used', tackle + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("The wild WEEDLE is now at", weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Weedle used poison shot!')
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')

            else:
              print("Wild WEEDLE has fainted!")
              print("User has gained 14 experience!")
              break

          if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
            print('User used ' + quickAttack + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("The wild WEEDLE is now at", weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Weedle used poison shot!')
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')

            else:
              print("Wild WEEDLE has fainted!")
              print("User has gained 14 experience!")
              break

          if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
            print('User used', thunderShock + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("The wild WEEDLE is now at", weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Weedle used poison shot!')
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')

            else:
              print("Wild WEEDLE has fainted!")
              print("User has gained 14 experience!")
              break

          if decision == '4' or decision == 'scratch' or decision == 'Scratch':
            print('User used ' + scratch + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage
            if weedleHealth > 0:
              print("The wild WEEDLE is now at", weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Weedle used poison shot!')
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')

            else:
              print("Wild WEEDLE has fainted!")
              print("User has gained 14 experience!")
              break

      else:
        print("You did not select a pokemon and got jumped by a weedle.")
        print("""
      
        GAME OVER
      
        """)

    else:
      print("Too bad, you're doing this anyways!")
      time.sleep(2)
      print('Wild POKEMON has been encountered!')
      time.sleep(2)
      print()
      wildPokemon = []
      print('Wild WEEDLE:')
      time.sleep(1)
      print('Health:', weedleHealth)
      time.sleep(2)
      print()
      print('''Your Pokemon:
      ''', pokemon)
      pokemonDecisionBefore = input("What pokemon will  you like to choose? ")

      pokemonDecision = pokemonDecisionBefore.lower()

      if pokemonDecision == pokemon:
        print()
        time.sleep(1.5)
        print(pokemon)
        time.sleep(1)
        userHealth = str(userHealth)
        print('Health:', userHealth)
        time.sleep(2)
        print()

        decision = input('''What move would you like to use?
        Option 1: Tackle
        Option 2: Quick Attack
        Option 3: Thunder Shock
        Option 4: Scratch
        (Input a number for the move you want to use.): ''')
        print()

      while weedleHealth > 0:
        weedleDamage = random.randint(1, 10)
        userDamage = random.randint(5, 15)
        decision = input('''What move would you like to use?
          Option 1: Tackle
          Option 2: Quick Attack
          Option 3: Thunder Shock
          Option 4: Scratch
          (Input a number for the move you want to use.): ''')
        print()
        if decision == '1' or decision == 'tackle' or decision == 'Tackle':
          print('User used', tackle + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild WEEDLE is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Weedle used poison shot!')
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild WEEDLE has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
          print('User used ' + quickAttack + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild WEEDLE is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Weedle used poison shot!')
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild WEEDLE has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
          print('User used', thunderShock + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild WEEDLE is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Weedle used poison shot!')
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild WEEDLE has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '4' or decision == 'scratch' or decision == 'Scratch':
          print('User used ' + scratch + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage
          if weedleHealth > 0:
            print("The wild WEEDLE is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Weedle used poison shot!')
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild WEEDLE has fainted!")
            print("User has gained 14 experience!")
            break

  if answerRight != '28.26':
    time.sleep(2)
    print('Wrong.')
    time.sleep(2)
    print('GAME OVER')
    time.sleep(1)
    print('Restart the game to try again!')
    print()
    time.sleep(1)
    quit()


def trainerBattle():
  print()
  trainerAcePokemon = 'Radiuseal'
  if pokemon == 'PI-MON':
    trainerAcePokemon = 'SirCumference'

  elif pokemon == 'SIRCUMFERENCE':
    trainerAcePokemon = 'RADIUSEAL'

  elif pokemon == 'RADIUSEAL':
    trainerAcePokemon == 'PI-MON'
  print(
    "You see a strange sign in front of you. It says, 'The radius of a circle is 25. What is the circumfernce of the circle? Hint: the formula to find circumference is 2 times pi times the radius!'"
  )
  answerSign = input()
  if answerSign == '157':
    print(
      'Correct! You may pass through. By the way, pi is very important because it is used for measurements and can be very helpful in various topics! '
    )
    print()
    time.sleep(2.8)
    print('You see light up ahead!')

    if trainerAcePokemon == 'Pi-Mon':
      trainerAceMoves = ['Leaf Edge', 'Leaf Swirl', 'Scratch']
    elif trainerAcePokemon == 'Radiuseal':
      trainerAceMoves = ['Water Bubble', 'Fin Slap', 'Aqua Step']

    elif trainerAcePokemon == 'SirCumference':
      trainerAceMoves = ['Fire Breath', 'Flame Tail', 'Scratch']

    poke1 = 'Pikachu'
    global userHealth
    userHealth = 25
    weedleHealth = 25
    scratch = 'SCRATCH'
    quickAttack = 'QUICK ATTACK'
    thunderShock = 'THUNDER SHOCK'
    tackle = 'TACKLE'

    preEngageFight = input(
      'Would you like to go towards the light? Yes or no? ')
    engageFight = preEngageFight.lower()
    if engageFight == 'yes':
      print('You see a person ahead of you')
      time.sleep(2)
      print("They come towards you!")
      print()
      time.sleep(3)
      print("""
      
      Trainer Ace:

      My name's Ace and I'm sure I'll beat you in a pokemon battle!
      
      """)
      print()
      time.sleep(3)
      wildPokemon = []
      print('Trainer Ace: Let\'s go,', trainerAcePokemon + '!')
      time.sleep(1)
      print(trainerAcePokemon + ': ')
      time.sleep(1)
      print('Health:', weedleHealth)
      time.sleep(2)
      print()
      print('''Your Pokemon:
      ''', pokemon)
      pokemonDecisionBefore = input("What pokemon will you like to choose? ")

      pokemonDecision = pokemonDecisionBefore.upper()

      if pokemonDecision == pokemon:
        print()
        time.sleep(1.5)
        print(pokemon)
        time.sleep(1)
        userHealth = str(userHealth)
        print('Health:', userHealth)
        time.sleep(2)
        print()

        while weedleHealth > 0:
          weedleDamage = random.randint(1, 15)
          userDamage = random.randint(5, 10)
          decision = input('''What move would you like to use?
          Option 1: Tackle
          Option 2: Quick Attack
          Option 3: Thunder Shock
          Option 4: Scratch
          (Input a number for the move you want to use.): ''')
          print()
          if decision == '1' or decision == 'tackle' or decision == 'Tackle':
            print('User used', tackle + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
            print('User used ' + quickAttack + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
            print('User used', thunderShock + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '4' or decision == 'scratch' or decision == 'Scratch':
            print('User used ' + scratch + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage
            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

      else:
        print("You did not select a pokemon and got jumped by a weedle.")
        print("""
      
        GAME OVER
      
        """)

    else:
      print(
        "The developers were too lazy to program so you're gonna go towards the light either way!"
      )
      print('You see a person ahead of you')
      time.sleep(2)
      print("They come towards you!")
      print()
      time.sleep(3)
      print("""
      
      Trainer Ace:

      My name's Ace and I'm sure I'll beat you in a pokemon battle!
      
      """)
      print()
      time.sleep(3)
      wildPokemon = []
      print('Trainer Ace: Let\'s go,', trainerAcePokemon + '!')
      time.sleep(1)
      print(trainerAcePokemon + ': ')
      time.sleep(1)
      print('Health:', weedleHealth)
      time.sleep(2)
      print()
      print('''Your Pokemon:
      ''', pokemon)
      pokemonDecisionBefore = input("What pokemon will you like to choose? ")

      pokemonDecision = pokemonDecisionBefore.upper()

      if pokemonDecision == pokemon:
        print()
        time.sleep(1.5)
        print(pokemon)
        time.sleep(1)
        userHealth = str(userHealth)
        print('Health:', userHealth)
        time.sleep(2)
        print()

        while weedleHealth > 0:
          weedleDamage = random.randint(1, 15)
          userDamage = random.randint(5, 10)
          decision = input('''What move would you like to use?
          Option 1: Tackle
          Option 2: Quick Attack
          Option 3: Thunder Shock
          Option 4: Scratch
          (Input a number for the move you want to use.): ''')
          print()
          if decision == '1' or decision == 'tackle' or decision == 'Tackle':
            print('User used', tackle + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
            print('User used ' + quickAttack + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
            print('User used', thunderShock + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage

            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

          if decision == '4' or decision == 'scratch' or decision == 'Scratch':
            print('User used ' + scratch + '!')
            time.sleep(2)
            print("It did,", userDamage, "points of damage!")
            time.sleep(2)
            weedleHealth = weedleHealth - userDamage
            if weedleHealth > 0:
              print("Trainer Ace's", trainerAcePokemon, " is now at",
                    weedleHealth, "health!")

              time.sleep(2)
              print()
              print('Trainer Ace\'s', trainerAcePokemon, 'used',
                    random.choice(trainerAceMoves))
              time.sleep(2)
              weedleDamage = str(weedleDamage)
              print('It did', weedleDamage, 'damage!')
              userHealth = int(userHealth)
              weedleDamage = int(weedleDamage)
              userHealth = userHealth - weedleDamage
              time.sleep(2)
              if userHealth == 0 or userHealth < 0:
                print("Your Pokemon has DIED")
                print("GAME OVER")
                break
              else:
                userHealth = str(userHealth)
                print(pokemon, 'is now at ' + userHealth + ' health!')
                userHealth = int(userHealth)

            else:
              print("Trainer Ace has been defeated!")
              print("User has gained 14 experience!")
              print("""
              Trainer Ace:
              
              I'm Flame Fist Ace!
              And don't you forget it!
              Gosh, this feels like a punch in the stomach..
              Here's 10 coins for beating me.
              """)
              break

      else:
        print("You did not select a pokemon and got jumped by a weedle.")
        print("""
      
        GAME OVER
      
        """)

  if answerSign != '157':
    time.sleep(2)
    print('Wrong.')
    time.sleep(2)
    print('GAME OVER')
    time.sleep(1)
    print('Restart the game to try again!')
    print()
    time.sleep(1)
    quit()

  elif answerSign == "itsacheatcode!":
    print("How you know dis??", '157')


def leftBattle():
  print()
  time.sleep(1)
  print(
    "Irrational numbers came up in Ms. Ealey's class when we were doing problems with quadratic formula. Sometimes, we would get answers such as radical 3, which would end up as an irrational number when simplified!"
  )
  time.sleep(5.5)
  print()
  print("Uh oh! You see a kid being harassed by a wild CHOPPER!")
  kidSave = input('Would you like to help the kid? Yes or no? ')
  kidSave.lower()
  if kidSave == 'yes':
    print()
    chopperMoves = ['Rumble Boost', 'Can We Get Much Higher', 'Tackle']
    poke1 = 'Pikachu'
    global userHealth
    userHealth = 25
    weedleHealth = 20
    scratch = 'SCRATCH'
    quickAttack = 'QUICK ATTACK'
    thunderShock = 'THUNDER SHOCK'
    tackle = 'TACKLE'
    print('Wild POKEMON has been encountered!')
    time.sleep(2)
    print()
    wildPokemon = []
    print('Wild CHOPPER:')
    time.sleep(1)
    print('Health:', weedleHealth)
    time.sleep(2)
    print()
    print('''Your Pokemon:
    ''', pokemon)
    pokemonDecisionBefore = input("What pokemon will you like to choose? ")

    pokemonDecision = pokemonDecisionBefore.upper()

    if pokemonDecision == pokemon:
      print()
      time.sleep(1.5)
      print(pokemon)
      time.sleep(1)
      userHealth = str(userHealth)
      print('Health:', userHealth)
      time.sleep(2)
      print()

      while weedleHealth > 0:
        weedleDamage = random.randint(1, 10)
        userDamage = random.randint(5, 15)
        decision = input('''What move would you like to use?
        Option 1: Tackle
        Option 2: Quick Attack
        Option 3: Thunder Shock
        Option 4: Scratch
        (Input a number for the move you want to use.): ''')
        print()
        if decision == '1' or decision == 'tackle' or decision == 'Tackle':
          print('User used', tackle + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.randint(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
          print('User used ' + quickAttack + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
          print('User used', thunderShock + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '4' or decision == 'scratch' or decision == 'Scratch':
          print('User used ' + scratch + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage
          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

  else:
    chopperMoves = ['Poison Sting', 'Bug Bite', 'String Shot']
    poke1 = 'Pikachu'
    userHealth = 25
    weedleHealth = 20
    scratch = 'SCRATCH'
    quickAttack = 'QUICK ATTACK'
    thunderShock = 'THUNDER SHOCK'
    tackle = 'TACKLE'
    print()
    print("Too bad, you're gonna do it anways!")
    time.sleep(2)
    print('Wild POKEMON has been encountered!')
    time.sleep(2)
    print()
    wildPokemon = []
    print('Wild CHOPPER:')
    time.sleep(1)
    print('Health:', weedleHealth)
    time.sleep(2)
    print()
    print('''Your Pokemon:
    ''', pokemon)
    pokemonDecisionBefore = input("What pokemon will you like to choose? ")

    pokemonDecision = pokemonDecisionBefore.upper()

    if pokemonDecision == pokemon:
      print()
      time.sleep(1.5)
      print(pokemon)
      time.sleep(1)
      userHealth = str(userHealth)
      print('Health:', userHealth)
      time.sleep(2)
      print()

      decision = input('''What move would you like to use?
      Option 1: Tackle
      Option 2: Quick Attack
      Option 3: Thunder Shock
      Option 4: Scratch
      (Input a number for the move you want to use.): ''')
      print()

      while weedleHealth > 0:
        weedleDamage = random.randint(1, 10)
        userDamage = random.randint(5, 15)
        decision = input('''What move would you like to use?
          Option 1: Tackle
          Option 2: Quick Attack
          Option 3: Thunder Shock
          Option 4: Scratch
          (Input a number for the move you want to use.): ''')
        print()
        if decision == '1' or decision == 'tackle' or decision == 'Tackle':
          print('User used', tackle + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '2' or decision == 'quick attack' or decision == 'Quick attack' or decision == 'Quick Attack':
          print('User used ' + quickAttack + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '3' or decision == 'thunder shock' or decision == 'Thunder shock' or decision == 'Thunder Shock':
          print('User used', thunderShock + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage

          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break

        if decision == '4' or decision == 'scratch' or decision == 'Scratch':
          print('User used ' + scratch + '!')
          time.sleep(2)
          print("It did,", userDamage, "points of damage!")
          time.sleep(2)
          weedleHealth = weedleHealth - userDamage
          if weedleHealth > 0:
            print("The wild CHOPPER is now at", weedleHealth, "health!")

            time.sleep(2)
            print()
            print('Wild CHOPPER used', random.choice(chopperMoves))
            time.sleep(2)
            weedleDamage = str(weedleDamage)
            print('It did', weedleDamage, 'damage!')
            userHealth = int(userHealth)
            weedleDamage = int(weedleDamage)
            userHealth = userHealth - weedleDamage
            time.sleep(2)
            if userHealth == 0 or userHealth < 0:
              print("Your Pokemon has DIED")
              print("GAME OVER")
              break
            else:
              userHealth = str(userHealth)
              print(pokemon, 'is now at ' + userHealth + ' health!')

          else:
            print("Wild CHOPPER has fainted!")
            print("User has gained 14 experience!")
            break


if directionDecisionLowered == 'right':
  rightBattle()
  print()
  time.sleep(1)
  print('Congrats! Now on with your adventure!')
  time.sleep(2)
  print("You go forward a bit!")
  leftBattle()
  time.sleep(1)
  print("Congrats on beating the second stage!")
  print("Now you move on to the third stage!")
  trainerBattle()
  time.sleep(2)
  print(
    'Congratulations on beating this game! We can see that you and your pokemon have grown a deep connection. We wish you the best of luck on your journeys!'
  )
  time.sleep(1.4)
  print('THE END')
  quit

if directionDecisionLowered == 'left':
  leftBattle()
  time.sleep(1)
  print()
  print('Congratulations on winning your battle!')
  print('Now on with your adventure!')
  trainerBattle()
  time.sleep(2)
  print()
  print(
    'Congratulations on beating this game! We can see that you and your pokemon have grown a deep connection. We wish you the best of luck on your journeys!'
  )
  time.sleep(1.4)
  print('THE END')
  quit

if directionDecisionLowered == 'forward':
  trainerBattle()
  print()
  time.sleep(2)
  print('Congrats on winning your battle!')
  time.sleep(1.3)
  print('Now on with your adventure!')
  print()
  rightBattle()
  print()
  time.sleep(1.3)
  print('Onto your final stage!')
  print('Good luck!')
  leftBattle()
  print(
    'Congratulations on beating this game! We can see that you and your pokemon have grown a deep connection. We wish you the best of luck on your journeys!'
  )
  time.sleep(1.4)
  print('THE END')
  quit
