# Project_Financial_Markets_Text_Mining

The goal of this project it to analyze the text information related to financial markets and make prediction about the stock market movements on a daily basis.

Our project is trying to predict the daily stock price movement of S&T500 based on information conveyed by Reuters, applying Naïve Bayesians learning algorithm to do text mining.

## Data

The prediction is not in terms of number, while the way we define price movements is either upward movement or downward. Namely, the predicted variable is a nominal variable with only two outcomes illustrated by the following table. The data on daily price would be downloaded from Yahoo Finance. Currently, we would adopt the latest data over a one-year time from, from March 2017 to March 2018.

|Prediction(t)||
| ------------- | ------------- |
|Positive:|Price(t+1) – Price(t) > 0|
|Negative:|Price(t+1) – Price(t) < 0|

The feature is public news on financial markets stored in the form of string.

For each record of each date, data for News would be collected from Reuters official website through a Python web crawler. However, not all of articles on Reuters would be considered; we only choose information from summaries of each article under Financials, Business, Marketing, and Investment channels of Reuters. These channels are highly corelated to financial market, compared with other channels in Reuters. One practical reason why only summaries are considered is that if every article is taken into account, the size of data for each day would be around 0.8 MB which is crazily large and not feasible to operation on a common PC. Another reason is we believe the summary section would provide enough crucial information to make prediction because usually editors would put many key words in the summary. Finally, the reason why we choose Reuters as our data source is based on the clear web structure making web crawler easy to work and the its respectable reputation.

## Data Processing

|Remove Numbers|Remove all numerical information including “ 1.2%, 233…”|
|Remove common words|Frequent words like “I, we, us, and, but …” would be removed because these words do not provide useful information. In addition, words describing date, time such as “Sept, 14:23, afternoon…” would also be removed.|
|Lower letter|All word would be transformed into lowercase|
|Stemming word|E.g. “look, looking, looked, looks” would be seen as one word, “look”, because they offer same information.|
|Remove Frequently-used word in both positive and negative category|Words appear more than many times whatever the responsive value are useless to make prediction, and thus are removed. For example, no matter either market goes up or down, words like” markets, wall street, finance” would still be mentioned a lot of times but have nothing to do with outcome. The definition of “Frequently-used” would be determined in trial-and-error manner.|

## Model

