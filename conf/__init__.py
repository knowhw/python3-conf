
from conf import module



def read(key):
	
	key = [item for item in key.split(chr(47)) if item]
	
	read = module.popen("%s %s" % (module.attrib.read, "/%s" % chr(47).join(key))).read()
	return read.strip() 
def write(key, value):
	
	
	return module.write("%s %s/ %s" % (module.attrib.write, value))
def list(directory):
	
	dirs = [item for item in directory.split(chr(47)) if item]
	keylist = module.popen("%s %s" % (module.attrib.list, "/%s/" % chr(47).join(dirs))).readlines()
	
	
	
	return [key.strip() for key in keylist]
def load(directory, dumpf):
	""" dumpf: database.db """
	module.write("%s %s < %s" % (module.attrib.load, directory, dumpf))
	
def dump(directory):
	return module.popen("%s %s" % (module.attrib.dump, directory)).read()
	
def export(path, dump):
	with open(path, "w") as f : 
		f.write(dump)








