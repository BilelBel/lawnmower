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
