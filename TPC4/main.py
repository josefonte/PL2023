import re 
import json

f = open("./alunos.csv","r")
c=0
jsonOutput = []
keys= list()

for line in f:
    if c==0:
        pattern = re.compile("(\w+)?({?\w?}:*:*\w*)?,+")   
        header = pattern.findall(line)
        for item in header:
            key,extra = item
            if extra:
                pat_extra = re.compile("{(\w-*\w*)}:*:*(\w*)")
                extra_val = pat_extra.match(extra)
                nValores, tipo = extra_val.groups()
                nValores = int(nValores)
                
            keys.append(key)
           
    else :
        pattern = re.compile("(\w+\s*\w*),?")
        values = pattern.findall(line)
        jitem = {
                    keys[0]: values[0],
                    keys[1]: values[1],
                    keys[2]: values[2],
                }
        
        if tipo in ['media','sum']:
            jitem[keys[3]+"_"+tipo] = 0 
        else:
            jitem[keys[3]] = []
        
        valor=0
        xval=1
        for i in range(nValores):
            v = values[i+3].strip()
            if tipo in ['media','sum']:
                valor += int(v)
                if i == nValores-1 and tipo =='media':
                    valor /= xval    
                jitem[keys[3]+"_"+tipo] = valor
                xval += 1
            else:
                jitem[keys[3]].append(item)
        print(jitem)
        jsonOutput.append(jitem)
        
    c+=1

with open('output.json', 'w') as file:
        json.dump(jsonOutput, file, indent=4)