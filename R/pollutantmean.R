pollutantmean <- function(directory, pollutant, id = 1:332)  {
  d = c()
  for (i in id) {
    if(i>=1 && i<10) {
      te1 <- paste("00",i,sep="")
      #print(te1)
    } else if(i>=10 && i<=99) {
      te1 <- paste("0",i,sep="")
      #print(te1)
    } else {
      te1 <- i
      #print(te1)
    }
    #print(te1)
    filename = paste(directory, te1, sep = "/")
    filename = paste(filename, "csv", sep = ".")
    data <- read.csv(filename)
    data = (data[pollutant])
    tmp = data[!is.na(data)]
    d <- c(d,tmp)
    #ans = mean(d)
    #print(ans)
    #c( rbind(a,b) )
  }    
  ans = mean(d)
  ans <- round(ans,3)
  return(ans)
  #print(ans)
}

