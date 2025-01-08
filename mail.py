#!//usr//bin//python
# -*- coding: UTF-8 -*-

from random import sample, shuffle, randint
import re
from collections import defaultdict
from itertools import combinations as comb
from solvers import moir, formula_list, molar_mass, equation_balancer, formula_namer, name_formulizer
from inputers import moir_input
from makers import *
from data import *
from selector import *
import translators
from practice import *
from time import sleep

def prob_num():
    problems = ''
    while True:
        problems = input("\nHow many practice problems would you like: ")
        if problems.isnumeric() and 0 < int(problems) < 110:
            return int(problems)
        else:
            print("Please select a number between 1 and 10.\n")
            

while True:
    print('\n'*40)
    menu_display()
    selection = ''
    while True:
        selection = input("Please make a selection: ")
        if selection.isnumeric() and 0 < int(selection) < 15:
            break
    match selection:
        case '1':#Naming Compounds
            problems = prob_num()
            compound_naming_practice(problems)
            sleep(3)
        case '2':#Finding Formulas
            problems = prob_num()
            formula_finding_practice(problems)
            sleep(3)
        case '3':
            problems = prob_num()
            equation_balance_practice(problems)
            sleep(3)
        case '4':
            problems = prob_num()
            reaction_prediction_practice(problems)
            sleep(3)
        case '5':
            problems = prob_num()
            stoichiometry_practice(problems)
            sleep(3)
        case '6':
            problems = prob_num()
            moir_practice(problems)
            sleep(3)
