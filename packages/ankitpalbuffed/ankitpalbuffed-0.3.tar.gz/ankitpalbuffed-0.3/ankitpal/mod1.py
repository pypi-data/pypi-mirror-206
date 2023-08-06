def buffed():
    return """#Use Iris data set for following questions (use R):
#  1. Draw scatter plot to represent relation between sepal length Vs sepal width for all
#species (sepal length on x axis, sepal width on y axis). Use different color and shape to
#represent species. Give appropriate title and labels for x and y axis
#2. Modify above chart to show 3 groups of species separately using Facet
#3. Draw boxplot for petal length attribute for each species. (use different colors for
#                                                              species. Give appropriate titles and labels)
library(ggplot2)
data(iris)
ggplot(iris, aes(x=Sepal.Length, y=Sepal.Width,color=Species,shape=Species))+
  geom_point()+
  xlab("Sepal Length")+
  ylab("Sepal Width")+
  ggtitle("Scatter Plot")

ggplot(iris,aes(x=Sepal.Length,y=Sepal.Width,color=Species,shape=Species))+
  geom_point()+
  xlab("Sepal Length")+
  ylab("Sepal Width")+
  ggtitle("Scatter Plot")+
  facet_wrap(~Species)

ggplot(iris,aes(x=Species,y=Sepal.Length,fill=Species))+
  geom_boxplot()+
  xlab("Species")+
  ylab("Sepal length")+
  ggtitle("Boxplot")


#Use Iris data set for following questions (use R):
#  1. Draw the histogram of sepal width attribute (use appropriate title, label, binwidth and
#                                                  manual 3 colours to represent species)
#2. Draw a bar chart to show the average value of each attribute for each species. (species
#                                                                                   on x axis, average value on y axis, use orange, blue, green and purple color to indicate
#                                                                                   sepal length, sepal width, petal length and petal width respectively, use side by side
#                                                                                   bar chart, put legend on top)
#3. Draw a pie chart showing count of every species. (give appropriate legend title)
binwidth <- 0.2
colours <- c('red','blue','green')
hist(iris$Sepal.Width, breaks=seq(2,4.5,binwidth),col=colours[iris$Species],
     main="Histogram for Sepal Width vs Species",xlab="Sepal Width",ylab="Count")

means <- aggregate(iris[,1:4],list(Species=iris$Species),mean)
colours<-c("orange","blue","green","purple")
legend_labels<-c("Sepal Length","Sepal Width","Petal Length","Petal Width")
barplot(t(means[,2:5]),beside=TRUE,col=colours,
        main="Average Plot",xlab="Species",ylab="Average Value",
        ylim=range(0,round(max(means[,2:5]),1)+0.2),
        legend.text=legend_labels,args.legend = list(x="top",ncol=4))

counts<-table(iris$Species)
colours<-c("red","blue","green")
labels<-c("Setosa","Versicolor","Virginica")
pie(counts,col=colours,main="Species Count",labels=labels)
legend("topright",labels,fill=colours,title="Species")


# Use Iris data set for following questions (use R):
#   1. Draw a line plot showing the range of sepal length values and sepal width values for each
# species. Line should start from a point( minimum sepal length and minimum sepal width
#                                          value) and end at point( maximum sepal length and maximum sepal width value). (Give
#                                                                                                                         appropriate title and labels)
# 2. Draw boxplot for sepal length attribute for each species. (use different colors for
#                                                               species. Give appropriate titles and labels)
# 3. Draw the histogram of petal width attribute (use appropriate title, label, binwidth and
#                                                 manual 3 colours to represent species)

min_max<-aggregate(cbind(Sepal.Length,Sepal.Width) ~Species,data=iris,FUN=range)
min_max
plot(Sepal.Length ~ Sepal.Width,data=iris,type="n",
     main="Plot Range",
     xlab="Sepal Width",ylab="Sepal Length")
colours<-c("red","blue","green")
for(i in 1:nrow(min_max)){
  lines(c(min_max[i, "Sepal.Width"][1],min_max[i,"Sepal.Width"][2]),
        c(min_max[i,"Sepal.Length"][1],min_max[i,"Sepal.Length"][2]),
        col=colours[i], lwd=2,)
}
legend("topright",legend=levels(iris$Species),col=colours[1:nlevels(iris$Species)],lwd=2)

boxplot(Sepal.Length ~ Species, data=iris,
        main="Boxplot",
        xlab="Species",
        ylab="Sepa; length",col=colours)

hist(iris$Petal.Width[iris$Species=="setosa"],
     col=colours[1],
     xlim=c(0,3),
     ylim=c(0,25),
     breaks=seq(0,3,by=0.2),
     main="Setosa",
     xlab="Petal Width",
     ylab="Frequency")
hist(iris$Petal.Width[iris$Species=="versicolor"],
     col=colours[2],
     add=TRUE,
     breaks=seq(0,3,by=0.2))
hist(iris$Petal.Width[iris$Species=="virginica"],
     col=colours[3],
     add=TRUE,
     breaks=seq(0,3,by=0.2))
legend("topright",legend=levels(iris$Species),fill=colours)

# 1. Perform the given task in R (without using direct functions available )
# Consider the following data
# X1 10 12 10 9 15 10 14 15 15 16
# X2 8 12 9 9 11 9 11 14 11 12
# y 10 10 10 9 11 11 9 9 10 10
# 
# a) Print first 5 rows of data
# b) Calculate(using formula) and print regression coefficients b0,b1 and b2
# c) Display regression line equation
# d) Calculate and print coefficient of determination (R squared, Residual sum of
#                                                      squares (RSS), and RMSE
X1<-c(10,12,10,9,15,10,14,15,15,16)
X2<-c(8,12,9,9,11,9,11,14,11,12)
y<-c(10,10,10,9,11,11,9,9,10,10)
df<-data.frame(X1,X2,y)
head(df,5)
df['X1Y'] <- df['X1']*df['y']
df['X2^2'] <- df['X2']*df['X2']
df['X2Y'] <- df['X2']*df['y']
df['X1X2'] <- df['X1']*df['X2']
df['X1^2'] <- df['X1']*df['X1']
B1 <- (sum(df['X1Y'])*(sum(df['X2^2']))-(sum(df['X2Y']))*(sum(df['X1X2'])))/(sum(df['X1^2'])*sum(df['X2^2'])-(sum(df['X1X2'])*sum(df['X1X2'])))
B2 <- (sum(df['X2Y'])*(sum(df['X1^2']))-(sum(df['X1Y']))*(sum(df['X1X2'])))/(sum(df['X1^2'])*sum(df['X2^2'])-(sum(df['X1X2'])*sum(df['X1X2'])))
B0 <- (sum(df['y'])/10)-B1*(sum(df['X1'])/10)-B2*(sum(df['X2'])/10)
B0<-round(B0,digits=2)
B1<-round(B1,digits=2)
B2<-round(B2,digits=2)
cat("B0:",B0,"\nB1:",B1,"\nB2:",B2)
cat("Regression Line Equation: y = ",B0," + ",B1,"X1 + ",B2,"X2")
df['ypred'] <- 0.29+0.19*df['X1']+0.69*df['X2']
ymean <- sum(df['y'])/10
df['y-ypred'] <- df['y']-df['ypred']
df['y-ymean'] <- df['y']-ymean
df['(y-ypred)^2'] <- df['y-ypred']*df['y-ypred']
df['(y-ymean)^2'] <- df['y-ymean']*df['y-ymean']
rss <- sum(df['(y-ypred)^2'])
tss <- sum(df['(y-ymean)^2'])
cat(rss,tss)
rsq <- round(1-(rss/tss),digits=2)
rsq
rmse <- (sum(df['(y-ypred)^2'])/10)**(0.5)
cat("RMSE:",rmse)


# 1. Perform the given task using R (in built functions)
# a) Read dataset “advertising.csv”
# b) Divide data into training and testing split
# c) Apply multiple linear regression
# d) Predict for test data
df<-read.csv('Advertising.csv')
df
sample <- sample(c(TRUE, FALSE), nrow(df), replace=TRUE, prob=c(0.7,0.3))
train<-df[sample,]
test<-df[!sample,]
model<-lm(TV~Radio+Newspaper+Sales,data=df)
y_pred<-predict(model,newdata=test)
y_pred


# 1. Perform the given task in R
# Consider the following data
# X 0 1 2 3 4 5 6 7 8 9
# y 1 3 2 5 7 8 8 9 10 12
# 
# a) Print first 5 rows of data
# b) Display scatter plot of data
# c) Calculate(using formula) and print regression coefficients b0 and b1
# d) Display regression line equation
# e) Calculate and print coefficient of determination (R squared, Residual sum of
#                                                      squares (RSS), and RMSE
#                                                      f) Plot regression line
#g) Predict the value of y given x=10
library(ggplot2)
X<-c(0,1,2,3,4,5,6,7,8,9)
y<-c(1,3,2,5,7,8,8,9,10,12)
df<-data.frame(X,y)
head(df,5)
ggplot(df,aes(X,y,col='red'))+
  geom_point()+
  xlab("X")+
  ylab("y")+
  ggtitle("Data Spread")
df['XY'] <- df['X']*df['y']
df['X^2'] <- df['X']*df['X']
ymean <- sum(df['y'])/10
xmean <- sum(df['X'])/10
B1 <- ((10*sum(df['XY']))-(sum(df['X'])*sum(df['y'])))/((10*sum(df['X^2']))-((sum(df['X']))**(2)))
B1 <- round(B1,digits=2)
B0 <- ymean-(B1*xmean)
B0 <- round(B0,digits=2)
cat("B0: ",B0)
cat("B1: ",B1)
cat("Regression Line Equation: y=",B0,"+",B1,"X")
df['ypred'] <- B0+(B1*df['X'])
df['y-ypred'] <- df['y']-df['ypred']
df['(y-ypred)^2'] <- df['y-ypred']**2
rss <- sum(df['(y-ypred)^2'])
rss <- round(rss,digits=2)
cat("RSS: ",rss)
ymean <- sum(df['y'])/10
df['y-ymean'] <- df['y']-ymean 
df['(y-ymean)^2'] <- df['y-ymean']**2
tss <- sum(df['(y-ymean)^2'])
tss <- round(tss,digits=2)
cat("TSS: ",tss)
rsq <- 1-(rss/tss)
rsq <- round(rsq,digits=2)
cat("R-Squared: ",rsq)
rmse <- ((sum(df['(y-ypred)^2'])/10)**(0.5))
rmse <- round(rmse,digits=2)
cat("RMSE: ",rmse)
ggplot(df,aes(X,y,col='red'))+
  geom_point()+
  xlab("X")+
  ylab("y")+
  ggtitle("Regression Line")+
  geom_smooth(method='lm')
cat("The value of y given x=10:\ny =",(B0+(B1*10)))


# Perform the following task using R (using direct functions available)( (Use lm function, summary
#                                                                         function, predict function, plot function)
#                                                                        a) Read data set (advertising.csv)
# b) Select the column ‘TV’ as independent variable and ‘sales’ as dependent variable
# c) Divide data into training and testing split
# d) Apply linear regression using function available.
# e) Get coefficients of regression and coefficient of determination from the model
# f) Apply the model for predictions on testing data.
df<-read.csv('Advertising.csv')
df<-df[,c("TV","Sales")]
sample <- sample(c(TRUE,FALSE),nrow(df),replace=TRUE,prob=c(0.7,0.3))
train<-df[sample,]
test<-df[!sample,]
model<-lm(TV~Sales,data=df)
model.score(test)
summary(model)$r.squared
coef <- coef(summary(model))["Sales", "Estimate"]
cat("Coefficient of regression (slope):", coef, "\n")
cat("Coefficient of determination:", summary(model)$r.squared)
pred <- predict(model,newdata=test)
pred


# Install dplyr package
# Load dplyr package
# Create data frame containing 8 rows and columns as id, name, gender, age, and ity. Also use
# row.names as r1,r2….
# Display rows where gender is M (Use filter)
# Display rows with female and city Mumbai (use filter)
# Display single column(use select)
# Display multiple columns(use select)
# Display any 4 rows (use slice)
# Change the name of any person (use mutate)
# Change the name of any column (use rename)
# Sort the dataframe in ascending order of age (use arrange)
install.packages("dplyr")
library(dplyr)
id <- c("r1","r2","r3","r4","r5","r6","r7","r8")
name <- c("Tom","Tommy","Jhandeya","Gege","Ram","Sham","Rum","Keith")
gender <- c("M","M","F","F","M","M","F","M")
age <- c(40,40,39,29,5,68,75,2)
city <- c("Mumbai","Bangalore","Mumbai","Agra","Chennai","Bhopal","Agra","Pune")
df <- data.frame(id,name,gender,age,city)
filter(df,gender=="M")
filter(df,gender=="M" & city=="Mumbai")
select(df,id)
select(df,id,name,age)
slice(df,1:4)
mutate(df,name=ifelse(name=="Gege","Gigi",name))
rename(df,city_name=city)
arrange(df,age)


# Do the following in R
# Consider “airquality” dataset
# 1. print out the first 5 rows of airquality data set
# 2.Calculate the mean, median, mode of “temperature” column of dataset
# 3.Calculate variance and std. deviation of that column data
# 4. Get the five number summary of that column data(use quantile)
# 5. Get the summary of entire dataset(use summary)
# 6. plot the histogram of that column data
# 7.plot QQ plot for it
df <- read.csv('AirQuality.csv')
head(df,5)
mean(df$Temp)
median(df$Temp)
install.packages("modeest")
library(modeest)
mfv(df$Temp)
quantile(df$Temp,probs=c(0,0.25,0.5,0.75,1))
summary(df)
hist(df$Temp,main="Histogram for Temperature",xlab="Temperature",ylab="Frequency",col="blue")
qqnorm(df$Temp)
qqline(df$Temp)


# Do the following in R
# Consider “airquality” dataset
# 1. print out the first 5 rows of airquality data set
# 2.Calculate the mean, median, mode of “temperature” column of dataset
# 3. Draw a boxplot for “ozone” column
# 4. Draw a scatterplot for finding relation between “temperature” and “ozone”
df <- read.csv("AirQuality.csv")
head(df,5)
mean(df$Temp)
median(df$Temp)
library(modeest)
mfv(df$Temp)
boxplot(df$Ozone, main="Ozone Boxplot",col="blue")
plot(df$Temp,df$Ozone,main="Temperature vs Ozone",col="red")


# Do the following in R
# consider data set esoph in R
# Draw a boxplot of the number of cancer cases according to each age group
# Draw a boxplot of the number of cancer cases according to each level of alcohol consumption
# draw a scatterplot between any two attributes
df <- read.csv('esoph.csv')
color=c('red','blue','green','yellow','pink','purple')
boxplot(ncases ~ agegp,data=df,main="Boxplot for Number of Cases vs age group",col=color)
boxplot(ncases ~ alcgp,data=df,main="Boxplot for Number of Cases for Alcohot consumption age groups",col=color)
plot(df$ncontrols, df$ncases, main = "Tobacco and Cancer Cases", xlab = "Tobacco Group", ylab = "Number of Cancer Cases",col='red')


# Do following in R
# 1. Create two vectors and perform arithmetic, relational and logical operators on them.
# Try to perform arithmetic operations on different sized vectors and observe the output.
# 2. Apply functions like mean, median, mode, std. deviation, max, min, cumsum to vector
# 3. Apply functions like typeof(), length(), rep(), seq(),any(),all() to vector
# 4. Write a program to find sum of digits of three digit number
# 5. Write a R program to sort a Vector in ascending and descending order.(use sort)
# 6. Write a R program to test whether a given vector contains a specified element.(use is.element)
x <- c(1,2,3)
y <- c(4,5,6)
x+y
x-y
x*y
x/y
x<y
x>y
x==y
x!=y
x<2 | y>5
x<2 & y>5
!(x<2)
x <- c(2,3,5,7,11)
mean(x)
median(x)
library(modeest)
mlv(x)
sd(x)
var(x)
max(x)
min(x)
cumsum(x)
typeof(x)
length(x)
rep(x,times=3)
seq(from = 1, to = 10, by = 2)
any(x<4)
all(x<20)
num <- as.numeric(readline("Enter a 3 digit number:"))
d1 <- num%/%100
d2 <- num %/% 10 %% 10
d3 <- num %% 10
sum_digits <- d1 + d2 + d3
cat("The sum of digits is:", sum_digits)
x <- c(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
sort(x)
sort(x,decreasing = TRUE)
x <- c(2, 3, 5, 7, 11)
is.element(5,x)
is.element(4,x)


# Do following in R
# 1. Write a R program to count the specific value in a given vector.
# 2. Write a R program to access the last value in a given vector.(use tail)
# 3. Write a R program to find second highest value in a given vector.(use sort, partial)
# 4. Write a R program to find common elements from multiple vectors.(use intersect)
# 5. Write a R program to list the distinct values in a vector from a given vector.(use unique)
# 6. Write a R program to find the elements of a given vector that are not in another given
# vector.(use setdiff)
vec <- c(1, 2, 3, 2, 4, 2, 5)
sum(vec == 2)
tail(vec,1)
sort(vec,decreasing = TRUE)[2]
vec1 <- c(1, 2, 3, 4, 5)
vec2 <- c(4, 5, 6, 7, 8)
intersect(vec1, vec2)
unique(vec)
vec1 <- c(1, 2, 3, 4, 5)
vec2 <- c(4, 5, 6, 7, 8)
setdiff(vec1,vec2)
setdiff(vec2, vec1)


# Do the following task in R
# 1. Apply the simple linear regression model for the data set “faithful”, and estimate the next
# eruption duration if the waiting time since the last eruption has been 80 minutes also plot the
# best fit line.
# 2. Find the coefficient of determination for the simple linear regression model of the data set
# faithful.
# 3. Plot the residual of the simple linear regression model of the data set faithful against the
# independent variable waiting.
data(faithful)
fit <- lm(eruptions ~ waiting, data=faithful)
summary(fit)
predict(fit,data.frame(waiting=80))
plot(faithful$waiting,faithful$eruptions,main="Olf Faithful Eruptions",xlab="Waiting Time",ylab="Eruption Duration")
abline(fit,col="red")
rsq <- summary(model)$r.squared
data(faithful)
model <- lm(eruptions ~ waiting,data=faithful)
resid <- residuals(model)
plot(faithful$waiting, resid, xlab="Waiting", ylab="Residuals",main="Residual plot")


# Do the following in R
# 1. Apply the multiple linear regression model for the data set “stackloss”, and predict the stack
# loss if the air flow is 72, water temperature is 20 and acid concentration is 85.
# 2. Find the coefficient of determination for the multiple linear regression model of the data set
# stackloss.
# 3. . Find the covariance of eruption duration and waiting time in the data set faithful. Observe if
# there is any linear relationship between the two variables.
# 4. Find the correlation coefficient of eruption duration and waiting time in the data set faithful.
# Observe if there is any linear relationship between the variables.
data(stackloss)
stackloss
model <- lm(stack.loss ~ Air.Flow+Water.Temp+Acid.Conc.,data=stackloss)
newdata <- data.frame(Air.Flow=72,Water.Temp=20,Acid.Conc.=85)
predict(model,newdata=newdata)
summary(model)$r.squared
data(faithful)
cov(faithful$eruptions,faithful$waiting)
cat("13.97 means there is a positive linear relationship between the two variables")
cor(faithful$eruptions,faithful$waiting)
cat("A strong positive linear relationship between the two variables.")


# 1. Write a R program
# a. To create a data frame from four given vectors.(emp_id,
#                                                    emp_name,salary,start_date)
# b. To get structure of a given data frame.(use str)
# c. Write a R program to get the statistical summary and nature of the data
# of a given data frame.(use summary)
# d. print i)specific column from a data frame using column name. ii)first two
# rows iii) 3rdand 5throws with 1stand 3rdcolumns
# 5. Write a R program to i)add a new column(say dept ii) to add new row
# iii) to drop column dept iv) to drop row(s) by number in a given data frame.
emp_id <- c(101,102,103,104,105)
emp_name <- c("John","Mary","David","Peter","Sara")
salary <- c(50000,60000,55000,65000,70000)
start_date <- c("2010-01-01", "2012-06-30", "2014-02-15", "2016-09-01", "2018-05-10")
df <- data.frame(emp_id,emp_name,salary,start_date)
str(df)
summary(df)
df$emp_id
df[1:2,]
df[c(3,5),c(1,3)]
df$dept <- c("IT","HR","Sales","IT","Marketing")
df <- rbind(df, c(106,"Mark",62000,"2023-04-01","Sales"))
df$dept <- NULL
df <- df[-3,]


# Consider “iris” dataset
# Give R codes to generate any three following graphs
data(iris)
library(ggplot2)
ggplot(iris,aes(Sepal.Length,Sepal.Width,col=Species))+
  geom_point()+
  xlab("Sepal Length")+
  ylab("Sepal Width")+
  ggtitle("Sepal Length-Width")+
  labs(color = "Species")

ggplot(iris,aes(x=Sepal.Width,fill=Species))+
  geom_histogram(binwidth=0.2,color="black")+
  xlab("Sepal Width")+
  ylab("Frequency")+
  ylim(0,38)+
  xlim(2,5)+
  ggtitle("Histogram of Sepal Width")
  
ggplot(iris,aes(x=Species,y=Sepal.Length,fill=Species))+
  geom_boxplot()+
  xlab("Species")+
  ylab("Sepal Length")+
  ggtitle("Iris Boxplot")


# Consider “iris” dataset
# Give R codes to generate any three following graphs
library(ggplot2)
ggplot(iris,aes(x=Sepal.Width))+
  geom_histogram(aes(y=..density..),binwidth=0.2,color="black",fill="lightblue")+
  geom_density(alpha=0.2,fill="lightblue")+
  xlab("Sepal Length") +
  ylab("Density") +
  xlim(2,5)+
  ggtitle("Histogram with Density Curve for Sepal Width")

ggplot(iris,aes(x=Species,y=Sepal.Length,fill=Species))+
  geom_violin()+
  geom_density(alpha=0)+
  xlab("Density") +
  ylab("Sepal Length")

ggplot(iris,aes(x=Sepal.Length,y=Sepal.Width,col=Species,shape=Species))+
  geom_point()+
  geom_smooth(method="lm")+
  xlab("Sepal Length")+
  ylab("Sepal Width")+
  ggtitle("Faceting")+
  facet_wrap(~Species)

# 1. Import seaborn library
# 2. Load “titanic” dataset from the seaborn library
# 3. Create Following plots and give appropriate title to each plot
# i. box plot for “fare”(y axis) with respect to “class”(x axis).
# ii violin plot for “age” with respect to “sex”.
# iii line plot for “fare” and “embarked”
# iv. Bar plot for “fare” with respect to “embarked”

import seaborn as sns

df = sns.load_dataset('titanic')
df

sns.boxplot(data = df,x='class',y='fare').set_title('Boxplot')

sns.violinplot(data=df,x='sex',y='age').set_title('Violin Plot')

sns.lineplot(data=df,x='embarked',y='fare').set_title('Line Plot')

sns.barplot(data=df,x='embarked',y='fare').set_title('Bar Plot')

# 1. Load “iris” dataset from seaborn library
# 2. Create Following plots and give appropriate title to each plot
# i. scatter plot for “sepal_length” and “petal_length”
# ii. Regression using lmplot() for “sepal_width” and “petal_width”
# iii. Regression using regplot() for “petal_length” and “petal_width”
# iv. Using “PairGrid” on “iris” dataset show the pairwise relationships in
# the dataset. Plot histogram on diagonal. Show different colors for
# three species.

df = sns.load_dataset('iris')
df

sns.scatterplot(data=df,x='sepal_length',y='petal_length').set_title('Scatter Plot')

import matplotlib.pyplot as plt
sns.lmplot(data=df,x='petal_width',y='sepal_width')
plt.title('Regression Line with lmplot')

sns.regplot(data=df,x='petal_length',y='petal_width')
plt.title('Regression Line using regplot')

sns.PairGrid(df,hue='species').map_diag(sns.histplot)

# 1. Make a corpus of 3 sentences (consider one sentence as one document)
# 2.Calculate TF-IDF for each word in the document by applying standard formula (using python)
corpus = [
    "this is the first document.",
    "this is the second document.",
    "and this is the third document."
    ]
word_dump=[]
for i in corpus:
  temp = i.split(" ")
  for j in temp:
    if j not in word_dump:
      word_dump.append(j)
print(word_dump)

tf1 = []
tf2 = []
tf3 = []
idf = []
tfidf1 = []
tfidf2 = []
tfidf3 = []

for i in word_dump:
  count=0
  for j in corpus[0].split(" "):
    if i==j:
      count+=1
  tf1.append(count/len(corpus[0].split(" ")))
  count=0
  for j in corpus[1].split(" "):
    if i==j:
      count+=1
  tf2.append(count/len(corpus[1].split(" ")))
  count=0
  for j in corpus[2].split(" "):
    if i==j:
      count+=1
  tf3.append(count/len(corpus[2].split(" ")))
print(tf1,tf2,tf3)

import math
for i in word_dump:
  count = 0
  for j in corpus:
    if i in j.split(" "):
      count+=1
  idf.append(math.log(len(corpus)/count))
idf = [round(i,2) for i in idf]
print(idf)

for i in range(len(idf)):
  tfidf1.append(tf1[i]*idf[i])
  tfidf2.append(tf2[i]*idf[i])
  tfidf3.append(tf3[i]*idf[i])
print(tfidf1)
print(tfidf2)
print(tfidf3)

#Calculate TF-IDF for each word in the document by using inbuilt function in python

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_vectors = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()
for i in range(len(corpus)):
    print("Document ", i+1, ":")
    tfidf_vector = tfidf_vectors[i]
    for j in range(len(feature_names)):
        print(feature_names[j], ":", tfidf_vector[0, j])
    print()

# Do following using python
# 1. Import time series data
# 2. display first 5 rows and last five rows of the data
# 3. Show the line-plot of the given time series data
# 4. Import seasonal_decompose from the statsmodels package
# 5. Pass data frame into the seasonal_decompose method and plot the result (Consider additive
# model)
# 6. Import the augmented Dickey-Fuller test from the statsmodels package
# 7. Comment on the stationarity of data

import pandas as pd 
df = pd.read_csv('time_series.csv', index_col='Date')
df.head(5)

df.tail(5)

import seaborn as sns
sns.lineplot(data=df,x='Date',y='Births')

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
result = seasonal_decompose(df['Births'], model='additive', period=1)
result.plot()
plt.show()

from statsmodels.tsa.stattools import adfuller
adf_test = adfuller(df['Births'])
print(f'ADF Statistic: {adf_test[0]}')
print(f'p-value: {adf_test[1]}')
print(f'Critical Values: {adf_test[4]}')
print("Pretty stationary data")

# Do following using python
# 1. Import time series data
# 2. Divide the data in training and testing set. Plot the data with different colors
# 3. Apply ARIMA model of order(1,1,2) and generate predictions
# 4. Display train data, test data and predicted data with different colored lines
# 5. Calculate root mean squared error (RMSE) between test data and predicted data

df = pd.read_csv("time_series.csv")

df.shape

train = df['Births'].iloc[:-292]
test = df['Births'].iloc[-292:]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(train, color='blue', label='Training Data')
plt.plot(test, color='green', label='Testing Data')
plt.legend()
plt.show()

from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(train, order=(1,1,2))
model_fit = model.fit()
predictions = model_fit.forecast(steps=292)

plt.figure(figsize=(10,6))
plt.plot(train, color='blue', label='Training Data')
plt.plot(test, color='green', label='Testing Data')
plt.plot(predictions, color='red', label='Predictions')
plt.legend()
plt.show()

from sklearn.metrics import mean_squared_error
import numpy as np
mse = mean_squared_error(test, predictions)
rmse = np.sqrt(mse)
print('Root Mean Squared Error:', rmse)

# Do following using python
# 1. Import time series data
# 2. Show the line-plot of the given time series data
# 3. Apply ARIMA model of order(1,1,1)
# 4. Calculate root mean squared error (RMSE) between test data and predicted data

import pandas as pd
import matplotlib.pyplot as plt
date_rng = pd.date_range(start='1/1/2022', end='12/1/2022', freq='MS')
temps = [15, 18, 20, 25, 28, 30, 33, 32, 29, 25, 20, 16]
df = pd.DataFrame({'date': date_rng, 'temp': temps})
df.set_index('date', inplace=True)
plt.plot(df.index, df['temp'])
plt.title('Average Temperature by Month')
plt.xlabel('Date')
plt.ylabel('Temperature (Celsius)')
plt.show()

train = df.iloc[-9:]
test = df.iloc[:-9]

from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(train,order=(1,1,1))
model_fit = model.fit()
predictions = model_fit.forecast(steps=3)

from sklearn.metrics import mean_squared_error
import numpy as np
mse = mean_squared_error(test, predictions)
rmse = np.sqrt(mse)
print('Root Mean Squared Error:', rmse)

# 1. Perform the given task in python (without using direct functions available)
# Consider the following data
# X1 10 12 10 9 15 10 14 15 15 16
# X2 8 12 9 9 11 9 11 14 11 12
# y 10 10 10 9 11 11 9 9 10 10

# a) Print first 5 rows of data
# b) Display scatter plot of data
# c) Calculate(using formula) and print regression coefficients b0,b1 and b2
# d) Display regression line equation
# e) Calculate and print coefficient of determination (R squared, Residual sum of
# squares (RSS), and RMSE
# f) Plot regression line
# g) Predict the value of y given x1=10, x2=11

import pandas as pd 
df = pd.DataFrame({'X1':[10,12,10,9,15,10,14,15,15,16],
                   'X2':[8,12,9,9,11,9,11,14,11,12],
                   'y':[10,10,10,9,11,11,9,9,10,10]})
df.head(5)

import seaborn as sns
sns.scatterplot(data=df,x='X1',y='y',color='red')
sns.scatterplot(data=df,x='X2',y='y',color='blue')

df['X1Y'] = df['X1']*df['y']
df['X2^2'] = df['X2']*df['X2']
df['X2Y'] = df['X2']*df['y']
df['X1X2'] = df['X1']*df['X2']
df['X1^2'] = df['X1']*df['X1']

B1 = (sum(df['X1Y'])*(sum(df['X2^2']))-(sum(df['X2Y']))*(sum(df['X1X2'])))/(sum(df['X1^2'])*sum(df['X2^2'])-(sum(df['X1X2'])*sum(df['X1X2'])))
B2 = (sum(df['X2Y'])*(sum(df['X1^2']))-(sum(df['X1Y']))*(sum(df['X1X2'])))/(sum(df['X1^2'])*sum(df['X2^2'])-(sum(df['X1X2'])*sum(df['X1X2'])))
B0 = (sum(df['y'])/10)-B1*(sum(df['X1'])/10)-B2*(sum(df['X2'])/10)

B0 = round(B0,2)
B1 = round(B1,2)
B2 = round(B2,2)

print("B0: ",B0)
print("B1: ",B1)
print("B2: ",B2)

print("Regression Line Equation: y = {} + {}X1 + {}X2".format(B0,B1,B2))

df['ypred'] = 0.29+0.19*df['X1']+0.69*df['X2']

ymean = sum(df['y'])/10
df['y-ypred'] = df['y']-df['ypred']
df['y-ymean'] = df['y']-ymean

df['(y-ypred)^2'] = df['y-ypred']*df['y-ypred']
df['(y-ymean)^2'] = df['y-ymean']*df['y-ymean']

rss = sum(df['(y-ypred)^2'])
tss = sum(df['(y-ymean)^2'])

rss,tss

rsq = round(1-(rss/tss),2)
rsq

import numpy as np
rmse = np.sqrt(sum(df['(y-ypred)^2'])/10)
print("RMSE:",rmse)

df

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(np.column_stack((df['X1'][:-2], df['X2'][:-2])), df['y'][:-2])

y_pred = lr.predict(np.column_stack((df['X1'][-2:],df['X2'][-2:])))
y_pred

plt.figure(figsize=(3,3))
plt.ylim(6,15)
plt.xlim(6,17)
plt.scatter(df['X1'], df['y'], label='x1')
plt.plot(df['X1'][-2:],y_pred,color="red", linewidth=2)

print("Predicted value of y at x1=10, x2=11:",0.29+0.19*10+0.69*11)

# 1. Perform the given task using python (in built functions)

# a) Import the packages numpy, pandas, seaborn  and the sklearn.linear_model
# b) Read dataset “advertising.csv”
# c) Divide data into training and testing split
# d) Apply multiple linear regression
# e) Predict for test data

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Advertising.csv')
df

from sklearn.model_selection import train_test_split
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

model.score(X_test,y_test)

# 1. Perform the given task in python (without using direct functions available)
# Consider the following data
# X 0 1 2 3 4 5 6 7 8 9
# y 1 3 2 5 7 8 8 9 10 12

# a) Print first 5 rows of data
# b) Display scatter plot of data
# c) Calculate(using formula) and print regression coefficients b0 and b1
# d) Display regression line equation
# e) Calculate and print coefficient of determination (R squared, Residual sum of
# squares (RSS), and RMSE
# f) Plot regression line
# g) Predict the value of y given x=10

import pandas as pd 
df = pd.DataFrame({'X':[0,1,2,3,4,5,6,7,8,9],
                  'y':[1,3,2,5,7,8,8,9,10,12]})
df.head(5)

import seaborn as sns
sns.scatterplot(data=df,x='X',y='y',color='red')

df['XY'] = df['X']*df['y']
df['X^2'] = df['X']*df['X']

ymean = sum(df['y'])/10
xmean = sum(df['X'])/10
B1 = ((10*sum(df['XY']))-(sum(df['X'])*sum(df['y'])))/((10*sum(df['X^2']))-((sum(df['X']))**(2)))
B1 = round(B1,2)

B0 = ymean-(B1*xmean)
B0 = round(B0,2)

print("B0: ",B0)
print("B1: ",B1)

print("Regression Line Equation: y = ",B0," + ",B1,"X")

df['ypred'] = B0+(B1*df['X'])

df['y-ypred'] = df['y']-df['ypred']
df['(y-ypred)^2'] = df['y-ypred']**2
rss = sum(df['(y-ypred)^2'])
rss = round(rss,2)
print("RSS: ",rss)

df['y-ymean'] = df['y']-ymean 
df['(y-ymean)^2'] = df['y-ymean']**2
tss = sum(df['(y-ymean)^2'])
tss = round(tss,2)
print("TSS: ",tss)

rsq = 1-(rss/tss)
rsq = round(rsq,2)
print("R-Squared: ",rsq)

rmse = ((sum(df['(y-ypred)^2'])/10)**(0.5))
rmse = round(rmse,2)
print("RMSE: ",rmse)

import matplotlib.pyplot as plt
def linefitline(x):
    return B0 + B1 * x
line1 = linefitline(df['X'])
plt.scatter(df['X'],df['y'])
plt.plot(df['X'],line1, c = 'red')
plt.show()

print("The value of y given x=10:- \ny =",B0+(B1*10))

# .Perform the following task using python (using direct functions available)
# a) Import the packages numpy, pandas and the sklearn.linear_model
# b) Read data set (advertising.csv)
# c) Select the column ‘TV’ as independent variable and ‘sales’ as dependent variable
# d) Divide data into training and testing split
# e) Apply linear regression using function available.
# f) Get coefficients of regression and coefficient of determination from the model
# g) Apply the model for predictions on testing data.

import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Advertising.csv')
df.head()

X = df.iloc[:,0]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=42)

X_train = X_train.values.reshape(-1,1)
X_test = X_test.values.reshape(-1,1)
y_train = y_train.values.reshape(-1,1)
y_test = y_test.values.reshape(-1,1)

model = LinearRegression()
model.fit(X_train,y_train)

print("Coefficient of Regression:",round(model.coef_[0][0],2),"\nCoefficient of Determination:",round(model.score(X_train,y_train),2))

y_pred = model.predict(X_test)
y_pred

# 1.
# Create a NumPy array.
# Create an identity matrix using eye() and identity() function.
# Create a 5x5 2D array for random numbers between 0 and 1.
# Sum an array along the column.
# Sum an array along the row.
#  Calculate the mean, median, standard deviation, and variance.
# Sort an array along the row using the sort() function.
# Append elements to an array using the append() function.
# Delete multiple elements in an array.
# Concatenate elements from 2 arrays.

import numpy as np
num_arr = np.array([0,1,2,3,4,5,6,7,8,9])
num_arr

eye_arr = np.eye(3)
eye_arr

identity_arr = np.identity(3)
identity_arr

random_arr = np.random.rand(5,5)
random_arr

col_sum = np.sum(random_arr,axis=0)
col_sum

row_sum = np.sum(random_arr,axis=1)
row_sum

print("Mean:",np.mean(random_arr))
print("Median:",np.median(random_arr))
print("Standard Deviation:",np.std(random_arr))
print("Variance:",np.var(random_arr))

sort_arr = np.sort(random_arr,axis=1)
sort_arr

appended_arr = np.append(random_arr,[0.0001,0.0002,0.0003,0.0004,0.0005])
appended_arr

del_arr = np.delete(random_arr,[0,1])
del_arr

arr1 = np.array([0,1,2,3,4])
arr2 = np.array([5,6,7,8,9])
concat_arr = np.concatenate((arr1,arr2))
concat_arr

# Load the dataset mtcars using pandas read_csv() function.
# Display the head of the dataset using the head() function.
# Display the bottom 5 rows from the dataset using the tail() function.
# Print summary statistics of the dataset using the describe() function.
# Plot a histogram for atleast 3 variables.
# Box plot to visualize the relationship between any two variable
# Drop irrelevant columns from the dataset using drop() function.

import pandas as pd
df = pd.read_csv('mtcars.csv')

df.head(5)

df.tail(5)

df.describe()

import matplotlib.pyplot as plt
df.hist(column=['mpg','cyl','vs'],bins=10)
plt.show()

df.boxplot(column=["mpg"],by=["cyl"],grid=False)
plt.show()

df = df.drop(["vs","am"],axis=1)
df.head(5)

# Load the dataset mtcars using pandas read_csv() function.
# Use rename() function to rename the columns.
# Print the total number of duplicate rows.
# Remove the duplicate rows using the drop_duplicates() function.
# Drop the missing values from the dataset.
# Plot a histogram to find the number of cars per number of cylinders.
# Load the dataset tips using pandas read_csv() function.
# Draw a scatter plot between day and tip (use colorbar)
# Draw line chart and bar chart between day and tip

import pandas as pd
df = pd.read_csv('mtcars.csv')

df.head()

df = df.rename(columns={"mpg":"Col 1"})
df.head()

print("Number of duplicate rows:",df.duplicated().sum())

df = df.drop_duplicates()

df = df.dropna()

df.hist('cyl',bins=[0,2,4,6,8,10])
plt.xlabel("Number of Cylinders")
plt.ylabel("Number of Cars")
plt.title("Number of Cars vs Number of Cylinders")
plt.show()

df = pd.read_csv('tips.csv')
df.head()

plt.scatter(data=df,x='day',y='tip')
plt.colorbar()
plt.xlabel("Days")
plt.ylabel("Tip")
plt.title("Tips on each day of the week")
plt.show()

df.groupby("day")["tip"].mean().plot(kind="line", marker="o")
plt.xlabel("Days")
plt.ylabel("Tip")
plt.title("Line Plot for Tips on each day of the week")
plt.show()

df.groupby("day")["tip"].mean().plot(kind="bar")
plt.xlabel("Days")
plt.ylabel("Tip")
plt.title("Bar Plot for Tips on each day of the week")
plt.show()

# Consider “iris” dataset
# Give PYTHON codes to generate any three following graphs

import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
df

colors = {'setosa':'red','versicolor':'green','virginica':'blue'}
shapes = {'setosa':'o','versicolor':'^','virginica':'s'}
sns.scatterplot(data=df,x='sepal_length',y='sepal_width',style='species',hue='species',palette=colors,markers=shapes,alpha=0.5)
plt.show()

labels=['setosa','versicolor','virginica']
colors=['red','green','blue']
sns.boxplot(data=df,x='species',y='sepal_length',palette=colors,saturation=0.3)
plt.legend(title='Species',labels=labels)
plt.show()

sns.histplot(data=df[df['species']=='setosa'],x='sepal_width',color="red")
sns.histplot(data=df[df['species']=='versicolor'],x='sepal_width',color="green")
sns.histplot(data=df[df['species']=='virginica'],x='sepal_width',color="blue")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.legend(title="Species",labels=labels,loc="center right",bbox_to_anchor=(1.3,0.5))
plt.show()

sns.histplot(data=df,x='sepal_width',kde=True)
plt.show()

g = sns.FacetGrid(df,col='species',hue='species',palette=colors)
g.map(sns.scatterplot,'sepal_length','sepal_width')
g.map(sns.regplot,'sepal_length','sepal_width')
plt.show()

colors=["red","green","blue"]
labels=['setosa','versicolor','virginica']
sns.violinplot(df,x='species',y='sepal_length',palette=colors,saturation=0.3)
plt.legend('species',labels=labels,loc="center right",bbox_to_anchor=(1.3,0.5))
plt.show()"""