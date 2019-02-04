from itertools import chain
import itertools
import numpy as np

def unique(x):
    unique_list=[]
    for i in x:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def enumerate_list(L,n):
    print("using enumerate_list")
    h=enumerate(range(0, L), 1)
    t=enumerate(range(0, n-1), 1)
    numlist=[]
    [numlist.append(x[1]) for x in h]
    [numlist.append(x[1]) for x in t]
    return numlist

def possible_options(L,n,numlist):
    print("using possible_options")
    possible=[]
    for i in range(0,L):
        tmp=[]
        [tmp.append(numlist[x]) for x in range(i,i+n)]
        possible.append(tmp)
    return possible 

def com_list(L,n,k,com):
    print("using com_list")
    possible= com
    for i in range(0,k-1):
        print(i)
        tmp=[]
        com=list(itertools.product(com, possible))
        joined_list=[]
        for x in com:
            tmp = x[0]+x[1]
            tmp=unique(x=tmp)
            joined_list.append(tmp)
        com=joined_list
    return com

def joined_list(L,n,k,com):
    print("using joined_list")
    joined=com
    return joined

def create_final_matrix(L,n,k,p,joined):
    print("using create_final_matrix")
    lengths=[len(x) for x in joined]
    nump_array = unique(lengths)
    nump_array
    numb_each=[]
    [numb_each.append(lengths.count(x)) for x in unique(lengths)]
    numb_prop=[]
    [numb_prop.append(x/len(joined)) for x in numb_each]
    tmp = np.column_stack((nump_array,numb_prop))
    tmp = list(chain.from_iterable(tmp))
    tmp2=[]
    for x in range(0,len(nump_array)):
        tmp2.append([tmp[2*x],tmp[(2*x)+1]])
    tmp=tmp2
    num_of_error=[]
    for x in tmp:
        n_comb=x[0]
        sequenced_error=(n_comb)*(p)
        non_sequenced_error=(L-n_comb)*(1-0.25)
        num_of_error.append(sequenced_error+non_sequenced_error)
    tmp2=[]
    [tmp2.append([num_of_error[x],tmp[x][1]]) for x in range(0,len(num_of_error))]
    return tmp2

def base_function(L,n,p,k):
    numlist = enumerate_list(L=L,n=n)
    possible = possible_options(L=L,n=n,numlist=numlist)
    com = com_list(L=L,n=n,k=k,com=possible)
    joined = joined_list(L=L,n=n,k=k,com=com)
    final = create_final_matrix(L=L,n=n,k=k,p=p,joined=joined)
    return final

with open("test2.txt") as f:
    for line in f:
    line = line.split(" ")
    n = create_final_matrix(L=int(line[0]),n=int(line[1]),p=float(line[2]),k=int(line[3]))
    print(sum([x[0]*x[1] for x in n]))
