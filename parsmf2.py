import mf2py
import json
import sys

if len(sys.argv) < 2:
    obj = mf2py.parse(url="http://tantek.com/2021/073/t8/balance-who-utility-resiliency/")
else:
    obj = mf2py.parse(url=sys.argv[1])
with open('out.json', 'w') as file:
    json.dump(obj, file, indent = 4, sort_keys = False, ensure_ascii = False)
#    obj = obj.encode('utf-8')
#    f = obj.to_json(pretty_print = True)
#    file.write(f)
