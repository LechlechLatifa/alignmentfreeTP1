from TP.loading import load_directory
from TP.kmers import stream_kmers, kmer2str



def jaccard(fileA, fileB, k):
    kmersA = set()
    kmersB = set()
    for sequence in fileA:
        kmersA.update(stream_kmers(sequence, k))
    for sequence in fileB:
        kmersB.update(stream_kmers(sequence, k))
    intersection = len(kmersA & kmersB)
    union = len(kmersA | kmersB)
    if union == 0:
        return 0
    return intersection / union



if __name__ == "__main__":
    print("Computation of Jaccard similarity between files")

    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21
    
    print("Computing Jaccard similarity for all pairs of samples")
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            
            # --- Complete here ---

            j = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], j)
