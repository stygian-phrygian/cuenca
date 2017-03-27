# -*- coding: utf-8 -*-

from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Integer,
                       Key, Text)
from _series_mapping_rule import SeriesMappingRule
from _key_press_event_mapping_rule import KeyPressEventMappingRule

firefox_context = AppContext(executable="firefox")
chrome_context  = AppContext(executable="chrome")
grammar         = Grammar("cuenca", context=chrome_context|firefox_context)

class CuencaMappingRule(KeyPressEventMappingRule):
    print("This is a wrapper around the key press event mapping to apply it to multiple browser web socket contexts.")
    pass


  
grammar.add_rule(SeriesMappingRule(CuencaMappingRule()))
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
