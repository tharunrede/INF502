# INF 502 - PA1
Programming Assignment 1 for INF 502.

**DUE DATE:** OCT-13

This assignment will give you some practice with basic Python structures, file input and output, 
and exceptions in the context of writing a basic program. We will deal with two dummy problems, about which you will have to discuss at the end.

SOURCE CODE: File attached [Here]()

```python



try:
    
    file_seq1 = open('sequence1.txt', 'r')  # opening the file in read mode
    for seq1 in file_seq1.readlines():      # traversing through the file
        print("The first Sequence is: ",seq1)  # printing file sequence
    file_seq1.close()       # closing file handler

    file_seq2 = open('sequence2.txt', 'r')    # opening the file in read mode
    for seq2 in file_seq2.readlines():     # traversing through the file
        print("The second Sequence is: ",seq2)      # printing file sequence
    file_seq2.close()       # closing file handler

    # highseq1=""
    # highseq2=""
    score=0

    #print(len(seq1))
    for i in range(len(seq1)):
        #print("i = ",i)
        preseq1=seq1[:i]
        postseq1="-"*i
        seqtemp1= seq1[i:]
        preseq2=i*"-"
        postseq2=seq2[len(seq2)-i:]
        seqtemp2= seq2[: len(seq2)-i]
        #print("seqtemp1 : ",seqtemp1)
        #print("seqtemp2 : ",seqtemp2)
        scoretemp=0
        for i in range(len(seqtemp1)):
            if seqtemp1[i]==seqtemp2[i]:
                scoretemp+=1
        #print("scoretemp : ",scoretemp)
        if scoretemp>score:
            score=scoretemp
            highseq1=preseq1+seqtemp1+postseq1
            highseq2=preseq2+seqtemp2+postseq2

    #print("Reverse")
    #     print("score inside: ", score)
    #     print("highseq1 inside: ",highseq1)
    #     print("highseq1 inside: ",highseq2)
    for i in range(len(seq1)):
        #print("i = ",i)
        preseq1=i*"-"
        postseq1=seq1[len(seq2)-i:]
        seqtemp1= seq1[ : len(seq2)-i]
        
        preseq2=seq2[:i]
        postseq2=i*"-"
        seqtemp2= seq2[i: ]
        #print("seqtemp1 : ",seqtemp1)
        #print("seqtemp2 : ",seqtemp2)
        scoretemp=0
        for i in range(len(seqtemp1)):
            if seqtemp1[i]==seqtemp2[i]:
                scoretemp+=1
        #print("scoretemp : ",scoretemp)
        if scoretemp>score:
            score=scoretemp
            highseq1=preseq1+seqtemp1+postseq1
            highseq2=preseq2+seqtemp2+postseq2       
         
         
         
    print("score : ", score)
    print("highseq1: ",highseq1)
    print("highseq2: ",highseq2)
        
except FileNotFoundError:
    print("DNA file(s) is not found")



```
