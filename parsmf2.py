import mf2py
import json
import sys

if len(sys.argv) < 2:
    obj = mf2py.parse(url="http://tantek.com/2021/073/t8/balance-who-utility-resiliency/")
else:
    obj = mf2py.parse(url=sys.argv[1])
with open('person.json', 'w') as json_file:
  json.dump(obj, json_file, indent = 4, sort_keys = True)