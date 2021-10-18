
#****** Variables and Some Arithmetic

#Given: Two positive integers a and b

#each less than 1000.

# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a
# and b
# hypotenuse square 
# use pythogoras or a2+b2=C2

def hypotenuse(a,b):
	hyp_sqr=(a**2 + b**2)
	return hyp_sqr

# print(hypotenuse(990, 805))






# ******* Strings and lists
# Given: A string s of length at most 200 letters and four integers a, b, c and d


# Return: The slice of this string from indices a
# through b and c through d (with space in between), inclusively. In other words, 
# we should include elements s[b] and s[d] in our slice.

# #string slicing
def slice(string,a,b,c,d):
	varst=string[a:b+1] + ' '+ string[c:d+1] 


	return varst
# print(slice('JqBbWjyVPVvaRY4zsgxjrQXKhlVoOyPJGIwK1ZDDda4DtPTUVDujOTRPmpVOiXwUL1CorallusFaZdBaHLruficollisvdynXSntjU8ch3B7jAAULk38VrQ58sekrrGJnNHKrJZ4HbXVSQxaHpFH1vPgkLWmUf2f.',66 ,73 ,82, 91))


# #**** conditional loops
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.


#Conditions and Loops

def cloops(a,b):
	Sum=0
	while a!=b and b<100 and a>0:
	    if a%2!=0:
	        Sum= a+Sum
	    a=a+1
	return Sum
# or 
def cloops_2(a,b):
	return sum([x for x in range(a,(b+1)) if x%2!=0])
	    
	

# print(cloops(1,10))
# print(cloops_2(1,10))


# *****Working with Files 

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. 
# Assume 1-based numbering of lines.

#printing even lines of a file.



def readf(file):
	count=0
	f=open(file,'r')
	for line in f:
		l=line.splitlines() #split files in lines
		count+=1 
		if count%2==0: #when count is even it reads line
			for line in l:
				print(line) #print even lines

# readf('practicef.txt')

# *****Dictionaries 
# Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.

#word frquencey on a string:



def wordfreq(string):
	count=0
	l=dict()
	s=string.split()
	#set up words in dictionary
	for word in s:
		l[word]=(count)
	#check if word is in s and then increment count if it is.
	for word in s:
		if word in s:
			l[word]+=1
	return l

var=wordfreq('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')

for key, value in var.items():
    print (key,value)
   








