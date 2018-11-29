import os
import re
import sys

if (len(sys.argv) < 4):
	print("ERROR: Expected 'scanner.py <phrase_len> <min_freq> <in_file.txt>'")
	exit()

phrase_length = int(sys.argv[1])
min_freq = int(sys.argv[2])
in_filename = sys.argv[3]
	
freqs = {}
print("---\n")

with open(in_filename, "r", encoding="utf8", errors="ignore") as file:
        all_lines = file.readlines()
        len_valid = True
        while len_valid:
                len_valid = False
                for line in all_lines:
                        line = re.split('\s+', line)
                        for i in range(len(line) - phrase_length + 1):
                                arr = []
                                for j in range(phrase_length):
                                        word = re.sub('\W+','',line[i+j]).lower()
                                        if (len(word) > 0):
                                                arr.append(word)
                                if (len(arr) >= phrase_length):
                                        phrase = ''
                                        for word in arr:
                                                phrase += word + ' '
                                        phrase = phrase[0:-1]
                                        freqs[phrase] = freqs.get(phrase, 0) + 1
                                        if (freqs[phrase] >= min_freq):
                                                len_valid = True
                phrase_length += 1
                                        

sort = sorted(freqs.items(), key = lambda entry: (entry[1],entry[0]), reverse = True)
for (key, val) in sort:
	if (val > min_freq):
		print("{} --> {}".format(key, val))
