import re
import vim
from numpy.random import randint

def print_error():
    print """
    Something faulty, use proper die format\n
    Some examples:
        1d6
        1d20+1
        3d6-2
    Currently, only one die type is supported
    """


def roll_dice(roll_data):
    total = 0
    bonus = die_data['mod']
    for key in ['add','sub']:
        for i in range (len(die_data[key])):
            if not 'd' in die_data[key][i]: continue
            #All the fixed bonuses are placed in 'mod'
                
            n,d = die_data[key][i].strip().split('d')
            if n == '':
                n = 1
            else:
                n = int(n)
            d = int(d)
            for i in range (n):
                print 'd{}: '.format(d),
                res = randint(1,d+1)
                total += res
                print 'result={}, total={}'.format(res,total)
    print '-'*10
    print 'Total+bonus={}'.format(total+bonus)
            
    return
    

def get_bonus(die_string):

    """ A function to split a string based on + and - signs
    returns a dict with 'add' and 'sub' keys"""

    out = {'add':[],'sub':[],'mod':0}
    
    target = 'add'
    while '+' in die_string or '-' in die_string:
        nextp = die_string.find('+')
        nextm = die_string.find('-')

        if nextp < nextm and nextp > 0 or nextm < 0:
            to_put,die_string = die_string.split('+',1)
            out[target].append(to_put)
            target = 'add'

        else:
            to_put,die_string = die_string.split('-',1)
            out[target].append(to_put)
            target = 'sub'

    out[target].append(die_string)        
    return out

def die_from_text(die_text):
    """ A function to check if a certain text is a die, a bonus, or a predefined
    die. If the latter is the case, the function would return the die
    definition"""

    #Checking if this follows a regular die notation or a simple bonus
    if re.match("[0-9]*d[0-9]*",die_text):
        return die_text
    elif re.match("[0-9]+",die_text):
        return die_text
    #Not a die, searching for the die definition
    lnum = 0
    n0 = 0
    pre = ''
    while '.' in die_text:
        first,die_text = die_text.split('.',1)
        n0 += 1
        pre = '*'*n0 
        pattern = '^' + '\*'*n0 + '[^\*]'

        while lnum < len(vim.current.buffer):
            line = vim.current.buffer[lnum]
            if re.match(pattern,line) and first in line:
                lnum += 1
                break 
            lnum += 1

        
    for line in vim.current.buffer[lnum:]:
        if die_text in line and '=' in line:
            die_info=line.split('=')[1]
            #definition found, return it
            return die_info
        if n0>0 and re.match(pattern,line):
            break
    



def die_converter():
    die = vim.current.line.strip()

    #split bonus from main die
    die_parts = get_bonus(die)
    
    #replace predefined dies and bonuses with die notation
    for key in ['add','sub']:
        for i in range (len(die_parts[key])):
            die_data = die_from_text(die_parts[key][i])
            die_parts[key][i] = die_data
            try: #Checking if this is a simple numerical value
                #yes add it
                die_data = int(die_data)
                if key == 'add':
                    die_parts['mod'] += die_data
                else:
                    die_parts['mod'] -= die_data
            except ValueError:
                #no, place it in the appropriate list
                pass
    return die_parts
    

    

        

        


#Get die data, retrun False if die infor is faulty
die_data = die_converter()
if not die_data:
    print_error()
else:
    roll_dice(die_data)


#if die_data == False:
#    print_error()
#else:
#    roll_die(die_data)
