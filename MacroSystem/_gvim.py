# -*- coding: utf-8 -*-
from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Function,
                        Integer, Key, Text)
from _series_mapping_rule import SeriesMappingRule
from _key_press_event_mapping_rule import KeyPressEventMappingRule

class GVimMappingRule(KeyPressEventMappingRule):
    pass
     

gvim_context = AppContext(executable="gvim")
gvim_grammar = Grammar("gvim", context=gvim_context)

# apply series mapping rules continuous command recognition
gvim_mapping_rule = SeriesMappingRule(GVimMappingRule())

# add and load mapping rules
gvim_grammar.add_rule(gvim_mapping_rule)
gvim_grammar.load()

def unload():
    global gvim_grammar
    if gvim_grammar: gvim_grammar.unload()
    gvim_grammar = None
