from makers import *
from data import *
from translators import *
from solvers import *
from random import sample, shuffle, randint
import re
from collections import defaultdict
from itertools import combinations as comb

def equation_balance_practice(num):
    num = int(num)
    print("\nEquations to balance: \n")
    for a,equation in enumerate(equations[0:num]):
        eq = equation[0]+' + '+equation[1]+' → '+equation[2]+' + '+equation[3]
        print(str(a+1)+'. '+eq.translate(SUB))
        input("Press enter for answer\n")
        coe = [x if x != 1 else '' for x in equation_balancer(eq)]
        eq = eq.translate(SUB).split(' ')
        print("ANSWER: "+str(coe[0])+eq[0]+' '+eq[1]+' '+str(coe[1])+eq[2]+' '+eq[3]+' '+str(coe[2])+eq[4]+' '+eq[5]+' '+str(coe[3])+eq[6])
        print()

def formula_finding_practice(num):
    print("\nCompound names - Find Formulas: \n")
    for a,name in enumerate(names[0:num]):
        print(str(a+1)+'. '+name)
        input("Press enter for answer\n")
        print("ANSWER: "+name_formulizer(name))
        print()

def compound_naming_practice(num):
    print("\nCompound formulas - Find Names: \n")
    for a,formula in enumerate(formulas[0:num]):
        if "•" in formula:
            print(str(a+1)+'. '+formula[0:formula.find('•')].translate(SUB) + formula[formula.find("•"):formula.find("•")+3]+formula[formula.find("•")+3:].translate(SUB))
        else:
            print(str(a+1)+'. '+formula.translate(SUB))
        input("Press enter for answer\n")
        print("ANSWER: "+formula_namer(formula))
        print()

def reaction_prediction_practice(num):
    print("\nReaction prediction and balancing: \n")
    for a,predict in enumerate(predictions[0:num]):
        pr = predict[0]+ ' + '+predict[1]+' → '
        fi = predict[0]+ ' + '+predict[1]+' → ' + predict[2] + ' + ' +predict[3]
        print(str(a+1)+'. '+pr.translate(SUB))
        input("\nPress enter for answer\n")
        result,r_type = reaction_predictor(predict)
        if result:
            coe = [x if x != 1 else '' for x in equation_balancer(fi)]
            eq = fi.translate(SUB).split(' ')
            if r_type == 'DD':
                phase1 = '(aq)'
                phase2 = '(aq)'
                for x in solubility_chart:
                    if x in predict[2] and any(y in predict[2] for y in solubility_chart[x]):
                        phase1 = '(s)'
                    if x in predict[3] and any(y in predict[3] for y in solubility_chart[x]):
                        phase2 = '(s)'
                print(str(coe[0])+eq[0]+' (aq)'+' '+eq[1]+' '+str(coe[1])+eq[2]+' (aq)'+' '+eq[3]+' '+str(coe[2])+eq[4]+' '+phase1+' '+eq[5]+' '+str(coe[3])+eq[6]+' '+phase2)
                print()
            else:
                print(str(coe[0])+eq[0]+' '+eq[1]+' '+str(coe[1])+eq[2]+' '+eq[3]+' '+str(coe[2])+eq[4]+' '+eq[5]+' '+str(coe[3])+eq[6]+' ')
                print()
        else:
            print("No Reaction")
            print()

def stoichiometry_practice(num):
    print("\nStoichiometry:\n")
    for stoich in stoichs[0:num]:
        display = stoich[0]+" + "+stoich[1]+" → "+stoich[2]+" + "+stoich[3]
        balance = equation_balancer(display)
        print(display.translate(SUB))
        #print(balance)
        comp1 = randint(100,200)/1000
        comp2 = randint(100,200)/1000
        while comp1 == comp2:
            comp1 = randint(100,200)/1000
            comp2 = randint(100,200)/1000
        mol0 = comp1/molar_mass(stoich[0])
        mol1 = comp2/molar_mass(stoich[1])
        mol3a = mol0/balance[0]*balance[3]*molar_mass(stoich[3])
        mol3b = mol1/balance[1]*balance[3]*molar_mass(stoich[3])
        answer = min(round(mol3a,3),round(mol3b,3))
        
        st = "\nHow many grams of "+stoich[3].translate(SUB)+" can be formed from "+"{:.3f}".format(comp1)+" grams of "+stoich[0].translate(SUB)+" reacting with "+"{:.3f}".format(comp2)+" grams of "+stoich[1].translate(SUB)+"?"
        print(st)
        input("\nPress enter for answer\n")
        coe = [x if x != 1 else '' for x in equation_balancer(display)]
        eq = display.translate(SUB).split(' ')
        print(str(coe[0])+eq[0]+' '+eq[1]+' '+str(coe[1])+eq[2]+' '+eq[3]+' '+str(coe[2])+eq[4]+' '+eq[5]+' '+str(coe[3])+eq[6])
        print()
        print("ANSWER: "+"{:.3f}".format(answer)+ " grams of "+stoich[3].translate(SUB)+" can be formed.\n")

def moir_practice(num):
    print("\nMethod of Initial Rates - Kinetics: \n")
    for moir_a in moir_data:
        for row in moir_a[0]:
            print('\t'.join(str(val) for val in row))
        print("\nFind the orders of each reactant.")
        print("Find the value and unit of the rate constant.\n")
        input("Press enter for answer\n")
        moir(moir_a[0],moir_a[1],moir_a[2])

#moir_practice(1)
