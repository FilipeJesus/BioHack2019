L=210
n=11
p=0.034
k=156

tmp=dbinom(x=1:(L-n+1), size=(L-n+1), prob=(209.95261-n+1)/(L-n+1))
print(sum(tmp))
total_list=c()
for(x in 1:(L-n+1)){
	    proportion=tmp[x]/sum(tmp)
    sequenced_error=proportion*(x+n-1)*(p)
        non_sequenced_error=proportion*(L-x-n+1)*(1-0.25)
        #print(paste(x, "number:", sequenced_error, "sequenced erros and", non_sequenced_error, "unseqeuenced errors"))
        summation=sequenced_error+non_sequenced_error
	    total_list=c(total_list,summation)
}
print(sum(total_list))
