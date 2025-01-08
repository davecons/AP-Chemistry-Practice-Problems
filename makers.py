from data import *
from random import sample, shuffle, randint
import re
from collections import defaultdict
from itertools import combinations as comb
from copy import deepcopy
from translators import *

type1 = []#double displacement with m+tm and nm
type2 = []#double displacement with m+tm and pai
type3 = []#single displacement with m and m+tm and nm
type4 = []#single displacement with m and m+tm and pai
type5 = []#combustion easy
type6 = []#combustion hard
type7 = [["NH3","O2","NO","H2O"],["NH3","O2","NO2","H2O"]]

type1A = []#these are for naming
type1B = []
type2A = []
type2B = []
type3A = []
type4A = []
type4B = []
typeSpecA = []
typeSpecB = []

moir_data = []#method of initial rates
for x in range(100):#make 100 problems
    unit = sample(['sec','min','hour'],1)[0]
    data = []
    reactant_num = randint(1,3)
    reactants = ['A','B','C'][0:reactant_num]
    reactants.append(('Rate (mol • L-1 • '+unit+'-1)').translate(SUP))
    data.append(reactants)
    orders = [randint(0,2) for x in range(reactant_num)]
    first_data = [round(randint(100,1000)/randint(495,499),3) for x in range(reactant_num)]
    first_data.append(round(randint(100,1000)/randint(495,499),3))
    data.append(first_data)
    for y in range(reactant_num):
        temp = deepcopy(data[-1])
        factor = randint(100,1000)/(randint(495,499))
        temp[y] *= factor
        temp[y] = round(temp[y],3)
        temp[-1] *= factor**orders[y]
        temp[-1] = round(temp[-1],3)
        data.append(temp)
    moir_data.append([data,reactants[0:-1],unit])
    #print(moir_data[-1])

                   
for a in [q for q in (met+tmet) if q[0] in solubility_chart]:
    for b in [q for q in nmet if q[0] in sum(solubility_chart.values(),[])]:       
        for c in (met+tmet):
            for d in [q for q in nmet if q[0] in sum(solubility_chart.values(),[])]:
                temp = []
                if a[0] != c[0] and b != d and a[1] != c[1]:
                    j = ""
                    if max(a[1],b[1]) % min(a[1],b[1]) == 0:
                        co1 = a[1]//min(a[1],b[1])
                        co2 = b[1]//min(a[1],b[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        j += b[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += a[0] + str(b[1]) + b[0] + str(a[1])
                    temp.append(j)
                    j = ""
                    if max(c[1],d[1]) % min(c[1],d[1]) == 0:
                        co1 = c[1]//min(c[1],d[1])
                        co2 = d[1]//min(c[1],d[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        j += d[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += c[0] + str(d[1]) + d[0] + str(c[1])
                    temp.append(j)
                    j = ""
                    if max(a[1],d[1]) % min(a[1],d[1]) == 0:
                        co1 = a[1]//min(a[1],d[1])
                        co2 = d[1]//min(a[1],d[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        j += d[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += a[0] + str(d[1]) + d[0] + str(a[1])
                    temp.append(j)
                    j = ""
                    if max(c[1],b[1]) % min(c[1],b[1]) == 0:
                        co1 = c[1]//min(c[1],b[1])
                        co2 = b[1]//min(c[1],b[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        j += b[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += c[0] + str(b[1]) + b[0] + str(c[1])
                    temp.append(j)
                    type1.append(temp)

for a in [q for q in (met+tmet) if q[0] in solubility_chart]:
    for b in [q for q in pai if q[0] in sum(solubility_chart.values(),[])]:
        for c in (met+tmet):
            for d in [q for q in pai if q[0] in sum(solubility_chart.values(),[])]:
                temp = []
                if a[0] != c[0] and b != d and a[1] != c[1]:
                    j = ""
                    if max(a[1],b[1]) % min(a[1],b[1]) == 0:
                        co1 = a[1]//min(a[1],b[1])
                        co2 = b[1]//min(a[1],b[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += b[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += b[0]
                    else:
                        j += a[0] + str(b[1]) + "(" + b[0] + ")" + str(a[1])
                    temp.append(j)
                    j = ""
                    if max(c[1],d[1]) % min(c[1],d[1]) == 0:
                        co1 = c[1]//min(c[1],d[1])
                        co2 = d[1]//min(c[1],d[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += d[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += d[0]
                    else:
                        j += c[0] + str(d[1]) + "(" + d[0] + ")" + str(c[1])
                    temp.append(j)
                    j = ""
                    if max(a[1],d[1]) % min(a[1],d[1]) == 0:
                        co1 = a[1]//min(a[1],d[1])
                        co2 = d[1]//min(a[1],d[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += d[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += d[0]
                    else:
                        j += a[0] + str(d[1]) + "(" + d[0] + ")" + str(a[1])
                    temp.append(j)
                    j = ""
                    if max(c[1],b[1]) % min(c[1],b[1]) == 0:
                        co1 = c[1]//min(c[1],b[1])
                        co2 = b[1]//min(c[1],b[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += b[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += b[0]
                    else:
                        j += c[0] + str(b[1]) + "(" + b[0] + ")" + str(c[1])
                    temp.append(j)
                    type2.append(temp)

for a in [q for q in met if q[0] in activity_series]:
        for c in [r for r in (met+tmet) if r[0] in activity_series]:
            for d in nmet:
                if a[1] != c[1] and a[0] != c[0]:
                    temp = [a[0]]
                    j = ""
                    if max(c[1],d[1]) % min(c[1],d[1]) == 0:
                        co1 = c[1]//min(c[1],d[1])
                        co2 = d[1]//min(c[1],d[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        j += d[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += c[0] + str(d[1]) + d[0] + str(c[1])
                    temp.append(j)
                    j = ""
                    temp.append(c[0])
                    if max(a[1],d[1]) % min(a[1],d[1]) == 0:
                        co1 = a[1]//min(a[1],d[1])
                        co2 = d[1]//min(a[1],d[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        j += d[0]
                        if co1 != 1:
                            j += str(co1)
                    else:
                        j += a[0] + str(d[1]) + d[0] + str(a[1])
                    temp.append(j)
                    type3.append(temp)

for a in [q for q in met if q[0] in activity_series]:
        for c in [r for r in (met+tmet) if r[0] in activity_series]:
            for d in pai:
                if a[1] != c[1] and a[0] != c[0]:
                    temp = [a[0]]
                    j = ""
                    if max(c[1],d[1]) % min(c[1],d[1]) == 0:
                        co1 = c[1]//min(c[1],d[1])
                        co2 = d[1]//min(c[1],d[1])
                        j += c[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += d[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += d[0]
                    else:
                        j += c[0] + str(d[1]) + "(" + d[0] + ")" + str(c[1])
                    temp.append(j)
                    temp.append(c[0])
                    j = ""
                    if max(a[1],d[1]) % min(a[1],d[1]) == 0:
                        co1 = a[1]//min(a[1],d[1])
                        co2 = d[1]//min(a[1],d[1])
                        j += a[0]
                        if co2 != 1:
                            j += str(co2)
                        if co1 != 1:
                            j += "("
                            j += d[0]
                            j += ")"
                            j += str(co1)
                        else:
                            j += d[0]
                    else:
                        j += a[0] + str(d[1]) + "(" + d[0] + ")" + str(a[1])
                    temp.append(j)
                    type4.append(temp)

type5 = [[a,"O2","CO2","H2O"] for a in hc1]#easy to balance HC combustion
type6 = [[a,"O2","CO2","H2O"] for a in hc2]#hard to balance HC combustion
###Fill the type1A list
for a in met:
    for b in nmet:
        j = ""
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            j = a[0]
            if co2 != 1:
                j += str(co2)
            j += b[0]
            if co1 != 1:
                j += str(co1)
        else:
            j = a[0] + str(b[1]) + b[0] + str(a[1])
        type1A.append(j)

###Fill the type1B list
for a in met:
    for b in pai:
        j = ""
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            j = a[0]
            if co2 != 1:
                j += str(co2)
            if co1 != 1:
                j += "("
                j += b[0]
                j += ")"
                j += str(co1)
            else:
                j += b[0]
        else:
            j = a[0] + str(b[1]) + "(" + b[0] + ")" + str(a[1])
        type1B.append(j)

###Fill the type2A list
for a in tmet:
    for b in nmet:
        j = ""
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            j = a[0]
            if co2 != 1:
                j += str(co2)
            j += b[0]
            if co1 != 1:
                j += str(co1)
        else:
            j = a[0] + str(b[1]) + b[0] + str(a[1])
        type2A.append(j)

###Fill the type2B list
for a in tmet:
    for b in pai:
        j = a[0]
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            if co2 != 1:
                j += str(co2)
            if co1 != 1:
                j += "("
                j += b[0]
                j += ")"
                j += str(co1)
            else:
                j += b[0]
        else:
            j = a[0] + str(b[1]) + "(" + b[0] + ")" + str(a[1])
        type2B.append(j)

type3A = [a[0]+(str(c) if c > 1 else '')+b[0]+(str(d) if d > 1 else '') for a in nmet for b in nmet for c in range(1,11) for d in range(1,11) if a != b]          
type4A = [a[0]+str(b[1])+b[0] if b[1] > 1 else a[0]+b[0] for a in hyd for b in nmet if b[0] != 'O' and b[0] != 'N']#binary acids
type4B = [a[0]+str(b[1])+b[0] if b[1] > 1 else a[0]+b[0] for a in hyd for b in pai]#ternary acids


###Fill the SpecA list
for a in spec:
    for b in nmet:
        j = ""
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            j = a[0]
            if co2 != 1:
                j += str(co2)
            j += b[0]
            if co1 != 1:
                j += str(co1)
        else:
            j = a[0] + str(b[1]) + b[0] + str(a[1])
        typeSpecA.append(j)

###Fill the SpecB list
for a in spec:
    for b in pai:
        j = ""
        if max(a[1],b[1]) % min(a[1],b[1]) == 0:
            co1 = a[1]//min(a[1],b[1])
            co2 = b[1]//min(a[1],b[1])
            j = a[0]
            if co2 != 1:
                j += str(co2)
            if co1 != 1:
                j += "("
                j += b[0]
                j += ")"
                j += str(co1)
            else:
                j += b[0]
        else:
            j = a[0] + str(b[1]) + "(" + b[0] + ")" + str(a[1])
        typeSpecB.append(j)
        
###Create lists of names of compounds
type1A_names = [enames[a[0]]+" "+sroots[b[0]] + "ide" for a in met for b in nmet]#M - NM
type1B_names = [enames[a[0]]+" "+painames[b[0]] for a in met for b in pai]#M - PAI
type2A_names = [enames[a[0]]+" ("+rn[a[1]]+") "+sroots[b[0]] + "ide" for a in tmet for b in nmet]#TM nmet
type2B_names = [enames[a[0]]+" ("+rn[a[1]]+") "+painames[b[0]] for a in tmet for b in pai]#TM PAI
type3_names = [((pref[c] if c > 1 else '')+(enames[a[0]].lower() if c > 1 else enames[a[0]])+" "+pref[d]+sroots[b[0]].lower()+"ide").replace("aa","a").replace("ao","o").replace("oo","o") for a in nmet for b in nmet for c in range(1,11) for d in range(1,11) if a != b]#NM NM
type4A_names = ['Hydro'+aroots_NM[b[0]].lower()+" Acid" for b in nmet[2:]]#Binary Acids
type4B_names = [aroots_PAI[b[0]]+ " Acid" for b in pai]#Ternary Acids
typeSpecA_names = [enames[a[0]]+" "+sroots[b[0]] + "ide" for a in spec for b in nmet]#TM Exceptions NM
typeSpecB_names = [enames[a[0]]+" "+painames[b[0]] for a in spec for b in pai]#TM Exceptions PAI



for x in range(1):
    
    equations = []
    equations.extend(sample(type1,2))
    equations.extend(sample(type2,2))
    equations.extend(sample(type3,2))
    equations.extend(sample(type4,2))
    equations.extend(sample(type5,1))
    equations.extend(sample(type6,1))
    equations.extend(sample(type7,1))
    shuffle(equations)
    
    names = []
    names.extend(sample(type1A_names,2))
    names.extend(sample(type1B_names,2))
    names.extend(sample(type2A_names,2))
    names.extend(sample(type2B_names,2))
    names[-1] += ' '+pref[(randint(3,6))]+'hydrate'
    names.extend(sample(type3_names,2))
    names.extend(sample(type4A_names,2))
    names.extend(sample(type4B_names,2))
    shuffle(names)

    formulas = []
    formulas.extend(sample(type1A,2))
    formulas.extend(sample(type1B,2))
    formulas.extend(sample(type2A,2))
    formulas[-1] +=' • '+str(randint(5,8))+'H2O'
    formulas.extend(sample(type2B,2))
    formulas.extend(sample(type3A,2))
    formulas.extend(sample(type4A,1))
    formulas[-1] += ' (aq)'
    formulas.extend(sample(type4B,1))
    formulas[-1] += ' (aq)'
    shuffle(formulas)

    predictions = []
    predictions.extend(sample(type1,2))
    predictions.extend(sample(type2,2))
    predictions.extend(sample(type3,2))
    predictions.extend(sample(type4,2))
    predictions.extend(sample(type5,2))
    predictions.extend(sample(type6,2))
    #predictions.extend(sample(type7,2))
    shuffle(predictions)

    stoichs = sample(equations,7)
