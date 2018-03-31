## import

import numpy as np
import matplotlib.pyplot as plt

## lists declaration

names = ['Aquaman', 'Ant-Man', 'Batman', 'Black Widow',
         'Captain America', 'Daredavil', 'Elektra', 'Flash',
         'Green Arrow', 'Human Torch', 'Hancock', 'Iron Man',
         'Mystique', 'Professor X', 'Rogue', 'Superman',
         'Spider-Man', 'Thor', 'Northstar']

years = [1941, 1962, None, None, 1941,
         1964, None, 1940, 1941, 1961,
         None, 1963, None, 1963, 1981,
         None, None, 1962, 1979]

## association and sorting

couples,i = [],0
for i in range(0,len(names)):
  couples += [(names[i],years[i])]
couples.sort(key=lambda n:n[0][1]) # sorting alphabetically (second letter)
couples = [(n,y) for (n,y) in couples if y and y > 1960] # removing None and filter
print(couples)
         
## function decleration

def abs_freq(seq):
  counts = {}
  for i in seq:
    if i:
      if i in counts:
        counts[i] += 1
      else :
        counts[i] = 1
  return sorted(counts.items(), key=lambda n : n[1], reverse=True)

print(np.array(abs_freq(years)).transpose())

## plot and graphic

x,y=np.array(abs_freq(years)).transpose()
plt.bar(x,y)
#plt.show()

## playing with fun

def get_indexes(seq,key):
  res,index = [],0
  for i in seq:
    if i == key:
      res += [index]
    index += 1
  return res

def abs_freq_with_name(seq_name,seq_year):
  counts = {}
  for y in seq_year:
    if y not in counts:
      counts[y] = [seq_name[i] for i in get_indexes(years,y)]
  return counts

print(abs_freq_with_name(names,years)[1941])

def print_films_after_year(films,year):
  del films[None]
  for (y,n) in sorted(films.items()):
    if y > year:
      for i in films[y]:
        print(i+" ("+str(y)+")")

print_films_after_year(abs_freq_with_name(names,years),1970)
