import re 
import json

f = open("./alunos.csv","r")
c=0
jsonOutput = []
vault = dict()
keys= list()

for line in f:
    if c==0:
        pattern = re.compile("(\w+)?{?(\w)?}?,+")   
        header = pattern.findall(line)
        for item in header:
            key,extra = item
            if extra : 
                #er1 = re.compile("")   
                vault[(key,extra)] = [] 
            else:
                vault[key] = [] 
            keys.append(key)
           

    else :
        pattern = re.compile("(\w+\s*\w*),?")
        values = pattern.findall(line)
        jitem = {
                    keys[0]: values[0],
                    keys[1]: values[1],
                    keys[2]: values[2],
                    keys[3]: []
                }
      
        for item in values[3:]:
            jitem[keys[3]].append(item)
        print(jitem)
        jsonOutput.append(item)
        
    c+=1



with open('output.json', 'w') as file:
        json.dump(jsonOutput, file, indent=4)