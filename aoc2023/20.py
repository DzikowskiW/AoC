from collections import defaultdict
from copy import deepcopy
import math

UNKNOWN = 0
SWITCH = 1
CONVERTER = 2
BROADCASTER = 3
RESET = 4


def process(inputs):
    modules = defaultdict(list)
    switches = defaultdict(bool)
    converters = {}
    last_converter = None
    module_types = defaultdict(int)
    last_converter_high_count = defaultdict(int)
    #get converters
    for fr, _ in inputs:
        if fr[0] == '&':
            mname = fr[1:]
            converters[mname] = {}
    
    #map inputs
    for fr, to in inputs:
        mname = None
        if fr == 'broadcaster':
            module_types[fr] = BROADCASTER
            mname = fr
        elif fr[0] == '%':
            mname = fr[1:]
            module_types[mname] = SWITCH
        elif fr[0] == '&':
            mname = fr[1:]
            module_types[mname] = CONVERTER
            switches[mname] = False
        else:
            continue
        for m in to:
            if m == 'rx':
                last_converter = mname
            modules[mname].append(m)
            if m in converters:
                converters[m][mname] = False
    
    lows = 0
    highs = 0
    
    def button_press(it):
        nonlocal highs, lows
        pulses = [('button', 'broadcaster', False)]
        count = 0
        while pulses:
            from_module, module, t = pulses.pop(0)
            # print(from_module, '-', t,'->', module)
            if t:
                highs += 1
            else:
                lows += 1
            nxt_t = t
            if module_types[module] == CONVERTER:    
                converters[module][from_module] = t
                #checking part 2
                if module == last_converter and t:
                    if last_converter_high_count[from_module] == 0:
                        last_converter_high_count[from_module] = it
                        if len(last_converter_high_count) == len(converters[module]):
                            return False
                #end checking part 2
                nxt_t = not all(converters[module].values())
                for m in modules[module]:
                    pulses.append((module, m, nxt_t))
            elif module_types[module] == SWITCH:
                if t == True:
                    continue
                switches[module] = not switches[module]
                nxt_t = switches[module]
                for m in modules[module]:
                    pulses.append((module, m, nxt_t))
            elif module_types[module] == BROADCASTER:
                for m in modules[module]:
                    pulses.append((module, m, nxt_t))                
            else:
                if module == 'rx' and t == False:
                    return False
        return True
    
    i = 0
    while True:
        i+=1
        if not button_press(i):
            print('part 2', math.lcm(*last_converter_high_count.values()))
            return
        if (i == 1000):
            print('part 1', highs * lows)

with open("input/20.txt") as f:
    lines = f.read().rstrip().split('\n')
    lines = [(fr, to.split(', '))for fr, to in (l.split(' -> ') for l in lines)]
    
    process(lines)
