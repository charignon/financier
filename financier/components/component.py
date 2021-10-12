#!/usr/bin/env python3

class Component:
   def __init__(self, *args, **kwargs):
       if "name" in kwargs:
           self.name = kwargs["name"]
