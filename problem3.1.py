from itertools import chain
import itertools
import numpy as np

sequence="GAGTCATCGGACGATCC"
n=2
I=7
d=3

possible=["A","C","T","G"]
com=possible
for x in range(0,I-1):
    tmp=[]
    com=list(itertools.product(com, possible))
    joined_list=[]
    for x in com:
        tmp = x[0]+x[1]
        joined_list.append(tmp)
    com=joined_list

list_string=[]
for x in com:
    len_through_sequence=0
    error=0
    len_through_x = 0
    len_of_matching_string=0
    #print(x)
    #print(sequence[counter])
    while len_of_matching_string <= I:
        if error > d:
            break
        elif (len_through_x) >= len(x):
            break
        elif (len_through_sequence) >= len(sequence):
            break
        elif x[len_through_x] == sequence[len_through_sequence]:
            len_through_sequence=len_through_sequence+1
            len_of_matching_string=len_of_matching_string+1
            len_through_x=len_through_x+1
        else:
            check=0
            for t in range(1,n+2):
                if (len_through_sequence+t+1) > len(sequence):
                    error = d+1
                    break
                elif (len_through_x+t+1) > len(x):
                    error = d+1
                    break
                elif error >d:
                    break
                elif x[len_through_x] == sequence[len_through_sequence+t]:
                    len_through_sequence=len_through_sequence+t+1
                    len_of_matching_string=len_of_matching_string+1
                    len_through_x=len_through_x+1
                    error=error+t
                    check=1
                    break
                elif x[len_through_x+t] == sequence[len_through_sequence]:
                    len_through_sequence=len_through_sequence+1
                    len_of_matching_string=len_of_matching_string+1
                    len_through_x=len_through_x+t+1
                    error=error+t
                    check=1
                    break
                elif x[len_through_x+t] == sequence[len_through_sequence+t]:
                    len_through_sequence=len_through_sequence+t+1
                    len_through_x=len_through_x+t+1
                    len_of_matching_string=len_of_matching_string+1
                    error=error+t
                    check=1
                    break
            if check==0:
                len_through_x=len_through_x+1
    if x == "ACGTAGC":
        print(x,len_through_sequence,error,len_through_x,len_of_matching_string)
    if error < d & len_of_matching_string >= I:
        list_string.append(x)
print(list_string)
