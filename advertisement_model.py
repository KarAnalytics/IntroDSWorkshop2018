## Objective: Fit simple linear regression model using R

adv <- read.csv("Advertising.csv")  ## The dataset used in class

## Visualize how Sales is individually related to television, radio and news advertisement
plot(adv$Sales,adv$TV)  ## Better correlation but possibly non-linear
plot(adv$Sales,adv$Radio) ## Lesser correlation
plot(adv$Sales,adv$Newspaper)

## Fit the model
model = lm(Sales ~ TV + Newspaper + Radio, data = adv)

## Summarize the model
summary(model)
