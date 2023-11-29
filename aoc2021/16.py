import numpy as np
HEXBIN = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

def calculate(op, args):
    if op == 0: return sum(args)
    if op == 1: return np.prod(args)
    if op == 2: return min(args)
    if op == 3: return max(args)
    if op == 5: return 1 if args[0] > args[1] else 0 
    if op == 6: return 1 if args[0] < args[1] else 0 
    if op == 7: return 1 if args[0] == args[1] else 0 
    assert(False)

def hexToBin(hex):
    out = ''
    for h in hex:
        out += HEXBIN[h]
    return out

def parseVersions(packet):
    #get version
    ver = int(packet[:3], 2)
    versum = ver
    typeId = int(packet[3:6], 2)
    value = 0
    # print('packet', ver, packet)
    posChange = 6
    if (typeId != 4):
        # print('operator')
        #find position of subpacket
        lengthTypeId = int(packet[6:7], 2) #TODO READ OPERATOR AND USE IT
        posChange += 1
        args = []
        if lengthTypeId == 0:
            # print('bit len')
            #next 15 bits - total length in bits of sub-packets
            posChange += 15
            subPacketsLen = int(packet[7:22], 2)
            maxLen = posChange + subPacketsLen
            while maxLen > posChange:
                (packPosChange, packVerSum, packValue) = parseVersions(packet[posChange:])
                versum += packVerSum
                posChange += packPosChange
                args.append(packValue)
        else:
            # print('num of subs')
            #next 11 bits - number of subpackets
            subPacketNum = int(packet[7:18], 2)
            posChange += 11
            for i in range(subPacketNum):
                (packPosChange, packVerSum, packValue) = parseVersions(packet[posChange:])
                versum += packVerSum
                posChange += packPosChange
                args.append(packValue)
        
        value = calculate(typeId, args)

    else:
        # print('literal val')
        litStart = posChange
        literalVal = ''
        checkNext = True
        while checkNext:
            if (packet[posChange] == '0'):
                checkNext = False 
            literalVal += packet[(posChange+1):(posChange+5)]
            posChange += 5
        # print('litval',int(literalVal,2))
        value = int(literalVal,2)
    return (posChange, versum, value)

def p1(transmission):
    return parseVersions(hexToBin(transmission))



with open("16.txt") as f:
    lines = [x.strip() for x in f]
    transmission = ''
    for line in lines:
        transmission += line
    print(transmission)
    assert(p1('C200B40A82')[2] == 3)
    assert(p1('04005AC33890')[2] == 54)
    assert(p1('880086C3E88112')[2] == 7)
    assert(p1('CE00C43D881120')[2] == 9)
    assert(p1('F600BC2D8F')[2] == 0)
    assert(p1('9C005AC2F8F0')[2] == 0)
    assert(p1('9C0141080250320F1802104A08')[2] == 1)
    

    print('P1', p1(transmission))
    #print('P2', p2(startTxt, assgn, 40))