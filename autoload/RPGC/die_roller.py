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
    

def die_maker(die=None):
    #A function to split die into number - die type - bonus
    
    #if passed die is none, it is currently yanked
    if die == None:
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

def get_die_parts_by_name():
    die = vim.eval('@"')

    #split bonus from main die
    if '+' in die:
        die,bonus_text = die.split('+')
        bonus_text = '+{}'.format(bonus_text)
        bonus = int(bonus_text)
    elif '-' in die:
        die,bonus = die.split('-')
        bonus_text = '-{}'.format(bonus_text)
        bonus = -int(bonus_text)

    #search for the die definition in the file
    for line in vim.current.buffer[:]:
        if die in line and '=' in line:
            die_info=line.split('=')[1]
            n,dtype,trm = die_maker(die_info)

    print "rolling {}d{}{}".format(n,dtype,bonus_text)
    return [n,dtype,bonus]
        

        


#Get die data, retrun False if die infor is faulty

#first try by names
die_data = get_die_parts_by_name()
#if this fails, try by die notation
if not die_data:
    die_data = die_maker()


if die_data == False:
    print_error()
else:
    roll_die(die_data)
