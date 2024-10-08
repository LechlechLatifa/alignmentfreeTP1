
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


def encode_nucl(letter):
    encoding = {'A':0, 'C':1, 'T':2, 'G':3}
    return encoding[letter]

def str2kmer(kmer_str, k):
    kmer = 0
    for i in range(k):
        kmer <<= 2
        kmer += encode_nucl(kmer_str[i])
    
    return kmer

def stream_kmers(text, k):
    kmers = set()
    for i in range(len(text) - k + 1):
        kmer = str2kmer(text[i:i+k], k)
        kmers.add(kmer)
    return kmers
