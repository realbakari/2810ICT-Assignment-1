import re
from pathlib import Path



def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen and
                    word not in list]

def inimatch(start,target):
  return len([c for (c, t) in zip(start, target) if c == t])

def find(word, words, seen, target, path,matched):

  pword = word
  list = []

  for i in range(len(word)):
      list += build(pword[:i] + "." + pword[i + 1:], words, seen, list)

  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  print(list)
  print(matched)
  for (match, item) in list:
      #this part down
    if matched > list[-1][0]:
        matched -= 1
        print("matched - 1")

    elif list[-1][0] == matched:
        if match == matched:
          path.append(item)
          seen.append(item)
          matched -= 1
          print("first")
          break

    elif match == matched + 1:
        #make a line that find the word which match the most to append
        path.append(item)
        seen.append(item)
        print("second")
        break



    elif match == 0 or matched -1:
        seen.append(item)
        print("third")


        #print("THIS IS",path)


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
matched = inimatch(start,target)

count = 0
path = [start]
seen = [start]

find(start, words, seen, target, path, matched)
while path[-1] != target:
    print(path)
    matched += 1
    find(path[-1], words, seen,target, path,matched)
else:
    print(len(path) - 1, path)


#######PROBLEM 2: There is no function and list for seen item########