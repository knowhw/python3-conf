from json import dumps
from os import popen 
from os import system as write

class attrib: pass


attrib.read,attrib.write="dconf read","dconf write"
\
attrib.list="dconf list"
attrib.dump="dconf dump"
attrib.laod="dconf load"

