# Coronavirus-Prediction-Model

Coronavirus Prediction Model

Worked by: Mammadgulu Novruzov, Sevana Ahmadzada, Mahmud Ahmadov and Samir Aliyev

Currently world is suffering deadly disease, and our country is struggling too. We as a team, decided to visualize the situation and predict next days new cases and new death.
(Data acquisition. By Mammadgulu Novruzov)
We started by collecting data about daily diseases, from the website “koronavirusinfo.az”, where we can get all needed information about virus effects in country. We collected data using web-scraping (BeautifulSoup library) and collected data into csv file. We were able to collect data only between dates 13.04-06.06.2020. The rest of data was added manually, as after date 6th June, information is given in pdf format and before 13th of April, data style is not consistent.

After collecting and doing some ML training, we wanted to compare our results with other countries (specifically Italy, as virus peaked there). After some research, we found website: https://ourworldindata.org/coronavirus-data-explorer where daily data of all countries are visualized in graph. Also, that website contains csv file with that information. After downloading and researching dataset, we decided to continue our project with it.

(Data cleaning. By Samir Aliyev)
Our data had many columns. We decided to use following features: 
-	iso_code – three letter code of country
-	date – date of the given info
-	stringency_index – strictness level of quarantine (0 – no limits, 100 – strict)
-	new_cases_per_million – the number of new daily cases per million people
-	new_deaths_per_million – the number of new daily death per million people
-	population_density – population density of given country

The reason why we chose new_cases_per_million over new_cases is that this feature is more normalized considering all countries. After getting these features, we had to numericize our categorical feature: iso_code. As, label encoding would have side effect of number difference. For ex. AZE < ITA, if we encode data using Label Encoding, thus, ML model can choose AZE over ITA (or vice versa).  Because of this, we preferred to use one-hot encoding. This way, we have no previous problem, however our column size increases dramatically. As our dataset is not huge, it was fine.
Then, we extracted data of Azerbaijan from that dataset and plotted it, for visualization. As we have two output features (new_cases_per_million and new_death_per_million) we plotted for each of them separately.

After this, we extracted last two weeks data of Azerbaijan for future predictions and compare.

(Choosing a model. By Mahmud Ahmadov)
We searched and applied regression models, that we found. For this dataset we used following models with variance score of (5 times cross-validated):
 
	 Polynomial regression was degree of 2, our computer did not handle degree 3 (Memory Error: Not enough memory). As we can see from this model, Random Forest Regressor scored best among all (Polynomial is also good enough). We also plotted prediction vs real values of cases of last two weeks in Azerbaijan:


 











(Clustering. By Sevana Ahmadzada)
	We also decided to visualize our situation in the country. We decided to use clustering algorithm to divide into groups the situation in our country (mild, severe etc.) Situation can be decided by two features: new_cases_per_million and new_death_per_million. First, we had to find, optimal cluster number. For that, we used elbow method and came up with 4 as number of clusters:
After training unsupervised model, we colorized our labels and plotted graph:
Conclusion:
	Among models, Random Forest algorithm worked best for our dataset. As, we couldn’t find similar works to ours, we couldn’t compare our models with real life experiments. Since, we have more technical features of our models, but in other projects we see more general information about coronavirus pandemic. Those projects mainly show how many cases and deaths in particular countries, however we give deep information about models’ working principal. For future, we can do parameter tuning to increase the efficiency of Random Forest and try Polynomial regression with more degrees. 











Reference:
Ready  Dataset (all countries) from GitHub
https://github.com/owid/covid-19-data/tree/master/public/data

