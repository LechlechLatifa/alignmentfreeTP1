


def compare_k_mers(kmers_1,kmers_2):
    for i in range(len(kmers_1)):
        if kmers_1[i] != kmers_2[i]:
            return False
    return True 

# To do 
def create_index(seq_1, k):
    pass

# To do 
def enumerate_k_mers(seq, k):
    pass # or smash okay

def compare_sequences(seq_1, seq_2, k):
    index = create_index(seq_1, k)
    intersect = 0 
    union = sum(index.values)
    for k_mer in enumerate_k_mers(seq_2, k):
        if k_mer in index and index[k_mer] > 0:
            index[k_mer] -= 1 
        else: 
            union += 1
        
