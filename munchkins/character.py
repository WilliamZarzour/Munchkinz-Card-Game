import random
from monster_cards import *
from curse_cards import *
import pyCardDeck

class Character: 
    '''A class that represents a character.'''
 
    def __init__(self, name, door_deck):
        '''name <string> is name of character'''
        self.race = "Human" # Elf, Dwarf, Halfling, Orc
        self.skill = "" #Cleric, Warrior, Thief, Wizard
        self.half_breed = None # Elf, Dwarf, Halfling, Orc, None
        self.super_munchkin = None #Cleric, Warrior, Thief, Wizard, None
        self.traits = [self.race, self.half_breed, self.skill, self.super_munchkin]
        self.character_level = 1
        self.character_combat_score = self.character_level
        self.treasure = 0
        self.name = name
        self.action_dict = {'kick down door':self.kdd,'look for trouble':self.lft,'loot':self.loot,'charity':self.charity}
        self.door_deck = door_deck
        self.base_run_away = 0
        self.gear_dict = {'headgear':None,'chestplate':None,'boots':None,'left hand':None,'right hand':None,'misc':[]}
        self.gold = 0


    def __repr__(self):
        '''return <string> representation of character'''
        return (f'Name: {self.name} Race: {self.race} Skill: {self.skill} Level: {self.character_level} Treasure(s):{self.treasure}')

    def prompt_action(self): 
        '''return <string> a prompt asking for an action'''
        action_key = input(f"{self.name} What is your action: ").strip().lower()
        self.action_dict[action_key]()
    
    def kdd(self):
        '''kick down door, draw a card from the door deck'''
        self.door_deck.shuffle()
        drawn_card = self.door_deck.draw()
        print(f"{self.name} is kicking down the door and drew ",end="" )
        self.door_deck.discard(drawn_card)
        if isinstance(drawn_card,MonsterCard):
            print(f"monster {drawn_card}.")
            self.combat(drawn_card)
        else:
            print(f"{drawn_card}, another type of card.")

    def escape(self):
        '''returns <string> a statement'''

        print("successfully evaded the monster")

    def run_away(self,monster):
        '''determines if player escapes or not 
        returns <string> a statement '''
        #This will need to be done for each individual character
        #this will also need to be done for each individual monster

        monster.targets_attempt_escape([self])
        run_away_roll = random.randint(1,6)
        print(f"{self.name} rolled {run_away_roll} and has a run away modifier of {self.base_run_away} and ", end ="")
        if run_away_roll + self.base_run_away >= 5:
            self.escape()
        else:
            print("failed to escape")
            monster.bad_stuff([self])
        
    #This will become combat() and run the combat function.
    def combat(self,monster):
        '''returns <string> a statement of attack'''
        print(f'{self.name} is in combat with {monster}')
        #place monster abilities here
        if self.character_level < monster.monster_level : 
            print(f"{self.name}'s attack Failed")
            self.run_away(monster)
            #monster.bad_stuff([self])
            #call monster specific badstuff
        else:
            self.add_n_levels(monster.lvl_reward)
            self.draw_treasure(monster.treasure)
            print(f"{self.name}'s the monster was defeated. You leveled up! Gain {monster.treasure} Treasure!")
        monster.combat_end()

    def lft(self):
        '''look for trouble select a monster from your hand to attack
        returns <string> a statement of of looking for trouble'''
        print(f'{self.name} is looking for trouble.')
        #player defines monster
        #player attacks monster
    
    def loot(self): 
        '''returns <string> a statement of looting'''
        print(f'{self.name} is looting the room.')
        #draw 1 card from door deck
    
    def charity(self):
        '''returns <string> a statement of charity'''
        print(f'{self.name} is offering charity.')
        #if hand is larger than 5 give away cards
    
    def add_n_levels(self,n):
        '''returns <int> a integer representing level increase'''
        self.character_level += n
        print(f"{self.name} has gained {n} level(s). {self.name} is now level: {self.character_level}")

    def subtract_n_levels(self,n):
        '''returns <int> an integer representing a level decrease'''
        if self.character_level - n < 1:
            self.character_level = 1
            print(f"{self.name}'s level cannot be lowered to zero. ", end="")
        else:
            self.character_level -= n
            print(f"{self.name} has lost {n} level(s). ", end="")
        print("{self.name} is now level: {self.character_level}")

    def set_level_n(self,n):
        '''returns <int> an integer representing the new level.'''
        self.character_level = n
        print(f"{self.name}'s level has been set to {n}.")
    
    def draw_treasure(self,n):
        '''returns <int> an integer representing an increase in the number of treasures'''
        self.treasure += n
    
    def death(self):
        '''returns <int> an integer representing that a character has died'''
        self.character_level = 0
        print(f"{self.name} has been killed", end=" ")
    
    def change_race(self, race):
        '''returns <str> a string representing that a character's race has changed'''
        self.race = race
        self.update_traits()
        
    def change_skill(self,skill):
        '''returns <str> a string representing that a character's skill has changed'''
        self.skill = skill
        self.update_traits()

    def update_traits(self):
        self.traits = [self.race, self.half_breed, self.skill, self.super_munchkin]

    def search_gear(self):
        '''returns <> representing the treasures you have'''
        armor = print(f'''
        Headgear:{self.headgear}
        Chestplate: {self.chestplate}
        Footgear: {self.footgear}
        Left Hand: {self.left_hand}
        Right Hand: {self.right_hand}
        Miscellaneous: {self.misc}''')

    def check_big_items(self, armors):
        '''returns <str> representing the player is currently carrying a Big item'''
        has_big_item = any(armor.big_item for armor in armors)

        if has_big_item:
            if self.race != "Dwarf":
                print(f"{self.name} already has a big item and can't equip another")
            else:
                print(f"{self.name} is {self.race} and can carry any number of big items")
