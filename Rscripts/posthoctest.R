GHIBLI/MARVEL SCRIPT SENTIMENT

2/12/21

#---------
setwd("D:\\PROJECT\\sagitta\\CSV")
data <- read.csv("movie_sentiment.csv")
library(dplyr)
library(psych)

#-----
#Descriptive Statistics

data_sentiment <- select(data, producer, polarity, subjectivity)
describeBy(data_sentiment, group=data$producer)

#-----
#ANOVA polarity

polarity.lm <- lm(polarity ~ producer, data=data_sentiment)
polarity.av <- aov(polarity.lm)
summary(polarity.av)

pol.tukey <- TukeyHSD(polarity.av)
pol.tukey

#------
#ANOVA subj

subj.lm <- lm(subjectivity ~ producer, data=data_sentiment)
subj.av <- aov(subj.lm)
summary(subj.av)

subj.tukey <- TukeyHSD(subj.av)
subj.tukey

#------
plot(pol.tukey)
