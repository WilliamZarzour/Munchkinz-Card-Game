import pyCardDeck
import random
from cards import MonsterCard

class DroolingSlime(MonsterCard):
    '''Monster object called drooling slime'''

    def __init__(self):
        super().__init__("Drooling Slime")
        self.monster_level = 1
        self.treasure = 1
    
    def monster_ability(self,targets):
        '''The passive ability the monster has during combat.'''
        for target in targets:
            if target.race == "elf":
                self.monster_level += 4
                break

    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
            target.subtract_n_levels(1)
            #monster bad stuff (lose lvl and/or footgear)
    
class PlutoniumDragon(MonsterCard):
    '''Monster object called Plutonium Dragon'''

    def __init__(self):
        super().__init__("Plutonium Dragon")
        self.monster_level = 20
        self.treasure = 5
        self.lvl_reward = 2

    def monster_ability(self):
        '''str representing monster's ability'''
        print("Will not pursue anyone of Level 5 or below")

    def targets_attempt_escape(self, targets):
        for target in targets:
            if target.character_level <= 5:
                target.base_run_away = 6
    
    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
                target.death()
                print(f"You are roasted and eaten.")       

class Bullrog(MonsterCard):
    '''Object is a monster called bullrog'''

    def __init__(self):
        super().__init__("Bullrog")
        self.monster_level = 18
        self.treasure = 5
        self.lvl_reward = 2

    def monster_ability(self):
        '''str representing monster's ability'''
        print("Will not pursue anyone of Level 4 or below")

    def targets_attempt_escape(self, targets):
        for target in targets:
            if target.character_level <= 4:
                target.base_run_away = 6  

    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
            target.death()
            print(f"You are flayed to death.")       

class StonedGolem(MonsterCard):
    '''object is a monser called stonedgolem'''
    def __init__(self):
        super().__init__("Stoned Golem")
        self.monster_level = 14
        self.treasure = 4
        self.lvl_reward = 2
    
    def monster_ability(self,targets):
        '''halflings must fight, others get to choose'''
        for target in targets:
            if target.race == "halfling":
                target.combat(self)
                break
            else:
                while flag == False:
                    x = input("Do you want to fight the Stoned Golem: Y/N").lower().strip()
                    if x=="y" or "yes":
                        flag = True
                        target.combat(self)
                    elif x=="n" or "no":
                        flag = True
                        print("You skip combat wave and walk by")
                        target.escape()
                    else:
                        x = input("Your input was not valid. Please enter yes(y) or no(n):").lower().strip()

    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
            target.death()
            print("He has the munchies. He eats you. You're dead.")      

class FlyingFrogs(MonsterCard):
    '''object is a monser called FlyingFrogs'''

    def __init__(self):
        super().__init__("Flying Frogs")
        self.monster_level = 2
        self.treasure = 1

    def monster_ability(self,targets):
        for target in targets:
            target.run_away_roll -= 1

    def bad_stuff(self,targets):
        for target in targets:
                print("They bite! ",end="")
                target.subtract_n_levels(2)

class LameGoblin(MonsterCard):
    '''object is a monster called Lame Goblin'''

    def __init__(self):
        super().__init__("Lame Goblin")
        self.monster_level = 1
        self.treasure = 1

    def monster_ability(self,targets):
        for target in targets:
            target.run_away_roll += 1

    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
            print(f"he whacks you with his crutch. ", end="")
            target.subtract_n_levels(1)
        
class KingTut(MonsterCard):
    '''object is a monser called King Tut'''
    def __init__(self):
        super().__init__("King Tut")
        self.monster_level = 1
        self.treasure = 4
        self.trait = "Undead"
    
    def monster_ability(self,targets):
        print("Will not pursue anyone of lvl 3 or below. Higher-level characters lose 2 levels even if they escape.")

    def targets_attempt_escape(self, targets):
        for target in targets:
            if target.level <= 3:
                targets.escape() #potentially a remove() could work
            else:
                target.subtract_n_levels(2)
    
    def bad_stuff(self, targets):
        #for target in targets:
            #target. lose all items
            #target. lose all cards in hand
        pass

class UndeadHorse(MonsterCard):
    '''object is a monster called undead horse'''

    def __init__(self):
        super().__init__("Undead Horse")
        self.monster_level = 4
        self.treasure = 2
        self.trait = "Undead"
    
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Dwarf":
                 self.monster_level += 5
                 break

    def bad_stuff(self, targets):
        for target in targets:
            print("Kicks, bites, and smells awful.")
            target.subtract_n_levels(2)    

class MaulRat(MonsterCard):
    '''Object is a monster called maul rat'''

    def __init__(self):
        super().__init__("Maul Rat")
        self.monster_level = 1
        self.treasure = 1
        
    def monster_ability(self,targets):
        for target in targets:
            if target.skill == "Cleric":
                 self.monster_level += 3
                 break

    def bad_stuff(self, targets):
        for target in targets:
            print("Kicks, bites, and smells awful.")
            target.subtract_n_levels(1)     
            
class Ghoulfiends(MonsterCard):
    '''Object is a monster called GhoulFiends'''

    def __init__(self):
        super().__init__("GhoulFiends")
        self.monster_level = 8
        self.treasure = 2

 # andre 
    def monster_ability(self,targets):
        #for target in targets:
            #target.character_combat_score - target.modifers
        #restrict modifier/item cards to be played. (curses are fine i think)
        pass

    def badstuff(self,targets,players):
        #for target in targets:
            #target.set_level_n(min(players.character_level))
        pass

class Squidzilla(MonsterCard):
    '''Object is a monster called Squidzilla '''

    def __init__(self):
        super().__init__("Squidzilla")
        self.monster_level = 2
        self.treasure = 4
        self.lvl_reward = 2
        
    def monster_ability(self,targets):
    
        print("Slimy!, Elves are at -4! Will not pursue anyone of level 4 or below except elves.")
        for target in targets:
            if target.race == "Elf":
                 target.character_combat_score -= 4

        for target in targets:
            if target.character_level <= 4:
                target.base_run_away = 6
            elif target.race == "Elf":
                target.base_run_away = -7 #-7 ensures a failed escape

    def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        for target in targets:
            target.death()
            print("You are grabbed, slimed, crushed, and gobbled. You are dead, dead, dead. Any questions?")
        
class NetTroll(MonsterCard):
    '''object is a monster called Net Troll'''
    def __init__(self):
        super().__init__("NetTroll")
        self.monster_level =10
        self.treasure = 3

    #Passive (nothing)
    # BadStuff Screws up game balance lests the player with the highest lvl take an item from each of you. (CHANGE)

class LargeAngryChichen(MonsterCard):
    def __init__(self):
        super().__init__("Large Angry Chicken")
        self.monster_level = 2
        self.treasure = 1

    #Passive gain an extra lvl if you beat it with fire or flame
    # Lose a level
    def bad_stuff(self, targets):
        for target in targets:
            print("Very painful pecking.")
            target.subtract_n_levels(1)
        
class BigChungus(MonsterCard):
    def __init__(self):
        super().__init__("Big Chungus")
        self.monster_level = 20
        self.treasure = 1

    def monster_ability(self,targets):
        for target in targets:
            if target.level < 5:
                print("$im BigChungus")
                targets.remove(target)

    # Passive posts a gif of bug chungus players below lvl 5 win
    def bad_stuff(self, targets):
        for target in targets:
            print("Big Chungus twerks on your face.")
            target.subtract_n_levels(2)
        
class Null(MonsterCard):
    def __init__(self):
        super().__init__("Null")
        self.monster_level = 1
        self.treasure = 1

    # Passive: cannot be outrun
    # BS: Discard armour and all items worn below the waste

class MrBones(MonsterCard):
    def __init__(self):
        super().__init__("Mr. Bones")
        self.monster_level = 2
        self.treasure = 1
        self.trait = "Undead"
    
    def monster_ability(self):
        print("If you must flee, you lose a level even if you escape!")

    def targets_attempt_escape(self, targets):
        for target in targets:
            target.subtract_n_levels(1)
        

    def bad_stuff(self, targets):
        for target in targets:
            print("His bony touch makes you uncomfortable")
            target.subtract_n_levels(2)
        
class Crabs(MonsterCard):
    def __init__(self):
        super().__init__("Crabs")
        self.monster_level = 1
        self.treasure = 1
    
    # Passive: cannot be outrun
    # BS: Discard armour and all items worn below the waste

class FaceSucker(MonsterCard):
    def __init__(self):
        super().__init__("Face Sucker")
        self.monster_level = 8
        self.treasure = 1

    # Passive: +6 against elves
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Elf":
                 self.monster_level += 5
                 break
    # BS: lose headgear if no headgear lose level

class WannabeVampire(MonsterCard):
    def __init__(self):
        super().__init__("Wannabe Vampire")
        self.monster_level = 12
        self.treasure = 3
        
    # P: If cleric then promt do u want to chase vampire away
        #if yes then take treasure but no lvl increase
        #if no then combat

    def bad_stuff(self, targets):
        for target in targets:
            print("Blocks the door and tells you about his character.")
            target.subtract_n_levels(3)
        
class Hippogriff(MonsterCard):
    def __init__(self):
        super().__init__("Hippogriff")
        self.monster_level = 16
        self.treasure = 4
        self.lvl_reward = 2

    # Passive: will not pursue lvl 3 or below
    # BS: MYSC

class Amazon(MonsterCard):
    def __init__(self):
        super().__init__("Amazon")
        self.monster_level = 8
        self.treasure = 2

    # Passive: Will not attack females (just gives them 1 treasure)
    # BS: lose class if no class lose 3 lvls

class FloatingNose(MonsterCard):
    def __init__(self):
        super().__init__("Floating Nose")
        self.monster_level = 10
        self.treasure = 3

    # Passive: can be bribe(change??)
    # BS: If you lose you cannot flee, lose 3 lvls
    def bad_stuff(self, targets):
        for target in targets:
            print("It can sniff you out anywhere. There is no escape. Nothing will help you.")
            target.subtract_n_levels(3)
        
class Harpies(MonsterCard):
    def __init__(self):
        super().__init__("Harpies")
        self.monster_level = 4
        self.treasure = 2

    # Passive: +5 against wizards
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Wizards":
                 self.monster_level += 5
                 break
    
    def bad_stuff(self, targets):
        for target in targets:
            print("Their music was definitly not electric.")
            target.subtract_n_levels(2)
        
class PitBull(MonsterCard):
    def __init__(self):
        super().__init__("Pit Bull")
        self.monster_level = 2
        self.treasure = 1

    # Passive: if you cant beat it you can drop and item (automatic escape) by dropping any wand/pole/or staff]
    def bad_stuff(self, targets):
        for target in targets:
            print("Fang marks in your butt.")
            target.subtract_n_levels(2)
        
class Bigfoot(MonsterCard):
    def __init__(self):
        super().__init__("Bigfoot")
        self.monster_level = 12
        self.treasure = 3

    # Passive: +3 against Haflings and Dwarves
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Halfling" or target.race == "Dwarf":
                self.monster_level += 3
                break
    # BS: lose headgear

class Platycore(MonsterCard):
    def __init__(self):
        super().__init__("Platycore")
        self.monster_level = 6
        self.treasure = 2

    #P: +6 against wizards
    def monster_ability(self,targets):
        for target in targets:
            if target.skill == "Wizards":
                 self.monster_level += 5
                 break
    #BS: Discard whole hand or Lose 2 lvls

class TongueDemon(MonsterCard):
    def __init__(self):
        super().__init__("Tongue Demon")
        self.monster_level = 12
        self.treasure = 3

    # Passive: +4 against clerics and
    ###### You must discard 1 item before combat
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Dwarf":
                 self.monster_level += 5
                 break

    # BS: lose 2 lvls if elf lose 3
    def bad_stuff(self, targets):
        for target in targets:
            print("A really disgusting kiss costs you levels.")
            target.subtract_n_levels(2)
        
class PukaChu(MonsterCard):
    def __init__(self):
        super().__init__("PukaChu")
        self.monster_level = 6
        self.treasure = 2

    # Passive: Gain an extra lvl if you defeat without help or bonuses
    # BS: discard hand

class GelatinousOctahedron(MonsterCard):
    def __init__(self):
        super().__init__("Gelatinous Octahedron")
        self.monster_level = 2
        self.treasure = 1

    # Passive: +1 to runaway
    # BS: lose all big items

class Leperchaun(MonsterCard):
    def __init__(self):
        super().__init__("Leperchaun")
        self.monster_level = 4
        self.treasure = 2

    # Passive: +5 against elves
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Elf":
                 self.monster_level += 5
                 break
    # BS: lose 2 items (usually chose by other players)

class PottedPlant(MonsterCard):
    def __init__(self):
        super().__init__("Potted Plant")
        self.monster_level = 1
        self.treasure = 1

    #Passive: Elves draw an extra tresure
    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Elf":
                 self.treasure += 1
                 break

    #done excape is auto
    
class WightBrothers(MonsterCard):
    def __init__(self):
        super().__init__("Wight Brothers")
        self.monster_level = 16
        self.treasure = 4
        self.trait = "Undead"
        self.lvl_reward = 2

    def monster_ability(self):
        print("Will not pursue anyone of Level 3 or below. Higher level characters lose 2 levels, even if they escape")

    def targets_attempt_escape(self, targets):
        for target in targets:
            if target.level > 3: 
                target.subtract_n_levels(2)
            else:
                target.base_run_away = 6

    def bad_stuff(self, targets):
        for target in targets:
            print("You lost the fight, a mistake was made, you fought the wight, a debt must be paid.")
            target.set_level_n(1)
        
class ThousandOrcs(MonsterCard):
    def __init__(self):
        super().__init__("3,872 Orcs")
        self.monster_level = 10
        self.treasure = 3

    def monster_ability(self,targets):
        for target in targets:
            if target.race == "Dwarf":
                 self.monster_level += 6
                 break

    # BS: role a die on 2 or less you die
    def bad_stuff(self,targets):
        for target in targets:
            dice_roll = random.randint(1,6)
            if dice_roll <= 2:
                target.death()
                print("The army of 3,872 Orcs stomp you to death")
            else:
                print("3,871 orcs stomp you but one of them feels bad and mends your fatal wounds.")
                target.subtract_n_levels(dice_roll)      

class Gazebo(MonsterCard):

    def __init__(self):
        super().__init__("Gazebo")
        self.monster_level = 8
        self.treasure = 2

    # Passive: You must face gazebo alone
    def bad_stuff(self,targets):
        for target in targets:
            print("You are trapped in the gazebo as it laughs maniacally")
            target.subtract_n_levels(3)       

class Reaver(MonsterCard):

    def __init__(self):
        super().__init__("Reavers")
        self.monster_level = 18
        self.treasure = 3

    # Passive: Gain an extra treasure for each person that helps you.

    def bad_stuff(self,targets):
        for target in targets:
            target.death()
            print("Legends say, they rape you to death, eat your flesh, and sew your skin into their clothing – and if you're very, very lucky, they'll do it in that order")

class SnailsOnSpeed(MonsterCard):
    '''object is a monser called Snails on Speed'''

    def __init__(self):
        super().__init__("Snails on Speed")
        self.monster_level = 4
        self.treasure = 2

    def monster_ability(self,targets):
        for target in targets:
            target.run_away_roll -= 2

    def bad_stuff(self,targets):
        for target in targets:
                print("They they steal your treasure. Roll a dice and lose that many items or cards in your hand players choice. ",end="")
                dice_roll = random.randint(1,6)
                player_choice = int(input(f"Please enter 1 or 2 for your choice:\n1. Lose Items\n2.Lose Cards").strip())
                if player_choice == 1: 
                    print("Remove items")
                elif player_choice == 2:
                    print("Remove cards")
                while player_choice != 1 or player_choice !=2:
                    player_choice = int(input(f"Invalid input. Please only integers 1 or 2 for your choice:\n1. Lose Items\n2.Lose Cards").strip())
                pass

class UnspeakablyAwfulIndescribableHorror:
   '''Object is a monster called Unspeakably Awful Indescribable Horror'''
   def __init__(self):
        super().__init__("Unspeakably Awful Indescribable Horror")
        self.monster_level = 14
        self.treasure = 4
    
   def monster_ability(self,targets):
        '''str representing monster's ability'''
        print("+4 Against Warriors")
        for target in targets:
            if target.skill == "Warrior":
                self.monster_level += 5
                break

   def bad_stuff(self,targets):
        '''The consequences for losing to the monster. '''
        print("Unspeakably awful death for anyone but a Wizard. A Wizard merely loses their powers - discard the wizard card.")
        for target in targets:
            if target.skill == "Wizard":
                target.change_skill("Human")
            else:
                target.death()