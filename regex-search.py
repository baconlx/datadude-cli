
import sys

from datadude import datadude

filepath = sys.argv[0]
complicated_pattern = [0xF4, [0x88, 0xF3], ['0xFFFFFFFF00AB01', 0xAB,  ['*', 0xFF], 0xFF, {'test': 0x41}, [0xAB, "0x41", bytes([0x41]), 0xBA, ['?', bytes([0x99, 0x75, 0xA7, 0x5B]), 0x0A]], 0xAB], 0xAB]

selfcreated_pattern = datadude.clean_pattern(complicated_pattern)
pattern = datadude.Pattern(complicated_pattern)


target_file = datadude.FileResource(filepath)

target_file.search_pattern(selfcreated_pattern)
target_file.search_pattern(pattern)

# print(pattern)

# target_file = datadude.FileResource(filepath)
# print(target_file)

# target_file.search_pattern(selfcreated_pattern)
# target_file.search_pattern(pattern)


