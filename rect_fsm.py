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
        setup = 1
        static = 2
        receive = 3
        passing = 4
        alligning = 5
    
    def __init__(self, id, next_id, prev_id, pos, continuous = False):

        super(Rectangle,self).__init__()

        self.name = "Rectangle" + str(id)
        self.id = id
        self.next_id = next_id
        self.prev_id = prev_id
        self.pos = pos
        
        self.behavior_failed = False

        for state in Rectangle.State:
            self.add_state(state,behavior.Behavior.State.running)
        
        self.add_transition(behavior.Behavior.State.start, Rectangle.State.setup,
            lambda: True,"initialize")
        
        self.add_transition(Rectangle.State.setup, Rectangle.State.receive,
            lambda: self.prev_has_ball(),"receive_pass")
        self.add_transition(Rectangle.State.setup, Rectangle.State.passing,
            lambda: self.has_ball(),"pass_to_next")
        self.add_transition(Rectangle.State.setup, Rectangle.State.alligning,
            lambda: (not self.prev_has_ball()) and (not self.has_ball()) and (not self.at_pos()),"move_to_pos")
        self.add_transition(Rectangle.State.setup, Rectangle.State.static,
            lambda: (not self.prev_has_ball()) and (not self.has_ball()) and self.at_pos(),"stay_at_pos")
        
        self.add_transition(Rectangle.State.static, Rectangle.State.alligning,
            lambda: (not self.prev_has_ball()) and (not self.has_ball()) and (not self.at_pos()),"allign")
        self.add_transition(Rectangle.State.alligning, Rectangle.State.static,
            lambda: self.at_pos(),"stay")
        self.add_transition(Rectangle.State.static, Rectangle.State.receive,
            lambda: self.prev_has_ball(),"receive")
        self.add_transition(Rectangle.State.static, Rectangle.State.passing,
            lambda: self.has_ball(),"receive")
        self.add_transition(Rectangle.State.receive, Rectangle.State.passing,
            lambda: self.has_ball(),"pass")
        self.add_transition(Rectangle.State.passing, Rectangle.State.alligning,
            lambda: not self.at_pos(),"allign")
        self.add_transition(Rectangle.State.passing, Rectangle.State.static,
            lambda: self.at_pos(),"stay")

        for state in Rectangle.State:
            self.add_transition(state,Rectangle.State.setup,
                lambda: self.behavior_failed,"failed")

    def add_kub(self, kub):
        self.kub = kub
    
    def add_theta(self, theta):
	    self.theta = theta

    def prev_has_ball(self):
        pass
    def has_ball(self):
        pass
    def at_pos(self):
        pass
    
    def on_enter_setup(self):
        pass
    def execute_setup(self):
        pass
    def on_exit_setup(self):
        pass

    def on_enter_static(self):
        pass
    def execute_static(self):
        pass
    def on_exit_static(self):
        pass

    def on_enter_alligning(self):
        pass
    def execute_alligning(self):
        pass
    def on_exit_alligning(self):
        pass

    def on_enter_receive(self):
        pass
    def execute_receive(self):
        pass
    def on_exit_receive(self):
        pass

    def on_enter_passing(self):
        pass
    def execute_passing(self):
        pass
    def on_exit_passing(self):
        pass
