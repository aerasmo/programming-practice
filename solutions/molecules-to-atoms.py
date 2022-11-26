import re
def parse_molecule (formula):
    atoms = {}
    res = [r'(?=\()(\((?:[A-Z][a-z]?\d?)*\))(\d?)', r'(?=\[)(.*\])(\d?)', r'(?=\{)(.*\})(\d?)']
        
    for element_re in res:
        elements = re.findall(element_re, formula)
        print(elements)
        if elements:
            for tup in elements:                    
                elements = tup[0].strip('([{}])')
                multiplier = tup[1]
                if not multiplier:
                    multiplier = 1
                atoms = count(elements)
                for key, val in atoms.items():
                    atoms[key] = int(val) * int(multiplier)
                
                subformula = stringify(atoms)
                if int(multiplier) > 1:
                    formula = formula.replace(tup[0] + str(multiplier), subformula)    
                else:   
                    formula = formula.replace(tup[0], subformula)
                
                print('formula', formula)
        
    else:
        print('formula', formula)
        
    atoms = count(formula)
    print('final', formula)   
    return formula
    
def count(formula):
    element_re = r'([A-Z][a-z]?)(\d*)?'
    elements = re.findall(element_re, formula)
    atoms = {}
    for tup in elements:
        key = tup[0]
        atoms.setdefault(key, 0)
        count = tup[1]
        if not count:
            count = 1
        atoms[key] += int(count)
    print('atoms', atoms)  
    return atoms
    
#def build(tuplist):

    
def stringify(atoms):
    string = ''
    for key, val in atoms.items():
        string += key + str(atoms[key])
    return string
