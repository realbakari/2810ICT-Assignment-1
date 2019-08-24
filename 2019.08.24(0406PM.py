import re
from pathlib import Path
import copy


def same(item, target):
  #this function will return a number that represent the matched char between first and second element
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list,path):
  ## Build function create a list where inculd words that satisfy the pattern
  return [word for word in words
                 if re.search(pattern, word) and word not in seen and
                    word not in list and word not in path]

def inimatch(start,target):
  ##basically the alike function as same function, but this only use once for getting initial match number
  return len([c for (c, t) in zip(start, target) if c == t])

def find(word, words, seen, target, path):
  ##this is the main function that finds the path
  list = []
  ##this list contains words that ready to be choose into path
  wmatched = len([c for (c, t) in zip(path[-1], target) if c == t])
  ##wmatched means word matched, it helps to understand how many words match between current word and target
  for i in range(len(word)):
      list += build(word[:i] + "." + word[i + 1:], words, seen, list,path)
  if len(list) == 0:
    path.append(target)

  list = sorted([(same(w, target), w) for w in list])
  ##this sorted part puts match number and word into a list
  if wmatched == len(target)-1:
    path.append(target)
    return
    ##this part above check if the word is already one match away from the target,
    ##if so, it will apend target to the end of path and finalise this attempt
  for (match, item) in list:

    if wmatched > list[-1][0]:
        seen.append(item)
        #if all values in the list are not wmatched to the requirment

    elif list[-1][0] == wmatched:
        if match == wmatched:
          path.append(item)
          seen.append(item)
          break
          #if the biggest value has the same match as current match

    elif match == wmatched + 1:
        if list.count(wmatched+1) > 1:
          path.append(item)
          seen.append()
          break
        #make a line that find the word which match the most to append
        else:
          path.append(item)
          break



    elif match == 0 or wmatched -1:
        seen.append(item)


        #If the value has 0 match or 1 below the current match


  else:
    return True




def wordladder(path,result):
    find(start, words, seen, target, path)
    #this while loop keeps running untill it found the path
    while path[-1] != target:
      find(path[-1], words, seen, target, path)
    else:
      if len([c for (c, t) in zip(path[-2], path[-1]) if c == t])!=len(target)-1:
        ##this if statement make sure the path is correct
        path.clear()
        path.append(start)
        return
      else:
        s = []
        for i in path:
          if i not in s:
            s.append(i)
        result.append([len(s) - 1, s[:]])
        ##this statement remove all duplicated elements
        path.clear()
        path.append(start)
        s.clear()



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
wmatched = matched
count = 0
path = [start]
seen = [start]
result = []




while count < 5:
  ##run 5 times and pick the fastest way
  wordladder(path,result)
  count += 1
  matched = wmatched
else:
  print(min(result))



