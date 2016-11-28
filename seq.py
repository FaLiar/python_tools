
# coding: utf-8
#sdaasdasdasdasdasdasdasdasdDDZZZZ

# In[49]:




# In[2]:

def mondatokraaaa(szoveg):
    mondatok = []
    for darab1 in szoveg.split("."):
        for darab2 in szoveg.split("!"):
            for darab3 in szoveg.split("?"):
                if darab3.strip():
#tatat
                    mondatok.append(darab3.strip())
    return mondatok    


# In[13]:

def mondatokra2(szoveg):
    mondatok = []
    for punct in ".?":
        szoveg = szoveg.strip().replace(punct, "!")
    for mondat in szoveg.split("!"):
        if mondat.strip():
            mondatok.append(mondat.strip())
    return mondatok


# In[7]:

szoveg = open('data/sample_text.txt').read()


# In[48]:

mondatokra2(szoveg)[0][:1000]


# In[49]:

mondatokra2(szoveg)


# Define a function that splits sentences into words, and strips punctuation marks (",", ";", etc.) from edges of words.

# In[7]:

def szavakra(mondat):
    szavak = mondat.split()
    strippelt_szavak = []
    for szo in szavak:
        strippelt_szavak.append(szo.strip(",.()"))
    return strippelt_szavak


# Use the last two functions in one that takes a filename as its argument and returns the text in the file as a list of lists. Test it on the file "data/sample_text.txt"

# In[6]:

def feldolgoz(fajl):
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        kimenet.append(szavak)
    return kimenet


# In[10]:

adat = feldolgoz("data/sample_text.txt")[0][:10]


# In[11]:

adat[:3]


# ### 4.1.2
# Use the functions defined in __4.1.1__ and define a function that goes through a text and replaces all proper names (capitalized words not at the beginning of a sentence) with "Joe". Print the first few sentences to test your solution.

# In[8]:

def joe2(fajl):
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        for index, item in enumerate(szavak):
            if szavak[index].istitle() == True:
                szavak[index] = "Joe"
        kimenet.append(szavak)
    return kimenet

    
joe2("data/sample_text.txt")[0][:10]


# In[9]:

def asd(fajl):
    kimenet = []
    adat = feldolgoz(fajl)
    for mondat in adat:
            uj_mondat = []
            uj_mondat.append(mondat[0])
            for szo in mondat[1:]:
                if szo.istitle():
                    uj_mondat.append("Joe")
                else:
                    uj_mondat.append(szo)
            kimenet.append(uj_mondat)
    return kimenet    


# In[12]:

asd("data/sample_text.txt")[0][-20:]


# ### 4.1.3
# Load the sample text using your function from __4.1.1__ and create a game where the user is shown a half of a word in a small context (e.g. "_Many solu\*\*\*\*\* were suggested_") and has to guess the full word (don't worry about randomization, your solution can come up with the same questions every time).

# In[ ]:




# ## 4.2 Lists
# <a id='4.2'></a>

# ### 4.2.1
# Define a function that takes as its input a list of $n$ lists of $n$ numbers (a square matrix) and decides if it is symmetric (i.e. $A[i,j] == A[j,i]$ for all $i, j$).

# In[23]:

matrix2 = [ [1,0,0], [0,1,0], [0,0,1] ]

matrix2 == map(list, zip(*matrix2))


# In[25]:

matrix = [ [1,0,0], [0,1,0], [0,0,1] ]

def symet(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return "False"

    return "True"


symet(matrix)


# ### 4.2.2
# Define a function that takes a list containing lists of equal length (i.e. a table of size $n\times k$) and "transposes" it, creating a table of size $k\times n$.

# In[32]:

matrix = [ [1,0,0,0], [0,1,0,0], [0,0,1,0] ]
print(len(matrix))
print(len(matrix[0]))


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


# In[59]:

matrix = [ [1,0,0,0], [0,1,0,0], [0,0,1,0] ]
transpose(matrix)


# ### 4.2.3
# Redo 4.2.2 using nested list comprehension!

# In[61]:

def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])]


# ### 4.2.4

# Define a function that takes a list and string, then returns all elements that start with the string, along with their indices in the list.

# In[ ]:

def parosito(lista,szo)
    


# ## 4.3 Dictionaries
# <a id='4.3'></a>

# ### 4.3.1
# Use a dictionary to count words in our sample text (use your text processing functions!). Then print the most common words, along with their frequencies!

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


# In[6]:

data


# ### 4.3.2

# Define function that performs the factorial operation ($n!$) but caches all results so that each call requires the least possible number of multiplications.

# In[ ]:




# ### 4.3.3
# Read the dataset in "data/movies.tsv" and store it in a dictionary whose keys are genres and the values are list of tuples of title and year

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


# In[13]:

data = process_data("data/movies.tsv")


# In[14]:

data["horror"][:10]


# ### 4.3.4
# Process the movies dataset (the original file or the dictionary built in __4.3.3__) and build a dictionary that indexes movies by the first letter of the title. Then create a small interface for querying (using the input function)

# In[ ]:




# ### 4.3.5
# Build an incremental search of movie titles: users should be able to narrow the set of movies with every character they type. You may create deeply nested dictionaries beforehand or process the data on-the-fly.

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


# In[40]:

search("data/movies.tsv")


# ## 4.4 The _collections_ module
# <a id='4.4'></a>

# ### 4.4.1
# Modify the word counter in __4.3.1__ so that it uses a defaultdict.

# In[ ]:




# ### 4.4.2
# Modify the word counter in __4.4.1__ so that it uses a Counter.

# In[ ]:




# ### 4.4.3
# Define a function that queries users for their last name, first name, year of birth, and hobby, and populates an OrderedDict whose keys are the last names and values are dictionaries with four keys each. If a second person with the same last name is encountered, both should now have keys of the form "lastname_firstname". If the same person is encountered multiple times, his/her data should be updated. Then test the solution of someone else and ask her to test yours.

# In[44]:

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
    


# ### 4.4.4
# Convert the database built in __4.4.3__ into a list of namedtuples.

# In[ ]:



