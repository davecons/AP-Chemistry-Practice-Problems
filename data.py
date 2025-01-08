nums = ['1','2','3','4','5','6','7','8','9','0']
met = [["Li",1],["Be",2],["Na",1],["Mg",2],["Al",3],["K",1],["Ca",2],["Ga",3],["Rb",1],["Sr",2],["Cs",1],["Ba",2],["Fr",1],["Ra",2]]
all_met = ["Li","Be","Na","Mg","Al","K","Ca","Ga","Rb","Sr","Cs","Ba","Fr","Ra"]
tmet = [["Ti",4],["Ti",3],["V",3],["V",5],["Cr",2],["Cr",3],["Mn",2],["Mn",4],["Fe",2],["Fe",3],["Co",3],["Co",4],["Ni",3],["Ni",2],["Cu",1],["Cu",2]]
nmet = [["N",3],["O",2],["F",1],["P",3],["S",2],["Cl",1],["Se",2],["Br",1],["Te",2],["I",1]]
pai = [["SO4",2],["SO3",2],["PO4",3],["PO3",3],["CO3",2],["NO3",1],["NO2",1]]
spec = [["Zn",2],["Ag",1]]
hyd = [["H",1]]
pref = ["Nul","Mono","Di","Tri","Tetra","Penta","Hexa","Hepta","Octa","Nona","Deca"]
rn = ["I","II","III","IV","V","VI","VII"]
hc1 = ["C2H4","C3H8","C4H8","C5H12","C6H12"]
hc2 = ["C2H6","C3H6","C4H10","C4H6","C5H10","C6H10"]
all_tmet = ["Sc", "Ti", "V", "Cr", "Mn", "Fe","Co", "Ni", "Cu","Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "In", "Sn", "Sb", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Ac", "Th", "Pa", "U","Np","Pu","Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No",  "Lr","Rf", "Db","Sg","Bh", "Hs","Mt",      "Ds","Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"] 
all_nmet = ['N','O','F','P','S','Cl','Se','Br','Te','I']

all_pai = ['SO4','SO3','PO4','PO3','CO3','NO3','NO2']
pai_names = ['Sulfate','Sulfite','Phosphate','Phosphite','Carbonate','Nitrate','Nitrite']

activity_series = ['Li','K','Ba','Sr','Ca','Na','Mg','Al','Zn','Cr',
                   'Fe','Cd','Co','Ni','Sn','Pb','H2','Cu','Hg','Ag',
                   'Pt','Au']

solubility_chart = {'Ca':['CO3','PO4','F','SO3'],
                    'Li':['PO4'],
                    'Mg':['CO3','OH','PO4','F','SO3'],
                    'Ba':['CO3','OH','SO4','PO4','F','SO3'],
                    'Fe':['OH','CO3','PO4'],
                    'Ag':['Cl','Br','I','CO3','OH','SO4','PO4','SO3'],
                    'Zn':['CO3','OH','PO4','SO3'],
                    'Pb':['F','Cl','Br','I','CO3','OH','PO4','SO3'],
                    'Al':['OH','PO4']}
                   
pt = {"H": 1.0079, "He": 4.0026, "Li": 6.941, "Be": 9.0122, "B": 10.811, "C": 12.0107, "N": 14.0067, "O": 15.9994, "F": 18.9984, "Ne": 20.1797, "Na": 22.9897, 
      "Mg": 24.305, "Al": 26.9815, "Si": 28.0855, "P": 30.9738, "S": 32.065, "Cl": 35.453,"Ar": 39.948,"K": 39.0983, "Ca": 40.078, "Sc": 44.9559, "Ti": 47.867, 
      "V": 50.9415, "Cr": 51.9961, "Mn": 54.938, "Fe": 55.845,"Co": 58.9332, "Ni": 58.6934, "Cu": 63.546, "Zn": 65.39, "Ga": 69.723, "Ge": 72.64, "As": 74.9216, 
      "Se": 78.96, "Br": 79.904, "Kr": 83.8, "Rb": 85.4678, "Sr": 87.62, "Y": 88.9059, "Zr": 91.224, "Nb": 92.9064, "Mo": 95.94, "Tc": 98, "Ru": 101.07, 
      "Rh": 102.9055, "Pd": 106.42, "Ag": 107.8682, "Cd": 112.411, "In": 114.818, "Sn": 118.71, "Sb": 121.76,"Te": 127.6, "I": 126.9045, "Xe": 131.293, 
      "Cs": 132.9055, "Ba": 137.327, "La": 138.9055, "Ce": 140.116, "Pr": 140.9077, "Nd": 144.24, "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, 
      "Tb": 158.9253, "Dy": 162.5, "Ho": 164.9303, "Er": 167.259, "Tm": 168.9342, "Yb": 173.04, "Lu": 174.967, "Hf": 178.49, "Ta": 180.9479, "W": 183.84, 
      "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt": 195.078, "Au": 196.9665, "Hg": 200.59, "Tl": 204.3833, "Pb": 207.2, "Bi": 208.9804, "Po": 209, 
      "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.0381, "Pa": 231.0359, "U": 238.0289,"Np": 237,"Pu": 244,"Am": 243, "Cm": 247, "Bk": 247, 
      "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259,  "Lr": 262,"Rf": 261, "Db": 262,"Sg": 266,"Bh": 264, "Hs": 277,"Mt": 268,"Ds": 281,"Rg": 272, 
      "Cn": 282, "Nh": 286, "Fl": 289, "Mc": 290, "Lv": 293, "Ts": 294, "Og": 294} 
         
enames = {"H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium","B": "Boron","C": "Carbon","N": "Nitrogen","O": "Oxygen","F": "Fluorine","Ne": "Neon",     
          "Na": "Sodium", "Mg": "Magnesium","Al": "Aluminum","Si": "Silicon","P": "Phosphorus","S": "Sulfur","Cl": "Chlorine","Ar": "Argon","K": "Potassium",
          "Ca": "Calcium",  "Sc": "Scandium","Ti": "Titanium","V": "Vanadium","Cr": "Chromium","Mn": "Manganese","Fe": "Iron","Co": "Cobalt","Ni": "Nickel",
          "Cu": "Copper","Zn": "Zinc","Ga": "Gallium","Ge": "Germanium","As": "Arsenic","Se": "Selenium","Br": "Bromine","Kr": "Krypton","Rb": "Rubidium",
          "Sr": "Strontium","Y": "Yttrium","Zr": "Zirconium","Nb": "Niobium","Mo": "Molybdenum","Tc": "Technetium","Ru": "Ruthenium","Rh": "Rhodium",
          "Pd": "Palladium","Ag": "Silver","Cd": "Cadmium","In": "Indium","Sn": "Tin","Sb": "Antimony","Te": "Tellurium","I": "Iodine","Xe": "Xenon",
          "Cs": "Cesium","Ba": "Barium","La": "Lanthanum","Ce": "Cerium","Pr": "Praseodymium","Nd": "Neodymium","Pm": "Promethium","Sm": "Samarium",
          "Eu": "Europium","Gd": "Gadolinium","Tb": "Terbium","Dy": "Dysprosium","Ho": "Holmium","Er": "Erbium","Tm": "Thulium","Yb": "Ytterbium",
          "Lu": "Lutetium","Hf": "Hafnium","Ta": "Tantalum","W": "Tungsten","Re": "Rhenium","Os": "Osmium","Ir": "Iridium","Pt": "Platinum", "Au": "Gold",
          "Hg": "Mercury","Tl": "Thallium","Pb": "Lead","Bi": "Bismuth","Po": "Polonium","At": "Astatine","Rn": "Radon","Fr": "Francium","Ra": "Radium",
          "Ac": "Actinium","Th": "Thorium","Pa": "Protactinium","U": "Uranium","Np": "Neptunium","Pu": "Plutonium","Am": "Americium","Cm": "Curium",
          "Bk": "Berkelium","Cf": "Californium","Es": "Einsteinium","Fm": "Fermium","Md": "Mendelevium","No": "Nobelium","Lr": "Lawrencium","Rf": "Rutherfordium",
          "Db": "Dubnium","Sg": "Seaborgium","Bh": "Bohrium","Hs": "Hassium","Mt": "Meitnerium","Ds": "Darmstadtium","Rg": "Roentgenium","Cn":"Copernicium",
          "Nh": "Nihonium", "Fl": "Flerovium", "Mc": "Moscovium", "Lv": "Livermorium", "Ts": "Tennessine","Og": "Oganesson"}

esymbols = {v: k for k, v in enames.items()}

sroots = {"C": "Carb","N": "Nitr","O": "Ox","F": "Fluor","P": "Phosph","S": "Sulf","Cl": "Chlor","Se": "Selen","Br": "Brom","I": "Iod","Te": "Tellur"}
ssymbols = {v: k for k, v in sroots.items()}
nmet_charge = {"C": 4,"N": 3,"O": 2,"F": 1,"P": 3,"S": 2,"Cl": 1,"As": 3,"Se": 2,"Br": 1,"Te": 2,"I": 1}
painames = {"CO3": "Carbonate","NO3": "Nitrate","SO4": "Sulfate","PO4": "Phosphate","NO2": "Nitrite","SO3": "Sulfite","PO3": "Phosphite"}
aroots_PAI = {"CO3": "Carbonic","SO4": "Sulfuric","SO3": "Sulfurous","PO3": "Phosphorous","PO4": "Phosphoric","NO3": "Nitric","NO2": "Nitrous"}
anames_PAI = {v: k for k, v in aroots_PAI.items()}
aroots_NM = {"S": "Sulfuric","P": "Phosphoric","F": "Fluoric","Se": "Selenic","Br": "Bromic","Te": "Telluric","I": "Iodic","Cl": "Chloric"}
anames_NM = {v: k for k, v in aroots_NM.items()}          

nmet_charge = {"C": 4,"N": 3,"O": 2,"F": 1,"P": 3,"S": 2,"Cl": 1,"As": 3,"Se": 2,"Br": 1,"Te": 2,"I": 1}

