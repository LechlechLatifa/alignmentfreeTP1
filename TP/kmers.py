# fonction donné
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for _ in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

# simple correspondance
def encode_nucl(letter):
    encoding = {'A':0, 'C':1, 'T':2, 'G':3}
    return encoding[letter]

def reverse_complement_kmer(kmer, k):
    complement = 0
    for _ in range(k):
        complement <<= 2
        complement |= (kmer & 0b11) ^ 0b10  # Swap A (00) with T (10), and C (01) with G (11)
        kmer >>= 2
    return complement

def canonical_kmer(kmer, k): # permet de calculer le reverse et d'appliquer le min
    rev_kmer = reverse_complement_kmer(kmer, k)
    return min(kmer, rev_kmer)

# fonction suffisante sans passer par des streams
def stream_kmers(text, k):
    kmers = set()
    for i in range(len(text) - k + 1):
        kmer = str2kmer(text[i:i+k], k)
        kmers.add(canonical_kmer(kmer,k)) # cannonical me permet de faire le min entre kmer et rkmer
    return kmers
