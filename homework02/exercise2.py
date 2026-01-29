from Bio.Seq import Seq
dna_sequence = Seq('GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA')

g_count = dna_sequence.count('G')
c_count = dna_sequence.count('C')

gc_content = (g_count + c_count) / len(dna_sequence)

print(f'The GC content of the sequence is {gc_content}.')