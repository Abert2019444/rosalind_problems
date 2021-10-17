#calculate the g and c content in a dna seq in fatsa formsat

def file_reader(file):	
	with open(file,'r') as f:

		return[i.rstrip() for i in f.readlines() ] #return a string with all the lines in file


def gc_content(seq):
	var=(seq.count('G')+seq.count('C') )/len(seq)*100 #calculate gc frequency
	return round(var,6)

rosalindFile=file_reader('dnastrings.txt')

labels=''
dnaseq={}
for line in rosalindFile: #makes a dictionary out of the label and seq
	if line.startswith('>'):
		labels=line
		dnaseq[labels]=''
	else:
		dnaseq[labels]+=line #go to the next line
results={}

for k,v in dnaseq.items(): #makes a dict of label and gc seq
	results[k]=gc_content(v)

maxkey=max(results,key=results.get) # the key of the max value
print(f'{maxkey},\n {results[maxkey]}') # print max value and key


	
	







		



	

	



	




	



