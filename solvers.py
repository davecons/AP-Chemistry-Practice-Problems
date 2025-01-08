from random import sample, shuffle, randint
import re
from collections import defaultdict
from itertools import combinations as comb
from data import *
from translators import *

def moir(data, reactants, rate_unit):#method of initial rates
    orders = [0]*len(reactants)
    #data format
    #molecule A     molecule B      molecule C(opt)      Rate
    #x              x               x                    x
    #y              y               y                    y
    #z              z               z                    z
    #w              w               w                    w
    for a in comb(range(1,len(data)),2):
        if sum(r != s for r,s in zip(data[a[0]][0:-1], data[a[1]][0:-1])) == 1:
            #print(a)
            dif = [abs(data[a[0]][x]/data[a[1]][x]) for x in range(len(data[a[0]])-1)]
            change = [q for q in dif if abs(q-1.00) > 0.05]
            change_loc = [1 if abs(q-1.00) > 0.05 else 0 for q in dif ] 
            rdif = data[a[0]][-1]/data[a[1]][-1]#rate differences
            #print(dif,change,change_loc,rdif,orders)
            for x in change:
                if abs(change[0]**2 - rdif) < 0.05:
                    orders[change_loc.index(1)] = 2
                elif abs(change[0] - rdif) < 0.05:
                    orders[change_loc.index(1)] = 1
                
            #orders[change_loc.index(1)] = int(temp_ord[0])
            
    #if sum(orders) == 0:#you found no change at all - likely an issue
    #    temp_row = data[1]#this may not work
    #    data[1] = data[2]#need to consider edge cases
    #    data[2] = temp_row#this will be an infinite loop if the orders are really all 0
    #    moir(data,reactants)
    #if sum(orders) == 0:
    #    print("All orders 0 or this rate law can't be solved")
    #    return
    ret = 'R = k'
    for q,r in enumerate(reactants):
        if orders[q] == 0:
            pass
        elif orders[q] == 1:
            ret += '['+reactants[q].translate(SUB)+']'
        elif orders[q] == 2:
            ret += '['+reactants[q].translate(SUB)+']'+'2'.translate(SUP)
    rate_constant = data[1][-1]
    for a,x in enumerate(orders):
        rate_constant /= (data[1][a]**orders[a])
    print("Orders: ",orders)
    print("Rate Law: ",ret)
    print("Value of Rate Constant: ",round(rate_constant,5))
    order_print = ''
    if sum(orders) == 1:
        order_print = (rate_unit+"-1").translate(SUP)
    else:
        order_print = ("mol"+str(1-sum(orders))+" L"+str(sum(orders)-1)+" "+rate_unit+"-1").translate(SUP)
    print("Unit of Rate Constant: ", order_print)
    print()
    return ret,round(rate_constant,5),("mol"+str(1-sum(orders))+" L"+str(sum(orders)-1)+" "+rate_unit+"-1").translate(SUP)
    
def formula_list(formula):

    sFormula = formula
    #Search data inside ()
    myRegEx = re.compile(r"(\()(\w*)(\))(\d*)",re.I)
    myMatches = myRegEx.findall(sFormula)

    while myMatches:
        myMatches = myRegEx.findall(sFormula)
        for match in myMatches:
            count = match[3]
            text =""
            if (count == ""):
                count = 1
            else:
                count = int(match[3])
            while (count >= 1):
                text = text + match[1]
                count -= 1
            sFormula = sFormula.replace('(' + match[1] + ')' + match[3], text)
            
            
    myRegEx = re.compile("(C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|U|V|W|Xe|Yb?|Z[nr])(\\d*)")
    myMatches = myRegEx.findall(sFormula)
    molecularFormula =""
    MW = 0
    text =""
    mol_form = {}
    for match in myMatches:
        #Search symbol
        symbol = match[0]
        #Search numbers
        number = match[1]
        if (number == ""):
            number = 1
        else:
            number = int(match[1])
        if symbol not in mol_form:
            mol_form[symbol] = number
        else:
            mol_form[symbol] += number
        MW = MW + float(pt[symbol])*number
        while (number >=1):
            molecularFormula = molecularFormula + symbol
            number -= 1 
    return mol_form# - This might be useful for molecular counting atoms
    #return MW

def molar_mass(formula):

    sFormula = formula
    #Search data inside ()
    myRegEx = re.compile(r"(\()(\w*)(\))(\d*)",re.I)
    myMatches = myRegEx.findall(sFormula)

    while myMatches:
        myMatches = myRegEx.findall(sFormula)
        for match in myMatches:
            count = match[3]
            text =""
            if (count == ""):
                count = 1
            else:
                count = int(match[3])
            while (count >= 1):
                text = text + match[1]
                count -= 1
            sFormula = sFormula.replace('(' + match[1] + ')' + match[3], text)
            
            
    myRegEx = re.compile("(C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|U|V|W|Xe|Yb?|Z[nr])(\\d*)")
    myMatches = myRegEx.findall(sFormula)
    molecularFormula =""
    MW = 0
    text =""
    mol_form = {}
    for match in myMatches:
        #Search symbol
        symbol = match[0]
        #Search numbers
        number = match[1]
        if (number == ""):
            number = 1
        else:
            number = int(match[1])
        if symbol not in mol_form:
            mol_form[symbol] = 1
        else:
            mol_form[symbol] += 1
        MW = MW + float(pt[symbol])*number
        while (number >=1):
            molecularFormula = molecularFormula + symbol
            number -= 1 
    return MW

def equation_balancer(equation):
    reComp = re.compile(r'([A-Z][a-z]?)(\d+)?|[\)\]](\d+)?|[\(\[]')

    def parse_term(term_str, ind, scalar):
        lex = reComp.finditer(term_str)

        def f():
            d = defaultdict(int)
            for m in lex:
                elt, mult, mult2 = m.groups()
                if elt is None:
                    if m.group(0) in ('(', '['):
                        for k, v in f().items():
                            d[k] += v
                        continue
                    else:
                        mult2 = 1 if mult2 is None else int(mult2)
                        for k in d:
                            d[k] *= mult2
                        return d

                d[elt] += scalar*(1 if mult is None else int(mult))

            return d

        return f()

    def gcd2(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def make_trans(term, atom, excl):
        m = term[atom]
        rv = defaultdict(lambda: (1, 0))
        for k in term:
            if k not in excl:
                if term[k] != 0 and k != atom:
                    g = gcd2(term[k], m)
                    rv[k] = (m // g, term[k] // g)
        return rv

    def scale_term(atom, trans):
        def f(term):
            m = term[atom]
            for k in trans:
                alpha, beta = trans[k]
                term[k] = alpha*term[k] - beta*m
        return f

    def solvewith(terms, solvelist):
        solution = dict()
        firstiter = True
        for atom in reversed(solvelist):
            nzterms = [(i, t) for (i, t) in enumerate(terms) if t[atom] != 0]
            foci = [(i, t) for (i, t) in nzterms if i not in solution]
            if len(foci) > (2 if firstiter else 1):
                raise ValueError("Solution is indeterminate")

            firstiter = False
            if len(foci) == 2:
                solution[foci[1][0]] = 1

            (ifocus, focus) = foci[0]
            nzterms.remove(foci[0])

            dp = -sum(solution[i]*t[atom] for i, t in nzterms)
            y = focus[atom]
            g = gcd2(y, dp)
            fac = y // g
            for k in solution:
                solution[k] *= fac
            solution[ifocus] = dp // g

        s_array = [None]*len(terms)
        for i in solution:
            s_array[i] = solution[i]
        return s_array
                
    def writesoln(LHS, RHS, solution):
        n = len(LHS)
        alpha = " + ".join("%s%s" % ('' if t==1 else t, s) for s, t in zip(LHS, solution[:n]))
        beta = " + ".join("%s%s" % ('' if t==1 else t, s) for s, t in zip(RHS, solution[n:]))
        return "{} -> {}".format(alpha, beta)

    sLHS, sRHS = equation.split('→')
    LHS = [s.strip() for s in sLHS.split('+')]
    RHS = [s.strip() for s in sRHS.split('+')]
    n = len(LHS)
    terms = [parse_term(s, i, 1) for i, s in enumerate(LHS)] + [parse_term(s, n + i, -1) for i, s in enumerate(RHS)]
    solvelist = []
    termlist = []
    for i, t in enumerate(terms):
        for atom in t:
            if atom in solvelist: continue
            if t[atom] != 0: break
        else:
            continue
        trans = make_trans(t, atom, solvelist)
        scale = scale_term(atom, trans)
        for u in terms[i:]:
            scale(u)
        solvelist.append(atom)
        termlist.append(i)
    solution = solvewith(terms, solvelist)
    assert(all(x is not None for x in solution))
    if all(x == 0 for x in solution):
        return "No solution"
    else:
        return solution

def formula_namer(formula):
    formula = formula.translate(NORSUB)
    if "•" in formula:#hydrate:
        ret = formula_namer(formula[0:formula.index("•")-1])
        ret += " "
        ret += pref[int(formula[formula.index("•")+2])]#'''won't work with hydrates above 9'''
        ret += 'hydrate'
        return ret
    try:
        if any(x in formula for x in pref):
            #subscripts with poly
            if "(" in formula:
                subscripts = ['1',formula[-1]]
                if formula[formula.index('(')-1].isnumeric():
                    subscripts[0] = formula[formula.index('(')-1]
                    formula_hold = formula_list(formula)
                    elements = list(formula_hold.keys())
                    #subscripts = [formula_hold[x] for x in elements]
        else:
            formula_hold = formula_list(formula)
            elements = list(formula_hold.keys())
            subscripts = [formula_hold[x] for x in elements]
    except:
        return "Can't name this compound"
    if elements[0] == 'H':#acid
        if ' aq' in formula:
            formula = formula[0:formula.index(' aq')]
        if ' (aq)' in formula:
            formula = formula[0:formula.index(' (aq)')]
        if '(aq)' in formula:
            formula = formula[0:formula.index('(aq)')]
        try:
            if formula[1].isnumeric():
                anion = formula[2:]
            else:
                anion = formula[1:]
            if anion[-1].isnumeric():
                return (aroots_PAI[anion.translate(NORSUB)]+" acid").title()
            else:
                return ("hydro" + aroots_NM[anion.translate(NORSUB)] + " acid").title()
        except:
            return "Acid name unknown"
    elif elements[0] in ['N','S','P','Cl','F','O','Br','Se','I','Te']:
        try:
            ret = ''
            if subscripts[0] != 1:
                ret += pref[subscripts[0]]
            ret += enames[elements[0]]
            ret += ' '
            ret += pref[subscripts[1]]
            ret += sroots[elements[1]]
            ret += 'ide'
            return ret.title()
        except:
            return "Can't name this compound"
    elif elements[0] == 'C':#organic
        return "Organic naming is generally too complex for a simple program. Please consider getting a Ph.D. in nomenclature."
    elif elements[0] in all_tmet:#
        
        try:
            ret = enames[elements[0]]
            ret += ' ('
            if any(x in formula for x in all_pai):
                spec_pai = ''
                for pai_opt in all_pai:
                    if pai_opt in formula:
                        spec_pai = pai_opt
                        break
                loc = formula.index(spec_pai)+len(spec_pai)
                if len(formula) > loc:#there is a subscript after the PAI
                    sub2 = int(formula[-1])
                else:
                    sub2 = 1
                roman = rn[pai[all_pai.index(spec_pai)][1]*sub2//subscripts[0]-1]
                ret += roman
                ret += ") "
                ret += painames[spec_pai]
            else:
                roman = rn[nmet[all_nmet.index(elements[1])][1]*subscripts[1]//subscripts[0]-1]
                ret += roman
                ret += ") "
                ret += sroots[elements[1]]
                ret += 'ide'
            return ret
        except:
            return "Can't name this compound"
    else:
        try:
            ret = enames[elements[0]]
            ret += ' '
            if any(x in formula for x in all_pai):
                spec_pai = ''
                for pai_opt in all_pai:
                    if pai_opt in formula:
                        spec_pai = pai_opt
                        break
                ret += painames[spec_pai]
            else:
                ret += sroots[elements[1]]
                ret += 'ide'
            return ret.title()
        except:
            return "Can't name this compound"
        
def name_formulizer(name):
    try:
        if 'hydrate' in name.lower():
            hyd_co = 1
            for pre in pref:
                if pre.lower() in name[name.rfind(" "):].lower():
                    hyd_co = pref.index(pre)
                    break
            return name_formulizer(name[0:name.rfind(" ")]).translate(SUB) + " • " + str(hyd_co) + "H2O".translate(SUB)
        words = name.split(" ")
        words = [x.title() if x != x.upper() else x for x in words ]
        if "Acid" in words:
            if "hydro" in name.lower():#binary
                spec_name = ''
                for aname in anames_NM:
                    if aname.lower() in words[0]:
                        spec_name = aname
                        break
                charge1 = ''
                charge2 = nmet[all_nmet.index(anames_NM[spec_name])][1]
                if charge2 == 1:
                    charge2 = ''
                ret = "H"+str(charge2)+anames_NM[spec_name]+str(charge1)+' (aq)'
                return ret.translate(SUB)
            else:
                spec_name = ''
                for aname in anames_PAI:
                    if aname in words[0]:
                        spec_name = aname
                        break
                charge1 = ''
                charge2 = pai[all_pai.index(anames_PAI[spec_name])][1]
                if charge2 == 1:
                    charge2 = ''
                ret = "H"+str(charge2)+anames_PAI[spec_name]+str(charge1)+' (aq)'
                return ret.translate(SUB)
        elif any("("+a+")" in name for a in rn):#tm compound
            head = esymbols[words[0]]
            charge1 = rn.index(name[name.index("(")+1:name.index(")")])+1
            if any(x in words for x in pai_names):#it's a PAI compound
                spec_pai = ''
                for y in pai_names:
                    if y in words:
                        spec_pai = y
                        break
                charge2 = pai[pai_names.index(spec_pai)][1]
                tail = "("+all_pai[pai_names.index(spec_pai)]+")"
            else:
                charge2 = nmet[all_nmet.index(ssymbols[words[2][0:words[2].index("ide")]])][1]
                tail = nmet[all_nmet.index(ssymbols[words[2][0:words[2].index("ide")]])][0]
            while charge1 %2 == 0 and charge2 %2 == 0:
                charge1 //=2
                charge2 //=2
            while charge1 %3 == 0 and charge2 %3 == 0:
                charge1 //=3
                charge2 //=3
            if charge1 == 1:
                charge1 = ''
            if charge2 == 1:
                charge2 = ''
            return (head + str(charge2) + tail + str(charge1)).translate(SUB)
        elif len(re.findall(r'\b(mon|\bdi|tri|tetr|pent|hex|hept|oct|non|dec)',name.lower())) > 0:#nonmetal compound
            pref1 = 'Nul'
            elem1 = words[0]
            for pre in pref:
                if (pre[0:-1].lower() in words[0][0:4].lower() and pre[-1] in ['a','o']) or pre.lower() in words[0][0:4].lower():
                    pref1 = pre
                    break
            if pref1.lower() in words[0].lower():
                elem1 = words[0][words[0].index(pref1)+len(pref1):]
            elif pref1[0:-1].lower() in words[0].lower():
                elem1 = words[0][words[0].index(pref1[0:-1])+len(pref1)-1:]
            pref2 = ''
            
            for pre in pref:
                if (pre[0:-1].lower() in words[1][0:4].lower() and pre[-1] in ['a','o']) or pre.lower() in words[1][0:4].lower():
                    pref2 = pre
                    break
            if pref2.lower() in words[1].lower():
                elem2 = words[1][words[1].index(pref2)+len(pref2):]
            elif pref2[0:-1].lower() in words[1].lower():
                elem2 = words[1][words[1].index(pref2[0:-1])+len(pref2)-1:]
            root2 = elem2[0:elem2.index('ide')]
            
            sub1 = ''
            if pref1 != 'Nul' and pref1 != 'Mono':
                sub1 = str(pref.index(pref1))
            sub2 = ''
            if pref2 != 'Nul' and pref2 != 'Mono':
                sub2 = str(pref.index(pref2))
            return (esymbols[elem1.title()]+sub1+ssymbols[root2.title()]+sub2).translate(SUB)
            pass
        elif esymbols[words[0]] in all_met:
            head = esymbols[words[0]]
            charge1 = met[all_met.index(esymbols[words[0]])][1]
            if any(x in words for x in pai_names):#it's a PAI compound
                spec_pai = ''
                for y in pai_names:
                    if y in words:
                        spec_pai = y
                        break
                charge2 = pai[pai_names.index(spec_pai)][1]
                tail = "("+all_pai[pai_names.index(spec_pai)]+")"
            else:
                charge2 = nmet[all_nmet.index(ssymbols[words[1][0:words[1].index("ide")]])][1]
                tail = nmet[all_nmet.index(ssymbols[words[1][0:words[1].index("ide")]])][0]
            while charge1 %2 == 0 and charge2 %2 == 0:
                charge1 //=2
                charge2 //=2
            while charge1 %3 == 0 and charge2 %3 == 0:
                charge1 //=3
                charge2 //=3
            if charge1 == 1:
                charge1 = ''
            if charge2 == 1:
                charge2 = ''
            if charge1 == '' and "(" in tail:
                tail = tail[1:-1]
            return (head + str(charge2) + tail + str(charge1)).translate(SUB)
    except:
        return "Cannot find this formula yet"

def reaction_predictor(reaction):
    #print(reaction,[len(formula_list(x)) for x in reaction],any((len(formula_list(x)) 
    if 'O2' in reaction[0:2]:#combustion or special combustion\
        return True,"Combustion"
    if len(reaction) < 4:#decomp
        return True,"Decomp"
    if any(len(formula_list(x)) == 1 for x in reaction):#Single Displacement
            if activity_series.index(reaction[0]) < activity_series.index(reaction[2]):
                return True,"SD"
            return False,"SD"
    else:#Double Displacement
        for x in solubility_chart:
            if x in reaction[2] and any(y in reaction[2] for y in solubility_chart[x]):
                print(reaction[2].translate(SUB)+" is insoluble")
                return True,"DD"
            if x in reaction[3] and any(y in reaction[3] for y in solubility_chart[x]):
                print(reaction[3].translate(SUB)+" is insoluble")
                return True,"DD"
        return False,"DD"
        
    return True
