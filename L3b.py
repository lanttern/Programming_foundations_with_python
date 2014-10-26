# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 18:40:54 2014

@author: zhihuixie
"""

class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print ("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys
        
Smith_Autism = Child("Smith Autism", "yellow", "10")
print Smith_Autism.last_name
print Smith_Autism.num_of_toys    