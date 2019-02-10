
calculate_error <- function(L,n,p,k,av){
    if(k == 1){
        sequenced_error=(n)*(p)
        non_sequenced_error=(L-n)*(1-0.25)
        print(paste(x, sequenced_error, non_sequenced_error))
        total_list=sequenced_error+non_sequenced_error
    } else {
        tmp=dbinom(x=1:(L-n+1), size=(L-n+1), prob=((av-n+1)/(L-n+1)))
        print(paste(L,n,p,k))
        total_list=c()
        for(x in 1:(L-n+1)){
            proportion=tmp[x]/sum(tmp)
            sequenced_error=proportion*(x+n-1)*(p)
            non_sequenced_error=proportion*(L-x-n+1)*(1-0.25)
            print(paste(x, sequenced_error, non_sequenced_error))
            summation=sequenced_error+non_sequenced_error
            total_list=c(total_list,summation)
        }
    }
    return(sum(total_list))
}

data <- read.table("python.problem2.1.output.txt", sep=" ")
for(x in 1:nrow(data)){
    x <- data[x,]
    tmp <- calculate_error(L=as.numeric(x[1]),n=as.numeric(x[2]),p=as.numeric(x[3]),k=as.numeric(x[4]),av=as.numeric(x[5]))
    print(tmp)
}