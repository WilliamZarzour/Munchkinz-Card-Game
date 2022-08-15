import pyCardDeck
import random
from cards import GearCard

class RatonaStick(GearCard):
    '''Gear object called Rat on a Stick'''

    def __init__(self):
        super.__init__("Rat on a Stick","right hand", 1, 0, False)

    #a player must choose to activate the gear ability or use it during the combat phase 
    # this target is a monster not a player
    def gear_ability(self,target):
        if target.monster_level <= 8:
            player_choice = input("""You may discard this item for an automatic escape from any monster of level 8 or below
            Would you like to discard for an automatic escape?
            Please enter: yes (y) or no (n): """
            ).strip().lower()

           #might be better to use a flag here not sure 
            while player_choice != "yes" or player_choice != "no"  or player_choice != "n"  or player_choice != "y":
                player_choice = input("You entered an invalid input. Please enter: yes (y) or no (n): ").strip().lower()

                if player_choice  == "yes" or player_choice == "no"  or player_choice == "n"  or player_choice == "y":
                    #target escapes and Combat ends (see .escape and .combat end)
                    break

class HornyHelmet(GearCard):
    '''Gear object called Horny Helmet'''

    def __init__(self):
        super.__init__("Horny Helmet","headgear", 1, 600)

    #this function is always active in every phase of the game
    def gear_passive(self,target):
        if target.race == "Elf":
            self.attack_bonus = 3


class TubaofCharm(GearCard):
    '''Gear object called Tuba of Charm'''

    def __init__(self):
        super.__init__("Tuba of Charm","right hand", 0, 300, True)

    #a player must choose to activate the gear ability or use it during the combat phase
    def gear_ability(self,target):
         target.run_away_roll += 3
         #if runaway works get +1 (face down) treasure
         pass

class SandalsofProtection(GearCard):
    '''Gear object called Sandals of Protection'''

    def __init__(self):
        super.__init__("Sandals of Protection","boots", 0, 700)

    #a player must choose to activate the gear ability or use it during the combat phase
    def gear_passive(self,target):
         #if target.draws curse card (during KDD phase) Curse has no effect
         pass

class BootsofRunningReallyFast(GearCard):
    '''Gear object called Boots of Running Really Fast'''

    def __init__(self):
        super.__init__("Boots of Running Really Fast","boots", 0, 400)

    #a player must choose to activate the gear ability or use it during the combat phase
    def gear_passive(self,target):
        target.run_away_roll += 2

class ReallyImpressiveTitle(GearCard):
    '''Gear object called really Impressive Title'''

    def __init__(self):
        super.__init__("Really Impressive Title","misc", 0, 0)

    #This should happen once the player attaches the card (once it is in play)
    def gear_action(self,target):
        print("You have been awarded a title! Example (The Great for Alexander the Great)", end=" ")
        target.name += input("Your title will be attacked at the end of your name. Please enter your title:")