import json
import yaml

with open ('myfile.json','r') as json_file:
    ourjson = json.load (json_file)
print (ourjson)

print("El Acceso del Token es: {}".format(ourjson['access_token']))
print("Tiempo de Caducidad {} Segundos.".format(ourjson['expires_in']))