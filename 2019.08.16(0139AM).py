import re
from pathlib import Path



def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def inimatch(start,target):
  return len([c for (c, t) in zip(start, target) if c == t])

def find(word, words, seen, target, path):
  matched = inimatch(start,target)
  pword = word
  list = []
  while matched != len(target):
    for i in range(len(word)):
      list += build(pword[:i] + "." + pword[i + 1:], words, seen, list)
      print(list)
    if len(list) == 0:
      return False
    list = sorted([(same(w, target), w) for w in list])
    ##print(list)
    for (match, item) in list:
      #this part down
      if match == matched + 1:
        #make a line that find the word which match the most to append
        path.append(item)
        matched += 1
        pword = item
        #print("THIS IS",path)

    ########PROBLEM 1: while loop is not running ########
    else:
      return True




fname = input("Enter dictionary name: ")
myfile = Path(fname)
#This while loop below attributes to check if file exists
while myfile.is_file():
  break
else:
  fname = input("Wrong dictionary path, Enter dictionary name: ")
  myfile = Path(fname)
  myfile.is_file()
file = open(fname)
while True:
  lines = file.readlines()
#To translate the txt file into lines of words
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
#words[] is a list contains words that have equal len with start word
  target = input("Enter target word:")
  while len(target) != len(start):
    if len(target) < len(start):
      target = input("Target word is too short, enter target word: ")
    elif len(target) > len(start):
      target = input("Target word is too long, enter target word: ")
  break


count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

#######PROBLEM 2: There is no function and list for seen item########