#!/usr/bin/python3
# encoding: utf-8

from enum import Enum
import os
import sys

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
    def __init__ (self,position,direction):
        self.position = position
        self.direction = direction 
    
    # Move a lownmower (only if it won't go out of the garden)
    def move (self,limit):
        old_position = self.position
        if self.position.is_int():
            new_position = self.position.move(self.direction,1)
            if new_position.validate_position(limit):
                self.position = new_position
            else:
                self.position = old_position
                
    # Execute a given string actions           
    def execute_actions( self,actions,limit):
        valid = True
        if Action.validate_actions(actions):
            for act in actions:
                if act == Action.MOVE.value:
                    self.move(limit)
                if act == Action.RIGHT.value:
                    self.direction = self.direction.turn_right()
                if act == Action.LEFT.value:
                    self.direction = self.direction.turn_left()
        else:
            valid = False
        return valid
                    
# The following (controler) class represents the fact of mowing a garden                    
class GardinMowing:
    def __init__ (self,gardin_limit,lawnmowers,actions):
        self.limit = gardin_limit
        self.lawnmowers = lawnmowers
        self.actions = actions
        
    #Lauch lawnmowers
    def launch(self): 
        i = 0
        print ("New lawnmowers positions: ")
        for l in self.lawnmowers:
            if l.execute_actions(self.actions [i],self.limit):
                print (l.position.x,l.position.y,l.direction.value)
            else:
                print ("Wrong actions for the lawnmower number", i+1)
            i +=1
            
# Function to parse a given file to lines            
def parse_file_to_lines (file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        lines = [line for line in f.readlines() if line.strip()]
    return lines

# Function to parse a given file to lines  
def parse_file_to_garden_mowing (file_path):
    gadin_mowing = None
    data = parse_file_to_lines(file_path)
    if data is None:
        print (f"Input file {file_path} does not exist")
    else:
        if len(data) % 2 == 1 :
            first_line   = [cordinate for cordinate in data[0].split() ]
            gardin_limit = Position (first_line[0],first_line[1])
            if gardin_limit.is_int():         
                lawn_mowers  = []
                actions      = []
                i = 1
                while  i < len (data):
                    lawn_param = [w for w in data[i].split() ]
                    i+=1
                    action_str = [w for w in data[i].split() ]
                    if len (lawn_param) > 2 and len (action_str) > 0:
                        if Direction.validate_direction (lawn_param[2]):
                            lawn_mower = LawnMower (Position(lawn_param[0],lawn_param[1]),Direction(lawn_param[2]))
                            lawn_mowers.append(lawn_mower)
                            action = action_str[0]
                            actions.append(action) 
                        else:
                            print ("Wrong direction for the lawn mower number ", int (i/2) )
                    i+=1
                gadin_mowing = GardinMowing (gardin_limit,lawn_mowers,actions)
            else:
             print ("Wrong file: Garden coordinates should be of type integer ")   
        else:
            print ("Wrong file: insufficient number of lines")
    return gadin_mowing 

def main(argv):
    garen_mowing = parse_file_to_garden_mowing(argv)
    if garen_mowing is not None:
        garen_mowing.launch()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print ("Missing argument: Input file")
