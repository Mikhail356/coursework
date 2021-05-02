import mf2py
import mf2util
import json
import sys
import requests

if len(sys.argv) < 2:
  print("Err inp parametres:", sys.argv[0], "URL-link")
  sys.exit()
try:
  requests.get(sys.argv[1])
except OSError:
  print('Not correct url')
  sys.exit()

obj = mf2py.Parser(url=sys.argv[1]).to_dict()
#print(json.dumps(obj, indent = 4, sort_keys = False, ensure_ascii = False))
#print(obj.keys(), obj['rel-urls'], obj['rels'], type(obj['rels']), sep='\n')
#wm_serv = obj['rels']['webmention'][0]# address of webmention node
#print('\n\n\n')

b = obj['items'][1]['children']
l = len(b)
for i in range(l):
  t_url = b[i]['properties']['url'][0]
  wm_serv = mf2py.Parser(url=t_url).to_dict()
#  print(json.dumps(wm_serv, indent = 4, sort_keys = False, ensure_ascii = False))
  wm_serv = wm_serv['rels']['webmention'][0]
  requests.post(wm_serv, data = {'source' : sys.argv[1], 'target' : t_url})
#  print('-------------------------------------')
