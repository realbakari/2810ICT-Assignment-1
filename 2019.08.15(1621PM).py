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
  list = []
  matched = inimatch(start,target)
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  print(list)
  for (match, item) in list:
    #this part down
    if match > matched:
      #make a line that find the word which match the most to append
      path.append(item)
      matched += 1
        #print("THIS IS",path)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

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
  target = input("Enter target word:")
  break


count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

