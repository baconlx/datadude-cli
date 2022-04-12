import re
from datadude import datadude

testpatterns = [
    0xDB,
    [0xDB],
    [0xDB, 0xAB],
    [0xAB, 0xEC, '*', 0xDB],
    [0xF4, 0x88, '?', 0x3B, '?48', 0x17, 0x10, 0x58, 0xC4],
    [0xF4, [0x88, 0xF3], ['0xFFFFFFFF00AB01', 0xAB,  ['*', 0xFF], 0xFF, {'test': 0x41}, [0xAB, "0x41", bytes([0x41]), 0xBA, ['?', bytes([0x99, 0x75, 0xA7, 0x5B]), 0x0A]], 0xAB], 0xAB],
    '0xFFFF',
    '0xadf213423',
    '0xAFAFG',
    [1, 2, 3, True, False, (1, [1, 234], 3)]
]

for num, orig_pattern in enumerate(testpatterns):
    print("------------------------------")
    print("processing pattern " + str(num+1))

    try:
        valid_pattern = datadude.clean_pattern(orig_pattern)
        print(valid_pattern)

    except Exception as e:
        print("datadude error: " + str(e))

