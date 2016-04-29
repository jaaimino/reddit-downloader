import importlib, re
from util import find_files

modules = []

for file in find_files("modules"):
	if file.endswith(".py") and not file == "__init__.py":
		filename = 'modules.'+file[:-3]
		modules.append(importlib.import_module(filename))

"""
for module in modules:
	print module
"""

pattern = re.compile(r'(http://i.imgur.com/(.*))(\?.*)?')

result = pattern.search("http://i.imgur.com/test") # using regex here instead of BeautifulSoup because we are pasing a url, not html
if result:
	print result.group(0)
	print len(result.groups())