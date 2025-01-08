def moir_input():
    num_of_reactants = int(input("How many reactants? "))
    reactants = []
    data = []
    for x in range(num_of_reactants):
        reactants.append(input("Formula of reactant #" +str(x+1)+"? "))
    reactants.append('Rate')
    data.append(reactants)
    num_of_trials = int(input("How many experiments are listed? "))
    for y in range(num_of_trials):
        row = []
        for z in range(num_of_reactants):
            row.append(float(input("What is the concentration of "+str(reactants[z])+" in experiment "+str(y+1)+"? ")))
        row.append(float(input("What is the Rate of Reaction in experiment "+str(y+1)+"? ")))
        data.append(row)
    rate_unit = input("What is the rate time unit? (s, min, etc.) ")
    #moir(data,reactants,rate_unit)
    #print(data,reactants,rate_unit)
    return data,reactants,rate_unit

#moir_data = moir_input()
#moir(moir_data[0],moir_data[1],moir_data[2])
