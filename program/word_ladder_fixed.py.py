import re # Importing regular expression library
import queue
from warnings import warn


"""
Function which open file name passed to it by the run() function.
"""
def file_load(filename, length, banned_filename=""):
  # If the user desides to use banned words
  banned_words = []
  if banned_filename != "":
    banned_fd = open(banned_filename)
    lines = banned_fd.readlines()
    for line in lines:
      if len(line.rstrip()) == length:
        banned_words.append(line.rstrip())
    banned_fd.close()
  # Read in the words from dictionary 
  file = open(filename)
  lines = file.readlines()
  # Populate the dictionary
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == length and word not in banned_words:
      words.append(word)
  file.close()
  return words

# Function which returns number of letters and indexes in two word that match exactly
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])


# Function which iterate through all of the words in the words path and conduct a regular
#   expression search on each word using a pattern and ensuring it not already in the seen
#     dictionary or in the path directory.
def build(pattern, words, seen, path):
  return [word for word in words
          if re.search(pattern, word) and word not in seen.keys() and
          word not in path]

# Does not require regex pattern | Faster implementation for bfs
def build(words, visited, current_word):
  neighbors = set()
  for word in words:
    if word not in visited:
      if same(word, current_word) == len(word)-1:
        neighbors.add(word)
  return neighbors


"""
Function which:

 - Build a list using the build function of all teh possible variation of word
in the dictionary.
 - check to see which path of length the user has selected and adjust the algorithm accordingly.
 - Selects the best possible word to then add to the path list based on teh match value of a word from the same function.
  - Add words to the seen dictionary to ensure word duplication will not occur.
"""

def find(word, words, seen, target, path, outer_fitness=0):
  adjacent = []
  for i in range(len(word)):
    # For loop which iterate through the word's letters based on the length of the chosen word.
    adjacent += build(word[:i] + "." + word[i + 1:], words, seen, adjacent)
  if len(adjacent) == 0:
    return False
  # Sorted in reverse to put best candidate words first
  adjacent = sorted([(same(w, target), w) for w in adjacent], reverse=True)

  # Looks for target word
  for (match, item) in adjacent: # Iterating through match and word pairs in lists
    if match == len(target) - 1:
      path.append(item)
      return True
    seen[item] = True
  # Otherwise recurses through words in current path
  for (match, item) in adjacent:
    if match >= outer_fitness:
      path.append(item)
      if find(item, words, seen, target, path, match):
        return True
      path.pop()


def short_path(words, start_word, target_word):
  q = queue.Queue()
  visited = {}
  q.put([start_word])
  while q:
    path = q.get()
    vertex = path[-1]
    if vertex not in visited:
      visited[vertex] = True
    if same(vertex, target_word) == len(target_word)-1:
      return path
    neighbors = build(words, visited, vertex)
    for neighbor in neighbors:
      if neighbor not in visited:
        visited[neighbor] = True
        new_path = list(path)
        new_path.append(neighbor)
        q.put(new_path)


def init():
  # Input and validation
  #   Loop whcih gather all of the appropriate user input required for the program
  #     to run successfuly.
  start_word = input("Please enter start word: ").lower().rstrip()
  if not start_word.isalpha():
    warn("Input words cannot contain numbers or special characters", UserWarning)
    quit()
  end_word = input("Please enter target word: ").lower().rstrip()
  if not end_word.isalpha():
    """
    Statement that prompt the user for input which will determine whether  they will be given
    the longest path or the shortest path. Input is sanitised to make sure it is not a number
    or special character.
    """
    warn("Input words cannot contain numbers or special characters", UserWarning)
    quit()
  if start_word == end_word:
    warn("Start and target words cannot be the same", UserWarning)
    quit()
  if len(start_word) != len(end_word):
    warn("Start and target words must be the same length", UserWarning)
    quit()
  return [start_word, end_word]


# A function which prompt user for dictionary name then calls the file_load function,
#   Passing the file name into it as an arguments.
def run():
  # Get dictionary file name
  filename = input("Please enter dictionary name (without .txt): ")
  filename += ".txt"

  """
  Check file exists
  """
  file_desc = open(filename)
  file_desc.close()

  """
  Get User Input
  """
  user_input = init()

  """
  Extract word
  """
  start = user_input[0]
  end_word = user_input[1]

  # Used Banned Words File?
  banned_filename = input("Please enter a filename for banned words. (Press enter if not required): ")
  if len(banned_filename) != 0:
    banned_fd = open(banned_filename)
    banned_fd.close()
    banned = True
  else:
    banned = False

  # Generate the word list
  if banned:
    words = file_load(filename, len(start), banned_filename)
  else:
    words = file_load(filename, len(start))
  # Check if the target exists before searching for a path
  if end_word not in words:
    warn("Target word does not exist in the dictionary (You may have banned it?)", UserWarning)
    quit()

  # If statement which gather all the of the appropriate user input required for the program to run successfully.
  # Short or long path?
  path_option = input("Enter 'y' if you would like to evaluate a mininal path (Press enter if not required): ")
  if path_option.lower() == "y":
    path = short_path(words, start, end_word)
    path.append(end_word)
    print(len(path) - 1, path, sep='\t')
  else:
    path = [start]
    seen = {start: True}
    if find(start, words, seen, end_word, path):
      path.append(end_word)
      print(len(path) - 1, path, sep='\t')
    else:
      print("No path found")

# Main
if __name__ == "__main__":
  run()
