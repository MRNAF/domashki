a = ['A', 'T', 'G', 'C']
text = 'ATAGACATGCGTGCATGCAACTGATA'
def SymbStat(a):
    def calcSymbStat(text):
        for i in a:
            print (f'{i} appears {text.count(i)} times')
    return calcSymbStat
calc = SymbStat(a)
calc(text)