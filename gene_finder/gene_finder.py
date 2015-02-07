# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Gabriel Butterick

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    if nucleotide == "T":
        return "A"
    if nucleotide == "A":
        return 'T'
        print 'T'
    elif nucleotide == "G":
        return "C"
    elif nucleotide == "C":
        return "G" 
    
    pass

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    x = len(dna)
    inverse_compliment = ''
    i = 1
    while i <= x:
        index = x-i
        nucleotide = dna[index]
        inverse_compliment = inverse_compliment + get_complement(nucleotide)
        i = i+1
    return inverse_compliment

    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string. Stop codons: TAG, TAA, or TGA
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # TODO: implement this
    length = len(dna)
    i = 0
    codontotal = ''
    if i+2 < length:
        while i < length:
            codon = dna[i:i+3]
            if codon == "TAG" or codon == "TAA" or codon == "TGA":
                return codontotal
                #print "end codon"
            else:
                #print "new orf"
                codontotal += codon
            i += 3
    else:
        return dna
    return codontotal
        
    

#print rest_of_ORF("ATGTGAA")

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    length = len(dna)
    i = 0
    code_list = []
    code = ''
    #ORF = False
    x = 0 
    end = False
    while x < length: 
        codon = dna[x:x+3]
            
        if codon == "ATG":
            code = rest_of_ORF(dna[x:])
            code_list += [code]
            x = x + len(code)
            
        else:
            x = x+3
            
    return code_list
#print find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    seriesTotal = []
    series1 = find_all_ORFs_oneframe(dna)
    series2 = find_all_ORFs_oneframe(dna[1:])
    series3 = find_all_ORFs_oneframe(dna[2:])
    seriesTotal += series1 + series2 + series3 
    return seriesTotal
#print find_all_ORFs("ATGATGCATGAATGTAGCCCGATATGGGATT")

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    seriesTotal = []
    series1 = find_all_ORFs(dna)
    reversecomplement = get_reverse_complement(dna)
    series2 = find_all_ORFs(reversecomplement)
    seriesTotal = series1 + series2
    return seriesTotal
#print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    #pass
    x = find_all_ORFs_both_strands(dna)
    length = len(x)
    longest = ''
    for i in range(length):
        if len(x[i]) > len(longest):
            longest = x[i]
    return longest
#print longest_ORF('ATGCGAATGTAGCATCAAA')        



#print longest_ORF('ATGCGAATGTAGCATCAAA')

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    longest = ''
    for i in range(num_trials):
        newDna = shuffle_string(dna)
        length = longest_ORF(newDna)
        if len(length) > len(longest):
            longest = length
    return longest
#print longest_ORF_noncoding('ATGCGAATGTAGCATCAAA', 20)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    length = len(dna)
    amino_total = ''
    for i in range(0,length,3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            amino_acid = aa_table[codon]
            amino_total += amino_acid
    return amino_total
#print coding_strand_to_AA("ATGCGA")
def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    threshold = len(longest_ORF_noncoding(dna, 1500))
    strand = find_all_ORFs_both_strands(dna)
    length = len(strand)
    amino_total = []
    for i in range(length):
        if len(strand[i]) > threshold:
            amino = coding_strand_to_AA(strand[i])
            amino_total += [amino]
    return amino_total
dna = load_seq("./data/X73525.fa")

print gene_finder(dna)





# if __name__ == "__main__":
#     import doctest
#     doctest.testmod() 