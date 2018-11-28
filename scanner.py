import os
import re
import sys

in_filename = None
min_freq = 5

if (len(sys.argv) < 2):
	print("ERROR: Expected 'scanner.py <in_file.txt>'")
	exit()

in_filename = sys.argv[1]
	
freqs = {}
print("---\n")

with open(in_filename, "r", encoding="utf8", errors="ignore") as file:
        all_lines = file.readlines()
        phrase_length = 1
        len_valid = True
        while len_valid:
                len_valid = False
                for line in all_lines:
                        line = re.split('\s+', line)
                        for i in range(len(line) - phrase_length + 1):
                                phrase = ''
                                for j in range(phrase_length):
                                        word = re.sub('\W+','',line[i+j]).lower()
                                        if len(word) > 1:
                                                phrase += word + ' '
                                phrase = phrase[0:-1]
                                if (len(phrase) > 3):
                                        freqs[phrase] = freqs.get(phrase, 0) + 1
                                        if (freqs[phrase] > min_freq):
                                                len_valid = True
                phrase_length += 1
                                        

sort = sorted(freqs.items(), key = lambda entry: (entry[1],entry[0]), reverse = False)
for (key, val) in sort:
	if (val > min_freq):
		print("{} --> {}".format(key, val))
