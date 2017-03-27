# -*- coding: utf-8 -*-
from dragonfly import (MappingRule, Dictation, Function, Integer, Key, Text)

# variable/function name formatting functions

def snake_case_action(text=""):
    s = "_".join(str(text).lower().split(" "))
    Text(s).execute()

def kebab_case_action(text=""):
    s = "-".join(str(text).lower().split(" "))
    Text(s).execute()

def one_word_case_action(text=""):
    s = "".join(str(text).lower().split(" "))
    Text(s).execute()

def camel_case_action(text=""):
    words = [word.capitalize() for word in str(text).split(" ")]
    s = words[0].lower() + "".join(words[1:])
    Text(s).execute()

def studley_case_action(text=""):
    words = [word.capitalize() for word in str(text).split(" ")]
    s = "".join(words)
    Text(s).execute()


#
# This mapping rule pertains mostly to single key press events
# and as such is rather low level.
#
# Text editing grammars should add this mapping rule into their grammar 
# and then build their own specific mapping rules  next to it 
# (rather than reinvent the wheel for each application).
#

class KeyPressEventMappingRule(MappingRule):
    name="key_press_event_mapping"
    exported=False
    mapping={

        "(dictate|say) <text>"    : Text("%(text)s"),

        "alpha"                   : Key("a"),
        "bravo"                   : Key("b"),
        "charlie"                 : Key("c"),
        "delta"                   : Key("d"),
        "echo"                    : Key("e"),
        "(foxtrot|foxy)"          : Key("f"),
        "(golf|gamma)"            : Key("g"),
        "hotel"                   : Key("h"),
        "india"                   : Key("i"),
        "(juliet|Juliet|Julia)"   : Key("j"),
        "kilo"                    : Key("k"),
        "lima"                    : Key("l"),
        "mike"                    : Key("m"),
        "november"                : Key("n"),
        "oscar"                   : Key("o"),
        "papa"                    : Key("p"),
        "(quebec|queen)"          : Key("q"),
        "romeo"                   : Key("r"),
        "sierra"                  : Key("s"),
        "tango"                   : Key("t"),
        "uniform"                 : Key("u"),
        "victor"                  : Key("v"),
        "whiskey"                 : Key("w"),
        "x-ray"                   : Key("x"),
        "yankee"                  : Key("y"),
        "zulu"                    : Key("z"),

        "upper alpha"             : Key("A"),
        "upper bravo"             : Key("B"),
        "upper charlie"           : Key("C"),
        "upper delta"             : Key("D"),
        "upper echo"              : Key("E"),
        "upper (foxtrot|foxy)"    : Key("F"),
        "upper (golf|gamma)"      : Key("G"),
        "upper hotel"             : Key("H"),
        "upper india"             : Key("I"),
        "upper (juliet|Juliet|Julia)"    : Key("J"),
        "upper kilo"              : Key("K"),
        "upper lima"              : Key("L"),
        "upper mike"              : Key("M"),
        "upper november"          : Key("N"),
        "upper oscar"             : Key("O"),
        "upper papa"              : Key("P"),
        "upper (quebec|queen)"    : Key("Q"),
        "upper romeo"             : Key("R"),
        "upper sierra"            : Key("S"),
        "upper tango"             : Key("T"),
        "upper uniform"           : Key("U"),
        "upper victor"            : Key("V"),
        "upper whiskey"           : Key("W"),
        "upper x-ray"             : Key("X"),
        "upper yankee"            : Key("Y"),
        "upper zulu"              : Key("Z"),

        "zero"                    : Key("0"),
        "one"                     : Key("1"),
        "two"                     : Key("2"),
        "three"                   : Key("3"),
        "four"                    : Key("4"),
        "five"                    : Key("5"),
        "six"                     : Key("6"),
        "seven"                   : Key("7"),
        "eight"                   : Key("8"),
        "nine"                    : Key("9"),
        "ten"                     : Text("10"),
        "eleven"                  : Text("11"),
        "twelve"                  : Text("12"),
        "thirteen"                : Text("13"),
        "fourteen"                : Text("14"),
        "fifteen"                 : Text("15"),
        "sixteen"                 : Text("16"),
        "seventeen"               : Text("17"),
        "eighteen"                : Text("18"),
        "nineteen"                : Text("19"),
        "twenty"                  : Text("20"),

        # Dragon already includes the macros
        # "go (up|down|left|right) <n>"
        # hence we don't need to implement them
        # nonetheless...
        # -- arrow keys
        "(Move|Moo) up    [<arrow_movement>]" : Key("up:%(arrow_movement)d"),
        "(Move|Moo) down  [<arrow_movement>]" : Key("down:%(arrow_movement)d"),
        "(Move|Moo) left  [<arrow_movement>]" : Key("left:%(arrow_movement)d"),
        "(Move|Moo) right [<arrow_movement>]" : Key("right:%(arrow_movement)d"),
        
        "page down" : Key("pgdown"),
        "page up"   : Key("pgup"),

        # vim specific things
        # I'm including <C-v> here because vim uses it
        # for visual block editing
        "control (V|Victor)" : Key("c-v"),
        # these next 2 don't work for some reason?
        #"control page down"  : Key("c-pgdown"),
        #"control page up"    : Key("c-pgup"),

        # Bugs?
        # The space, equals, and comma characters do not work so well
        # with CCR.  The same behavior persisted with the dot character,
        # until I proffered the hack below.  There must be a better way?


        "(space|spacer|spy|spine)": Key("space"),
        "(tab|tabby|Debbie)"      : Key("tab"),
        "(newline|enter|slap)"    : Key("enter"),
        "(Homey|Home)"            : Key("home"),
        "(Endy|Andy)"             : Key("end"),
        "(mod|percent) [sign]"    : Key("percent"),
        "(asterisk|star)"         : Key("asterisk"),
        "plus [sign]"             : Key("plus"),
        "(hyphen|minus|tack|negative)" : Key("hyphen"),
        "(equal|equals) [to]"     : Key("equal"),
        "bang"                    : Key("exclamation"),
        "(hash|hashtag|pound)"    : Key("hash"),
        "dollar [sign]"           : Key("dollar"),
        "comma"                   : Key("comma"),
        "[<text_left>] (dot|point) [<text_right>]" : Text("%(text_left)s") + Key("dot") + Text("%(text_right)s"),
        "[forward] slash"         : Key("slash"),
        "colon"                   : Key("colon"),
        # This doesn't work for some reason.
        #"semicolon": Key("semicolon"),
        "semicolon"               : Text(";"),
        "(escape|scape)"          : Key("escape"),
        "ampersand"               : Key("ampersand"),
        "apostrophe"              : Key("apostrophe"),
        "at [sign]"               : Key("at"),
        "(leader|backslash)"      : Key("backslash"),
        "backtick"                : Key("backtick"),
        "pipe"                    : Key("bar"),
        "caret"                   : Key("caret"),
        "question [mark]"         : Key("question"),
        "tilde"                   : Key("tilde"),
        "(underscore|score)"      : Key("underscore"),

        # open and close code delimiters
        "L paren"                     : Key("lparen"),   # (
        "(or|our|are|R) paren"        : Key("rparen"),   # )
        "L brace"                     : Key("lbrace"),   # {
        "(or|our|are|R) brace"        : Key("rbrace"),   # }
        "L bracket"                   : Key("lbracket"), # [
        "(or|our|are|R) bracket"      : Key("rbracket"), # ]
        "L angle"                     : Key("langle"),   # <
        "(or|our|are|R) angle"        : Key("rangle"),   # >
        "less than [or]"              : Key("langle"),   # -- synonyms
        "greater than [or]"           : Key("rangle"),   # --
        "[(single|S)] (quote|quotes)" : Key("squote"),   # '
        "(double|D) (quote|quotes)"   : Key("dquote"),   # "

        # -- comparison
        # "<=" & ">=" are already available thanks to CCR from SeriesMappingRule
        #
        "double (equal|equals)"          : Text("=="),
        "(strict|double) not equals"     : Text("!=="),
        "(triple|strict) (equal|equals)" : Text("==="),

        # -- variable/function naming
        "snake [case] <text>"    : Function(snake_case_action,    extra={"text"}),
        "camel [case] <text>"    : Function(camel_case_action,    extra={"text"}),
        "studley [case] <text>"  : Function(studley_case_action,  extra={"text"}),
        "one word [case] <text>" : Function(one_word_case_action, extra={"text"}),
        "kebab [case] <text>"    : Function(kebab_case_action,   extra={"text"}),

        # -- code block deliniation
        "cuddle (paren|parenthesis) [<inner_text>]" : Text("(%(inner_text)s)") + Key("left"),
        "cuddle [curly] brace [<inner_text>]"       : Text("{%(inner_text)s}") + Key("left"),
        "cuddle bracket [<inner_text>]"             : Text("[%(inner_text)s]") + Key("left"),
        "cuddle angle [bracket] [<inner_text>]"     : Text("<%(inner_text)s>") + Key("left"),
        "cuddle (s|single) quote [<inner_text>]"    : Text("'%(inner_text)s'") + Key("left"),
        "cuddle (d|double) quote [<inner_text>]"    : Text('"%(inner_text)s"') + Key("left"),

        # common programming abbreviations
        "asynchronous": Text("async"),
        "associate"   : Text("assoc"),
        "dissociate"  : Text("dissoc"),
        "standard in" : Text("stdin"),
        "standard out": Text("stdout"),
        "argh"        : Text("arg"),
        "arghz"       : Text("args"),
        "deaf"        : Text("def"),

        }
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
            Dictation("inner_text"),
            Dictation("text_left"),
            Dictation("text_right"),
            Integer("arrow_movement", 1, 50)
           ]
    defaults={
            "text"          : "",
            "inner_text"    : "",
            "text_left"     : "",
            "text_right"    : "",
            "arrow_movement": 1
             }
    #############################







