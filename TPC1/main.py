#função que lê ficheiro de CSV (DONE)
#função de distribuição da doença por sexo
#função de distribuição da doença por faixa etária - intervalos de 5 unidades (DONE)
#função de distribuição de doença por niveis de colesterol - intervalos de 10 unidades


def open_file(file):
    with open(file) as f:
        next(f)
        content = f.readlines()

    valid_lines= []

    for line in content:
        idade,sexo,tensao,colesterol,batimento,temDoenca = line.strip().split(',')
        valid_lines.append((int(idade),sexo,int(tensao),int(colesterol),int(batimento),bool(int(temDoenca))))

    return valid_lines


def dist_idades(lines):
    dist= dict()

    idade_max = max(x[0] for x in lines)

    for idade in range(30, idade_max, 5):
        pessoas = [x for x in lines if x[0] in range(idade,idade+5)]
        doentes = [x for x in pessoas if x[-1]]
        dist[(idade, idade+4)] = len(doentes)/len(pessoas)

    return dist

def dist_sexo(lines):
    dist = dict()

    #male = [x for x in lines if x[1]=="M"]
    male_d = [x for x in lines if x[1]=="M" and x[-1]]
    #female = [x for x in lines if x[1]=="F"]
    female_d = [x for x in lines if x[1]=="F" and x[-1]]

    dist["M"] = len(male_d)/(len(male_d)+len(female_d)) 
    dist["F"] = len(female_d)/(len(male_d)+len(female_d))

    return dist

def dist_col(lines):
    dist = dict()

    colesterol_max = max(x[3] for x in lines)
    print(colesterol_max)
    
    for colesterol in range(0, colesterol_max, 10):
        pessoas = [x for x in lines if x[3] in range(colesterol,colesterol+10)]
        doentes = [x for x in pessoas if x[-1]]
        
        if not pessoas:
            dist[(colesterol, colesterol+9)] = 0
        else:
            dist[(colesterol, colesterol+9)] = len(doentes)/len(pessoas)

    return dist

def show_idades(dist):
    print("+"+"-"*30 + "+")
    print("| idades | percentagem doentes |")
    print("+"+"-"*30 + "+")

    for (i_min, i_max) in dist:
        print(f'| {i_min} - {i_max} | {dist[(i_min,i_max)]:<19.3%}|')

    print("+"+"-"*30 + "+\n")

def show_sexo(dist: dict()):
    print("+"+"-"*30 + "+")
    print("|  sexo  | percentagem doentes |")
    print("+"+"-"*30 + "+")

    print(f'|    M   |  {dist["M"]:<19.3%}|')
    print(f'|    F   |  {dist["F"]:<19.3%}|')
    print("+"+"-"*30 + "+\n")



def show_colesterol(dist):
    print("+"+"-"*34 + "+")
    print("| colesterol | percentagem doentes |")
    print("+"+"-"*34 + "+")

    for (i_min, i_max) in dist:
        print(f'| {i_min} - {i_max} | {dist[(i_min,i_max)]:<19.3%}|')

    print("+"+"-"*34 + "+\n")


def main():
    data = open_file("myheart.csv")
    distidades = dist_idades(data)
    distsexo = dist_sexo(data)
    distcoles = dist_col(data)

    show_idades(distidades)
    show_sexo(distsexo)
    show_colesterol(distcoles)


if __name__ == "__main__":
    main()

