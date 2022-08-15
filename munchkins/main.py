#File Name: main.py
#Description: Munchkins
#Date: 2021-01-05
#Author: William Zarzour
from character import Character
from monster_cards import *
from curse_cards import *
from cards import GearCard
import pyCardDeck

door_deck = pyCardDeck.Deck([
        DroolingSlime(),
        PlutoniumDragon(),
        MaulRat(),
        FlyingFrogs(),
        LoseLevel()
    ],
    True,
    "Door Deck")

#Gearcard(name, gear_type, attack_bonus, gold_value, big=False, allowed=None, disallowed=None):
treasure_deck = pyCardDeck.Deck([
        GearCard("Flaming Armor", "chestplate", 2, 400),
        GearCard("Slimy Armor", "chestplate", 1, 200),
        GearCard("Short Wide Armor", "chestplate", 3, 400, False, allowed="Dwarf"),
        GearCard("2h Huge Rock", "right hand", 3, 0),
        GearCard("Chainsaw of Bloody Dismemberment", "right hand", 3, 600,True),
        GearCard("Leather Armor", "chestplate", 1, 200),
        GearCard("Mithril Armor", "chestplate", 3, 600,True, disallowed="Wizard"),
        GearCard("Pointy Hat of Power", "headgear", 3, 400, False, allowed="Wizard"),
        GearCard("Gentlemen's Club", "right hand", 3, 400, False), #Males only / 1 handed
        GearCard("2h Swiss Army Polearm", "right hand", 4, 600,True, allowed="Human"), #2handed
        GearCard("Boots of Butt-Kicking", "boots", 2, 400, False),
        GearCard("Bad-Ass Bandana","headgear",3,400, False, allowed = "Human"),
        GearCard("Helm of Courage","headgear",1,200, False),
        GearCard("Mace of Sharpness","right hand", 4, 600, False, allowed = "Cleric"),
        GearCard("Rapier of Unfairness","right hand", 3, 600, False, allowed = "Elf"),
        GearCard("Cheese Grater of Peace","right hand",3,400,False, allowed = "Cleric"),
        GearCard("Staff of Napalm","right hand",5,800,False, allowed = "Wizard"),
        GearCard("Dagger of Treachery","right hand",3,400,False, allowed = "Thief"),
        GearCard("Broad Sword","right hand",3,400,False), #females only
        GearCard("Buckler of Swashing","right hand",2,400,False),
        GearCard("Snaky Bastard Sword","right hand",2,400,False),
        GearCard("Hammer of Kneecapping","right hand",4 ,600 ,False , allowed = "Dwarf"),
        GearCard("Eleven-Foot Pole","right hand", 1, 200, False),
        GearCard("2h Bow with Ribbons","right hand",4 , 800, False, allowed = "Elf"),
        GearCard("Shield of Ubiquity","right hand",4, 600, True, allowed = "Warrior"),
        #these are cards that dont take up a gear slot but provide bonuses
        GearCard("Pantyhose of Giant Strength", "misc", 3, 600, False, disallowed = "Warrior"),
        GearCard("Limburger and Anchovy Sandwich" ,"misc", 3, 400, False, allowed = "Halfing"),
        GearCard("Cloak of Obscurity","misc",4, 600, False, allowed = "Thief"),
        GearCard("Stepladder","misc",3, 400, True, allowed = "Halfling"),
        GearCard("Spiky Knees","right hand",1, 200, False),
        GearCard("Singing and Dancing Sword", "misc", 2, 400, False, disallowed = "Thief"),
        
    ],
    True,
    "Treasure Deck")

character_list = [
    Character("Pluto",door_deck),
    Character("Stellar",door_deck),
    Character("Beswin",door_deck)]

door_deck.shuffle()

while True:
    for character in character_list: 
        character.prompt_action()
    #this checks if character lvl is 0 if 0 character is removed because they are dead. 
        for character in character_list:
            if character.character_level <= 0:
                character_list.remove(character)
                