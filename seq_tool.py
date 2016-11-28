
# coding: utf-8

# In[49]:

def szetvago(szoveg):
    f = open(szoveg).read()
    #print(f)
    #str(f)
    output_szoveg = str()
    for word in f.split('.'): #.decode("utf-8"): #.split(',').split('!').split('?').decode("utf-8"):
            output_szoveg.join(word)
    return output_szoveg
    #f.close()

szetvago("data/piszkos_fred.txt")


# In[13]:

def mondatokra(szoveg):
    mondatok = []
    for punct in ".?":
        szoveg = szoveg.strip().replace(punct, "!")
    for mondat in szoveg.split("!"):
        if mondat.strip():
            mondatok.append(mondat.strip())
    return mondatok


# In[7]:

def szavakra(mondat):
    szavak = mondat.split()
    strippelt_szavak = []
    for szo in szavak:
        strippelt_szavak.append(szo.strip(",.()"))
    return strippelt_szavak


# In[6]:

def feldolgoz(fajl):
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        kimenet.append(szavak)
    return kimenet


# In[1]:

def joe(fajl):
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        for index, item in enumerate(szavak):
            if szavak[index].istitle() == True:
                szavak[index] = "Joe"
        kimenet.append(szavak)
    return kimenet


# In[25]:

matrix = [ [1,0,0], [0,1,0], [0,0,1] ]

def symet(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return "False"

    return "True"


# In[48]:

matrix = [ [1,2,3,4], [0,1,0,0], [3,2,1,0] ]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print matrix[i][j],
    print '\n'

transpose=[]
for j in range(len(matrix[0])):
    transpose.append([])
    for i in range (len(matrix)):
        x=matrix[i][j]
        transpose[j].append(x)
print '\n'

for i in range (len(matrix[0])):
    for j in range (len(matrix)):
        print transpose[i][j],
    print '\n'


# In[58]:

def transpose(matrix):
    n = len(matrix)
    k = len(matrix[0])
    new_matrix = []
    for i in range(k):
        new_row = []
        for old_row in matrix:
            new_row.append(old_row[i])
        new_matrix.append(new_row)
    return new_matrix


# In[150]:

data = open('data/movies.tsv').readlines()
data = [line.strip().split("\t") for line in data]
data = [[title.strip(), int(year), genres.split(',')] for title, year, genres in data]

from collections import defaultdict, OrderedDict
d = defaultdict(int)

from collections import defaultdict
d = defaultdict(int)
for movie, year, genres in data:
    for genre in genres:
        d[genre] += 1
        d[year] += 1
        d[movie] += 1


# In[165]:

data = open('data/sample_text.txt').readlines()
data = [line.strip().split() for line in data]

from collections import defaultdict
d = defaultdict(int)


# In[12]:

def process_data(fn):
    data = {}
    f = open(fn)
    for line in f:
        title, year, genres = line.strip().split("\t")
        title = title.strip()
        year = int(year)
        genres = genres.split(",")
        #print title, year, genres
        #break
        for genre in genres:
            if genre not in data:
                data[genre] = []
            data[genre].append((title,year))
    return data


# In[32]:

def build_index(data):
    for movie in data:
        letter_index = {}
        title = movie[0]
        try:
            a, b, c = title[:3]
        except ValueError:
            print "skipping: {0}".format(title)
            continue
        if a not in letter_index:
            letter_index[a] = {}
        if b not in letter_index[a]:
            letter_index[a][b] = {}
        if c not in letter_index[a][b]:
            letter_index[a][b][c] = []
        letter_index[a][b][c].append(movie)
        
def search(fn):
    data = [(title.strip(), int(year), genres.split(",")) 
            for title, year, genres in [line.strip().split("\t") 
                                        for line in open(fn)]]
    letter_index = build_index(data)
    letter1 = raw_input()
    print letter_index[letter1]
    letter2 = raw_input()
    print letter_index[letter1][letter2]
    letter3 = raw_input()
    print letter_index[letter1][letter2][letter3]


# In[2]:

def query():
    last_name = raw_input()
    first_name = raw_input()
    year = int(raw_input())
    hobby = raw_input()
    return last_name, first_name, year, hobby

from collections import OrderedDict
data = OrderedDict()
while True:
    last_name, first_name, year, hobby = query()
    if last_name not in data:
        data[last_name] = (first_name, year, hobby)
    else:
        first_guy = data[last_name]
        if first_gux[0] == first_name:
            data[last_name] = (first_name, year, hobby)
        else:
            first_key = "{0}_{1}".format(last_name, first_guy[0])
            data[first_key] = first_guy
            second_key = "{0}_{1}".format(last_name, first_guy[0])
            data[second_key] = (first_name, year, hobby)
            del data[last_name]
        
    print data
    

