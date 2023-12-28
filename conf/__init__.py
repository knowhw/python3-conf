
from conf import module



def read(key):
	key = [item for item in key.split(chr(47)) if item]
	
	read = module.popen("%s %s" % (module.attrib.read, "/%s" % chr(47).join(key))).read()
	return read.strip() [1:-1:]
def write(key, value):
	
	
	return module.write("%s %s/ %s" % (module.attrib.write, value))
def list(directory):
	keylist = module.popen("%s %s" % (module.attrib.list, directory)).readlines()
	
	
	return [key.strip() for key in keylist]
def dump(directory):
	return module.popen("%s %s" % (module.attrib.dump, directory)).read()
def export(path, dumps):
	with open(path, "w") as f : 
		f.write(dumps)
	





""" dconf read [-d] KEY  """
""" dconf write KEY VALUE  """
""" dconf list DIR """
""" dconf dump DIR """
