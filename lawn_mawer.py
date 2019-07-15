#!/usr/bin/python3
# encoding: utf-8

from enum import Enum

# This class is created for factorize code related to authorised actions
class Action (Enum):
    LEFT  = 'G'
    RIGHT = 'D'
    MOVE  = 'A'
    
    # Check if a given string contains only authorised actions
    def validate_actions (actions):
        valid = True
        authorized_action = [a.value for a in list(Action)]
        i =0
        while valid == True and i < len(actions):
                if actions[i] not in authorized_action:
                    valid = False
                i+=1
        return valid

# This class is created for factorize code related to directions
 class Direction(Enum):
    NORTH  ='N'
    EAST   ='E'
    SOUTH  ='S'
    WEST   ='O'
    
    def turn_right (self):
        return self.__change_direction(1)
    
    def turn_left (self):
        return self.__change_direction(-1)

    # Switch to another direction according to a given step
    def __change_direction(self, step):
        directions = [d.value for d in list(Direction)]
        current_index = directions.index(self.value)
        new_index = (current_index + step) % len(directions)
        return self.__class__(directions[new_index])
    
    # Check if a string contains only authorised directions
    def validate_direction (value):
        valid= True
        authorised_directions = [d.value for d in list (Direction)]
        if not value in authorised_directions:
            valid = False
        return valid
    
   # This class reprensents the position (x,y)
   class Position:
    DEFAULTX = 0 # x= 0 by default
    DEFAULTY = 0 # y= 0 by default
            
    def __init__(self,x,y):
        self.x= x
        self.y =y
       
    # Check if a position (x,y) is inside a given rectangular surfaces (x,y) between (DEFAULTX,DEFAULTY) and (limit.x,limit.y)
    def validate_position (self,limit):
        valid = False
        if self.DEFAULTX <= self.x <= limit.x and self.DEFAULTY <= self.y <= limit.y :
            valid = True
        return valid
    
    # Move according to a given direction
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
    
     # Chech if a position p is of type (int,int)
    def is_int (self):
        try:
            self.x= int(self.x)
            self.y= int(self.y)
            return True
        except:
            return False
            pass

# The following class represents a lawnmower
class LawnMower:
    "this class represents a lawnMower"
    def __init__ (self,position,direction):
        self.position = position
        self.direction = direction 
