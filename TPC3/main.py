import re

f = open("processos.txt","r")
er1 = re.compile("(?P<id>\d+)::(?P<ano>\d{4})-\d{2}-\d{2}::(?P<nome>[a-zA-Z ]+)::(?P<pai>[a-zA-Z ]+)::(?P<mae>[a-zA-Z ]+)::(?P<extra>[\w,\. ]+)?::\s")

def perguntaA():
  
    processosA = dict()

    for line in f:
        parser = er1.fullmatch(line)
        if parser:
            if parser.group("ano") in processosA:
                processosA[parser.group("ano")] +=1
            else :
                processosA[parser.group("ano")] = 1


    processos_por_ano = dict(sorted(processosA.items()))

    print("PERGUNTA A")
    for a in processos_por_ano.items():
        ano,freq = a
        print(ano + " : " + str(freq))
    
    ################################################3

def perguntaB():

    pnome = re.compile(r'^[a-zA-Z]+')   
    unome = re.compile(r'[a-zA-Z]+$')
    
    sec = dict()

    sec[117] = dict()
    sec[217] = dict()
    
    sec[118] = dict()
    sec[218] = dict()
    sec[119] = dict()
    sec[219] = dict()
    
    sec[120] = dict()
    sec[220] = dict()


    for line2 in f:
        parser = er1.fullmatch(line2)
        if parser :
            primnome = pnome.search(parser.group("nome")).group()
            ultnome = unome.search(parser.group("nome")).group()
            
            ano =  int(parser.group("ano"))

            if ano>1601 and ano<=1701:
                if primnome in sec[117]:
                    sec[117][primnome] +=1
                else :
                    sec[117][primnome] =1
                if ultnome in sec[217]:
                    sec[217][ultnome] +=1
                else :
                    sec[217][ultnome] =1
            elif ano>1701 and ano<=1801:
                if primnome in sec[118]:
                    sec[118][primnome] +=1
                else :
                    sec[118][primnome] =1
                if ultnome in sec[218]:
                    sec[218][ultnome] +=1
                else :
                    sec[218][ultnome] =1
            elif ano>1801 and ano<=1901:
                if primnome in sec[119]:
                    sec[119][primnome] +=1
                else :
                    sec[119][primnome] =1
                if ultnome in sec[219]:
                    sec[219][ultnome] +=1
                else :
                    sec[219][ultnome] =1
            elif ano>1901 and ano<=2001:
                if primnome in sec[120]:
                    sec[120][primnome] +=1
                else :
                    sec[120][primnome] =1
                if ultnome in sec[220]:
                    sec[220][ultnome] +=1
                else :
                    sec[220][ultnome] =1
        

    print("PERGUNTA B")
    
    for i in range(17,21):
        print("####################### Lista de Nomes Próprios | SECULO " + str(i))
        seculoNP = dict(sorted(sec[100+i].items(), key=lambda x:x[1]))
        for a in seculoNP.items():
            nome,freq = a
            print(str(nome) + " : " + str(freq))
        
        print("####################### Lista de Últimos Nomes | SECULO " + str(i))
        seculoUP = dict(sorted(sec[200+i].items(), key=lambda x:x[1]))
        for a in seculoUP.items():
            nome,freq = a
            print(str(nome) + " : " + str(freq))
            
            

def perguntaC():
    er2 = re.compile(",(?P<rel>[a-zA-Z ]+).")
    for line in f:
        parser = er1.fullmatch(line)
        if parser :
            extra = parser.group("extra")
            if extra:
                print(extra)
                print(er2.findall(extra))




def main():
    #perguntaA()
    #perguntaB()
    perguntaC()


main()