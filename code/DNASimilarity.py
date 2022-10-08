

try:
    
    file_seq1 = open('sequence1.txt', 'r')  # opening the file in read mode
    for seq1 in file_seq1.readlines():      # traversing through the file
        print("The first Sequence is: ",seq1)  # printing file sequence
    file_seq1.close()       # closing file handler

    file_seq2 = open('sequence2.txt', 'r')    # opening the file in read mode
    for seq2 in file_seq2.readlines():     # traversing through the file
        print("The second Sequence is: ",seq2)      # printing file sequence
    file_seq2.close()       # closing file handler

    score=0          # initializing score to zero

    #print(len(seq1))
    for i in range(len(seq1)):    # traversing through the length of sequence-1
        #print("i = ",i)
        preseq1=seq1[:i]    # storing the remaining sequence
        postseq1="-"*i          # storing the sequence with "-" to atttach to the main string
        seqtemp1= seq1[i:]       # part of sequence1 to be compared
        preseq2=i*"-"         # storing the sequence with "-" to atttach to the main string
        postseq2=seq2[len(seq2)-i:]              # storing the remaining sequence
        seqtemp2= seq2[: len(seq2)-i]       # part of sequence2 to be compared
        #print("seqtemp1 : ",seqtemp1)
        #print("seqtemp2 : ",seqtemp2)
        scoretemp=0           #   temporary score counter
        for i in range(len(seqtemp1)):      # iterating through the length of sequence
            if seqtemp1[i]==seqtemp2[i]:     # comparing each character from sequence1 and sequence2
                scoretemp+=1      # increasing temporary score counter
        #print("scoretemp : ",scoretemp)
        if scoretemp>score:     # checking if temporary score is greater than the normal score
            score=scoretemp         # updating score variable
            highseq1=preseq1+seqtemp1+postseq1       # creating total sequence1
            highseq2=preseq2+seqtemp2+postseq2       # creating total sequence2

    #print("Reverse")
    #     print("score inside: ", score)
    #     print("highseq1 inside: ",highseq1)
    #     print("highseq1 inside: ",highseq2)
    for i in range(len(seq1)):    # traversing through the length of sequence-1
        #print("i = ",i)
        preseq1=i*"-"         # storing the sequence with "-" to atttach to the main string
        postseq1=seq1[len(seq2)-i:]          # storing the remaining sequence
        seqtemp1= seq1[ : len(seq2)-i]       # part of sequence1 to be compared
         
        preseq2=seq2[:i]                 # storing the remaining sequence
        postseq2=i*"-"         # storing the sequence with "-" to atttach to the main string
        seqtemp2= seq2[i: ]       # part of sequence2 to be compared
        #print("seqtemp1 : ",seqtemp1)
        #print("seqtemp2 : ",seqtemp2)
        scoretemp=0
        for i in range(len(seqtemp1)):      # iterating through the length of sequence
            if seqtemp1[i]==seqtemp2[i]:    # comparing each character from sequence1 and sequence2
                scoretemp+=1    # increasing temporary score counter 
        #print("scoretemp : ",scoretemp)
        if scoretemp>score:  # checking if temporary score is greater than the normal score
            score=scoretemp # updating score variable
            highseq1=preseq1+seqtemp1+postseq1       # creating total sequence1
            highseq2=preseq2+seqtemp2+postseq2        # creating total sequence2
         
         
         
    print("score : ", score)
    print("highseq1: ",highseq1)
    print("highseq2: ",highseq2)
        
except FileNotFoundError:                   # catching File not found Exception
    print("DNA file(s) is not found")

