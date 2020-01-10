# 单牌
# 对子
# 三张
# 顺子
# 炸弹：四张，王炸
# 连对
# 三带一
# 三带对
# 飞机
# 四带二


import re

_rules = {
    1: ['dan'],
    2: ['dui', 'zd'],
    3: ['san'],
    4: ['zd', 'sdy'],
    5: ['sz', 'sdd'],
    6: ['sz', 'ld', 'side', 'fj'],
    7: ['sz'],
    8: ['sz', 'ld', 'side', 'fj'],
    9: ['sz', 'fj'],
    10: ['sz', 'ld', 'fj'],
    11: ['sz'],
    12: ['sz', 'ld', 'fj'],
    14: ['ld'],
    15: ['fj'],
    16: ['ld', 'fj'],
    18: ['ld', 'fj'],
    20: ['ld', 'fj']
}

_compares = {
    'dan': 'first',
    'dui': 'first',
    'san': 'first',
    'sz': 'first',
    'zd': 'first',
    'ld': 'first',
    'sdy': 'second',
    'sdd': 'second',
    'fj': 'second',
    'side': 'third'
}

poker_value = ['3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A', '2', 'B', 'R']


def get_value(pokers):
    p_value = ''
    pokers = sorted(pokers, key=lambda x:poker_value.index(x[0]), reverse=True)
    for poker in pokers:
        p_value += poker[0]
    return p_value

def get_power(values):
    p_power = []
    for i in values:
        p_power.append(poker_value.index(i))
    return p_power


def dan_valid(pokers):
    pattern = r'^[02-9JQKABR]$'
    if re.search(pattern, pokers) is None:
        return False
    else:
        return True


def dui_valid(pokers):
    pattern = r'^([02-9JQKA])\1$'
    if re.search(pattern, pokers) is None:
        return False
    else:
        return True


def sz_valid(pokers):
    pattern = r'^[03-9JQKA]{5,12}$'
    if re.search(pattern, pokers) is None:
        return False
    else:
        for i in range(len(pokers) - 1):
            if poker_value.index(pokers[i]) - poker_value.index(pokers[i + 1]) != 1:
                return False
        return True


def ld_valid(pokers):
    pattern = r'^([03-9JQKA])\1([03-9JQKA])\2([03-9JQKA])\3[03-9JQKA]*$'
    if re.search(pattern, pokers) is None:
        return False
    else:
        for i in range(len(pokers) - 3, 0, -2):
            if poker_value.index(pokers[i]) - poker_value.index(pokers[i + 2]) != 1:
                return False
        return True


def san_valid(pokers):
    pattern = r'^([02-9JQKA])\1{2}$'
    if re.search(pattern, pokers) is None:
        return False
    else:
        return True


def sdy_valid(pokers):
    pattern1 = r'^([02-9JQKA])\1{2}[02-9JQKABR]$'
    pattern2 = r'^[02-9JQKABR]([02-9JQKA])\1{2}$'
    if re.search(pattern1, pokers) is None and re.search(pattern2, pokers) is None:
        return False
    else:
        return True


def sdd_valid(pokers):
    pattern1 = r'^([02-9JQKA])\1{2}([02-9JQKA])\2$'
    pattern2 = r'^([02-9JQKA])\1([02-9JQKA])\2{2}$'
    if re.search(pattern1, pokers) is None and re.search(pattern2, pokers) is None:
        return False
    else:
        return True


def side_valid(pokers):
    pattern = r'([02-9JQKA])\1{3}'
    si = re.findall(pattern, pokers)
    er = re.sub(pattern, '', pokers)
    if si is None:
        return False
    else:
        pattern1 = r'^[02-9JQKABR]{2}$'
        pattern2 = r'^([02-9JQKA])\1([02-9JQKA])\2$'
        if re.search(pattern1, er) is None and re.search(pattern2, er) is None:
            return False
        return True


def fj_valid(pokers):
    pattern = r'([02-9JQKA])\1{2}'
    pattern2 = r'([02-9JQKA])\1'
    sans = re.findall(pattern, pokers)
    dais = re.subn(pattern, '', pokers)
    if sans is None:
        return False
    if dais[0] and len(dais[0]) != dais[1] and len(re.findall(pattern2, dais[0])) != dais[1]:
        return False
    else:
        for i in range(len(sans) - 1):
            if poker_value.index(sans[i][0]) - poker_value.index(sans[i+1][0]) != 1:
                return False
        return True

def zd_valid(pokers):
    pattern = r'^([02-9JQKA])\1{3}$'
    if re.search(pattern, pokers) != None:
        return True
    elif re.search(r'^RB$', pokers):
        return True
    return False

def first_compare(sj, zj):
    '''dan,dui,san,ld,sz,zd'''
    sj = get_power(sj)
    zj = get_power(zj)
    if zj > sj:
        return True
    else:
        return False

def second_compare(sj, zj):
    '''sdy,sdd,fj'''
    pattern = r'([02-9JQKA])\1{2}'
    sj_sans = re.findall(pattern, sj)
    zj_sans = re.findall(pattern, zj)
    sj_sans = get_power(sj_sans)
    zj_sans = get_power(zj_sans)
    if zj_sans > sj_sans:
        return True
    else:
        return False

def third_compare(sj, zj):
    '''side '''
    pattern = r'([02-9JQKA])\1{3}'
    sj_sis = re.findall(pattern, sj)
    zj_sis = re.findall(pattern, zj)
    sj_sis = get_power(sj_sis)
    zj_sis = get_power(zj_sis)
    if zj_sis > sj_sis:
        return True
    else:
        return False

def check(pokers):
    pokers = get_value(pokers)
    for t in _rules[len(pokers)]:
        if eval(t + '_valid')(pokers):
            return t
    return False

def compare(sj, zj, sj_type, zj_type):
    sj = get_value(sj)
    zj = get_value(zj)
    if zj == 'RB':
        return True
    elif sj_type != 'zd' and zj_type == 'zd':
        return True
    elif sj_type != zj_type:
        return False
    elif len(sj) != len(zj):
        return False
    return eval(_compares[sj_type] + '_compare')(sj, zj)

