from abc import ABC, abstractmethod
class Sequence(ABC):
    def __init__(self, name, seq, alphabet):
        self._seq = seq
        self._name = name
    def Lehgth(self):
        return len(self._seq)
    def MolMass(self):
        if isinstance(self, DNA):
            return 2*345*len(self._seq)
        elif isinstance(self, RNA):
            return 345*len(self._seq)
    def Frequency(self):
        for i in set(self._alphabet):
            print(f'{i} frequency equals {self._seq.count(i)}')


class DNA(Sequence):
    def __init__(self, name, seq):
        self._name = name
        self._seq = seq
        self._alphabet = {'A':'T', 'G':'C','T':'A','C':'G'}
    def Complimentar(self):
        self.complimentar = ''
        for n in self._seq:
            self.complimentar += self._alphabet[n]
        return self.complimentar
    def Transcription(self):
        self.transcript = self.Complimentar()
        return self.transcript.replace('T', 'U')
class RNA(Sequence):
    def __init__(self, name, seq):
        self._name = name
        self._seq = seq
        self._alphabet = {'A': 'T', 'G': 'C', 'U': 'A', 'C': 'G'}
        self._codons = {
            'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
            'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
            'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
            'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
            'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
            'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
            'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
            'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
            'UAC': 'Y', 'UAU': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
            'UGC': 'C', 'UGU': 'C', 'UGA': 'Stop', 'UGG': 'W'}
    def Translation(self):
        self.protein = []
        for n in range(0,len(self._seq)//3*3,3):
            self.protein.append(self._codons[self._seq[n:n + 3]])
        return self.protein


#Test
s1 = DNA('s1', 'ATTTATCTCGTACGTAGCGCGATAGCTGATTCGACGCTTGGACACGTGAGTACGTTAGCAC')
s2 = RNA('s2', s1.Transcription())
s1.MolMass()
s2.MolMass()

