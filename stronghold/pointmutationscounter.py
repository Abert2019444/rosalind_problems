#counts how many mutations are on seq t, seq a is the ref seq
def mutation(s,t):
	counter=0
	# Dna_reverseseq={'A': 'T','T':'A', 'C':'G','G':'C'}

	for i in range(len(s)):
		if s[i]!=t[i]:
			counter+=1	
			
	return counter


	
print(mutation('CGTTTGTTGCTCCCAAGCGTGCGCTTTTACGCGCTCAGTCAAATTGCCTTGCCGAGTCCTGCTAAGGGTAGGATACTGAGCTATGGCTTATAGCCCCCCATTGCATCTCGCGTGCTGGCAGCGAACACAGCCCACTTTTTACGCCCAAGACCATATCCTAATTTGGTGGATCCCTATACGTATCCGGCATGTGTTAGTAAAGTGATATAAGTGTCCCCGCATCCACGTAAGATGATTGAACAGTGTGGCTAGACCCTCGCGTGGACAAATAGAGTAGCTGAGGACTTAAAATCTGCTGTCGAAATATAATGCCGTTATGGTAGACAATCAATGCCTCGTGTCTAACATCACACATAAACACGCTTAGCTTCATCGTAACCGAAGTTTAGTCCCGATGATCCTACTCGTAACCCCCCGGCTCGTGGGCGCGCCTTGCTTTTTGGGCGGGTTGTAAAGGATTATCTTGCAACTCAGCGACTCGCGTACTTTATCTGCGCAGCATTTTCTACCCTAAATCGCTTGGCACTACTACACGCTAATTTCTAGATTAGCGTGATCGAACACAAGGGCTGTAAAAGAAAGGGTGAGTGCGCACAGTCTGATGTGAAAACGGCGACCTAATTACTATAAGTGAGGAGAGAACACCCAAATCGAATCTGTTGAAAAGCTCGTGTCGCCGCTTTCCCCCTTAGAAAAACCTTATCCGACTCAGCATTCGTACGTTGAACACGGCATCGCATCTGCTTGGACACGTCCGTGTCCGCGTTGAGGTTCTCCGTAGTCCGAAAAGAAGATGTTATCCTAAGCCATGCACTCACTAAAGCGCAAGTCAACGTAGATCGTAACGAGGGCATGCGCAGATTATCGGCGACGGCCCATCAGCGTCTTCGAAGCGACTGCGGAAAGATG','CTATTTAGGCGGCTCCCCCGGCTCCCTTACGTCCTCACTTACATCTTTTCGCTACTGTGCCAGACGGAAGCATCTCTAATCGTCGATTTTGAGACCACAAGGGGAGAAACAGTGCAAGTCACGGAGAACCCCCAAACTTTATTGCAAAGACGAGGCGCGCAGCTGACCGGTGCCTATGGTTCAACTCCATGCGTGCGAAAATAAATCGAGTCATATGCACACCCCTGAAACGTATACGATCAGGCAGGATAGCTCAGTACCTTGATGCGTGAAATGGTGGATAACTAAACGCCAGCTTCCGACACGTTCCTTCGTGAGGTTCGAAAAACACTGGCGTAGTTCTAACGCAACGCTTCCACTGAATTGTGTTAACCTTAACGGCTTTTTTCACCAGGGGTTCTGATAGGCAGTCCACCCAATCATCGGCCGGGTTTGCTGTATACCAAGTTTGAATCCGTATCAATTGAATCCCCTTGACTCTCGACAGTTTTCTAGTCCTAAATGTCTCAACAAGACCGAAGGTCAAAAACCCAAGCCCTTGTCGTTGCAGGAGTTGTCGTTAGGAGGATTACGTGCATAAGGTGAGCGTGCTCCTCTCCGTTCCTGTCAGTGGGGAAGAATTTCCTTAAGGCCAGGAGTGTTGAAGCAACTGGGGTCCCGTGAAAGACACTCGTCCGTGCTACTAAGCTAAGAAAACCACTGTTTGACCTAATATCCGGTCGTAGAACTCGGCGAAACAGCACGATCCACTCGTCCGAGTGGACGTCAGGTTTATAGGAGGCCCATTTCCTAGATCAAGGCATAATCCTAATCCGCTCGGATAAGCACATACAAGGAGACCATAAACATGGTGACTCCCGAGTTTGCTGGGCTAACAATCCGTTTCCTCCGAGAGACCGGGAACGTACT'))

