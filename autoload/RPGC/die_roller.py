import vim
from numpy.random import randint

def print_error():
    print """
    Something faulty, use proper die format\n
    Some examples:
        1d6
        1d20+1
        3d6-2
    Currently, only one die type is possible
    """

def roll_die(die):
    n,dtype,bonus = die
    out = 0
    i = 0
    while n > i:
        v = randint(1,dtype+1)
        out += v
        print '{}) result: {}, total: {}'.format(i,v,out)
        i += 1

    print '-'*5
    print 'total: {}'.format(out+bonus)
    

def die_maker():
    #A function to split die into number - die type - bonus
    die = vim.eval('@"')
    try: 
        n,rest = die.split('d')
    except ValueError: 
        print "More than one d, can't be handled yet"
        return False
    if n.strip() == '':
        n = '1'
    #Generate bonus
    if '-' in rest:
        dtype,bonus = rest.split('-')
        bonus = '-'+bonus
    elif '+' in rest:
        dtype,bonus = rest.split('+')
    else:
        dtype,bonus = rest,0
    
    try:
        return [int(v) for v in n,dtype,bonus]
    except ValueError:
        return False


#Get die data, retrun False if die infor is faulty
die_data = die_maker()

if die_data == False:
    print_error()
else:
    roll_die(die_data)
