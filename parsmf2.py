import mf2py
import json
import sys

if len(sys.argv) < 2:
    obj = mf2py.Parser(url="http://tantek.com/2021/073/t8/balance-who-utility-resiliency/")
else:
    obj = mf2py.Parser(url=sys.argv[1])
with open('person.json', 'w') as json_file:
#  json.dump(obj, json_file, indent = 4, sort_keys = True)
#    f = obj.to_json()  # returns a JSON string
#    json_file.write(f)
    f = obj.to_json(pretty_print = True)
    json_file.write(f)