#!/usr/bin/python3
# encoding: utf-8

from enum import Enum

class Action (Enum):
    LEFT  = 'G'
    RIGHT = 'D'
    MOVE  = 'A'
    
    def validate_actions (actions):
        valid = True
        authorized_action = [a.value for a in list(Action)]
        i =0
        while valid == True and i < len(actions):
                if actions[i] not in authorized_action:
                    valid = False
                i+=1
        return valid

 class Direction(Enum):
    NORTH  ='N'
    EAST   ='E'
    SOUTH  ='S'
    WEST   ='O'
    
    def turn_right (self):
        return self.__change_direction(1)
    
    def turn_left (self):
        return self.__change_direction(-1)

    def __change_direction(self, step):
        directions = [d.value for d in list(Direction)]
        current_index = directions.index(self.value)
        new_index = (current_index + step) % len(directions)
        return self.__class__(directions[new_index])
    
    def validate_direction (value):
        valid= True
        authorised_directions = [d.value for d in list (Direction)]
        if not value in authorised_directions:
            valid = False
        return valid
    
    
   class Position:
    DEFAULTX = 0
    DEFAULTY = 0
            
    def __init__(self,x,y):
        self.x= x
        self.y =y
        
    
    def move (self,direction,step):
        new_pos = Position(self.x,self.y)
        if direction.value == Direction.NORTH.value:
            new_pos.y +=step
        if direction.value == Direction.EAST.value:
            new_pos.x +=step
        if direction.value == Direction.WEST.value:
            new_pos.x -=step
        if direction.value == Direction.SOUTH.value:
            new_pos.y -=step
        return new_pos
            

