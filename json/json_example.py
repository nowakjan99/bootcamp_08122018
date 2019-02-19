import json

lista = [1,3,'a','b','c']

print(type(lista))

json_list = json.dumps(lista)

napis = '{"1":"a", 2":"b"}'
ds_napis = json.loads(napis)

print(ds_napis)
print(type(ds_napis))