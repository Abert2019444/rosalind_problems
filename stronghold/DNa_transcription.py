#replaces every t for a u in a dna seq, 
#this is to refect that rna uses Uracil instead of thymine

dna_seq=''
def transcription(seq):
	rna_seq=[]
	for Nuc in seq:
		if Nuc=='A':
			rna_seq.append('U')
	return rna_seq
	
transcript=transcription(dna_seq)
#how to print a string without spaces
print(''.join(str(i) for i in transcript[:-1]))