from enum import Enum
import behavior
import _GoToPoint_
import rospy
from utils.functions import *
from utils.geometry import *
from utils.config import *
from math import *

class Rectangle(behavior.Behavior):

    class State(Enum):
        BOT_STATIC = 1
        BOT_RECEIVE = 2
        BOT_PASSING = 3
        BOT_ALLIGNING = 4
    
    def __init__(self, continuous = False):

        super(Rectangle,self).__init__()

        self.name = "Rectangle"
        
        self.behavior_failed = False

        self.add_state(Rectangle.State.BOT_STATIC,
            behavior.Behavior.State.running)

        self.add_state(Rectangle.State.BOT_RECEIVE,
            behavior.Behavior.State.running)

        self.add_state(Rectangle.State.BOT_PASSING,
            behavior.Behavior.State.running)

        self.add_state(Rectangle.State.BOT_ALLIGNING,
            behavior.Behavior.State.running)
        
        self.add_transition(behavior.Behavior.State.start,
            Rectangle.State.BOT_STATIC,lambda: True,'initialize')
        
        self.add_transition(Rectangle.State.BOT_STATIC,
            Rectangle.State.BOT_RECEIVE,lambda: ,'receive_pass')
        
        self.add_transition(Rectangle.State.BOT_STATIC,
            Rectangle.State.BOT_PASSING,lambda: ,'pass_to_next')

        self.add_transition(Rectangle.State.BOT_STATIC,
            Rectangle.State.BOT_ALLIGNING,lambda: ,'move_to_pos')
        
        self.add_transition(Rectangle.State.BOT_RECEIVE,
            Rectangle.State.BOT_STATIC,lambda: ,'pass_received')
        
        self.add_transition(Rectangle.State.BOT_PASSING,
            Rectangle.State.BOT_STATIC,lambda: ,'ball_passed')
        
        self.add_transition(Rectangle.State.BOT_ALLIGNING,
            Rectangle.State.BOT_STATIC,lambda: ,'at_pos')

    def add_kub(self, kub, pos, previous, target):
        self.kub = kub
        self.pos = pos
        self.previous = previous
        self.target = target
    
