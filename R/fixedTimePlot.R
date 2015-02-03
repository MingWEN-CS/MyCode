ustblue = rgb(0/255,51/255,102/255)
ustgold = rgb(153/255,102/255,0/255)
ustyellow = rgb(204/255,153/255,0/255)
ustsilver = rgb(204/255,204/255,204/255)

civiplot <- function(directory, filename) {
  filename = paste(directory,filename, sep = "/")
  data <- read.csv(filename)
  single = (data["single"])
  multi = (data["multi"])
  single = single[!is.na(single)]
  multi = multi[!is.na(multi)]
  single = single / (60*60*24)
  multi = multi / (60*60*24)
  print(mean(single))
  print(mean(multi))
  #var.test(single,multi)
  #t.test(single, multi,var.equal=FALSE,alternative="less")
  #  print("Hello");
  # plotData <- data.frame(Single = single, Multiple = multi)
  boxplot(single,multi,main="Bug Fixing Time",ylab = "Fix Time (days)",outline=FALSE,
          col= c(ustyellow,ustblue),names = c("Type I","Type II"))
}

civiBarplot <- function(type1, type2) {
  counts = matrix(c(type1,type2),nrow=3)
  print(t(counts))
  bp <- barplot(t(counts),main="Incomplete Fix Ratio",xlab="Projects",col=c(ustblue,ustyellow),ylab = "Number",
          names = c("Firefox24.0","Firefox25.0","Firefox26.0"),
          legend = c("Complete","Incomplete"),
          args.legend = list(x = "topright", cex = .8), ylim = c(0,150))
  text(bp, 0, c("24.0%","29.6%","33.0%"),cex=1,pos=3,col = ustsilver)
}