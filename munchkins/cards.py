class BaseCard:
    '''<Card> An object card.'''

    def __init__(self,name): 
        self.name = name
        
    def __str__(self):
        '''<string> representation of the card. helps pythonically'''
        #Return the name of the card + the ability.
        return self.name

    def __repr__(self):
        '''<string> representation of the card. helps pythonically'''
        #representation of the card
        return f"Card type: {type(self)} Card Name: {self.name} Card effect:"

class CurseCard(BaseCard):
    '''An object Curse subclass of <Card>'''
    def __init__(self,name):
        ''''''
        super().__init__(name)
        pass

class MonsterCard(BaseCard):
    '''An object Monster subclass of <Card>'''

    def __init__(self, name):
        '''initializing the attributes of the monster'''
        super().__init__(name)
        self.targets = []
        self.trait = None
        self.lvl_reward = 1
    
    def combat_end(self):
        '''A function that resets the modifiers of players in combat and empties the target list'''
        for target in self.targets:
            target.base_run_away = 0
            #reset modifiers

        self.targets = []
        
    def targets_attempt_escape(self,targets):
        ''''''
        pass

    def bad_stuff(self,targets):
        ''''''
        pass

    def death(self,sources):
        ''''''
        pass
   
class GearCard(BaseCard):
    def __init__(self, name, gear_type, attack_bonus, gold_value, big=False, allowed=None, disallowed=None):
        super().__init__(name)
        self.gear_type = gear_type
        self.attack_bonus = attack_bonus
        self.gold_value = gold_value
        self.big = big
        self.allowed = allowed # Array of class names (strings) or None
        self.disallowed = disallowed