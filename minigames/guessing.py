import re

last_id = 'http://site.com/produto/123123'
try:
   # found = re.search("([1-6]+)", last_id).group(1)
   found = re.search("([0-9]+){1,3}", last_id).group(1)
except AttributeError:
    found = 'Not Found'  # apply your error handling

print(found)
