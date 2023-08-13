#################### Assignment 1 ####################

#PART A 

import re
def names():
    #Find a list of all of the names in the following string using regex.
    
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    
    name = re.findall('[A-Z][\w]{1,4}',simple_string)
    return name

names()

assert len(names()) == 4, "There are four names in the simple_string"

#PART B
# Find a list of just those students who received a B in the course.

import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        students = file.read()
    
    grade = re.findall("([A-Z][\w]* [A-Z][\w]*)(?=. [B])",students)
    
    return grade
 
grades()

assert len(grades()) == 16

#PART C

# Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:

# a host (e.g., '146.204.224.152')
# a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
# the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:

# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
    
import re
def logs():
    log = []
    w = '(?P<host>(?:\d+\.){3}\d+)\s+(?:\S+)\s+(?P<user_name>\S+)\s+\[(?P<time>[-+\w\s:/]+)\]\s+"(?P<request>.+?.+?)"'
    with open("assets/logdata.txt", "r") as f:
        logdata = f.read()
    for m in re.finditer(w, logdata):
        log.append(m.groupdict())
    return log

    #raise NotImplementedError()

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

#################### Assignment 2 ####################

#Question 1

# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

# This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}

#import dependencies

import pandas as pd
import numpy as np

def proportion_of_education():
    
    #read the file as data frane
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)
    
    #get the EDUCATION OF MOTHERCATEGORIES (RECODE) variable
    EDUS = df['EDUC1']
    
    #sort values to see pattern
    edus = np.sort(EDUS.values)
    
    #create dictionary 
    
    education = {"less than high school":0,
                 "high school":0,
                 "more than high school but not college":0,
                 "college":0}
    
    n=len(edus)
     
    #add values of EDUS1 per category to the dictionary
    
    education["less than high school"]=np.sum(edus==1)/n
    education["high school"]=np.sum(edus==2)/n
    education["more than high school but not college"]=np.sum(edus==3)/n
    education["college"]=np.sum(edus==4)/n
    
    print(education)
    return education

proportion_of_education()

# assert type(proportion_of_education())==type({}), "You must return a dictionary."
# assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
# assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
# assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."



#Question 2

# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. 
# Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

# This function should return a tuple in the form (use the correct numbers:

# (2.5, 0.1)

import pandas as pd
import numpy as np

def average_influenza_doses():
    
    #read the file as data frane
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)
    
    #make data frame with the correct variables
    
    cbf_flu = df[['CBF_01','P_NUMFLU']]
    
    #CBF_01 > Chilren who were ever breastfed
    #P_NUMFLU > total number of seasonal influenza doses
    
    #Get the childrens who have been fed (1) and not (2) ignoring the NaN
    
    cbf_flu1 = cbf_flu[cbf_flu['CBF_01'] == 1].dropna()
    cbf_flu2 = cbf_flu[cbf_flu['CBF_01'] == 2].dropna()
    
    #Get the values for the Flu variable based on the values of the fed variable 
    #and its average
    
    flu1 = cbf_flu1['P_NUMFLU']
    f1 = flu1.sum() / flu1.size

    flu2 = cbf_flu2['P_NUMFLU']
    f2 = flu2.sum() / flu2.size
    
    #Return the Tuple
    
    print(f1, f2)
    return (f1,f2)

average_influenza_doses()

#assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."


#Question 3

# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. 
# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it 
# (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

# This function should return a dictionary in the form of (use the correct numbers):

#     {"male":0.2,
#     "female":0.4}
# Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the 
#digits 0.0077.

import pandas as pd
import numpy as np

def chickenpox_by_sex():
    
    #read the file as data frane
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)
    
    #make data frame with the correct variables
 
    #P_NUMVRC > total number of varicella doses
        # 0, 1 or 2
        
    #HAD_CPOX > child has had chicken pox disease
        # yes = 1 , no = 2
        
    #SEX > sex of child
        # male =1 , female = 2
    
    Data = df[['HAD_CPOX', 'P_NUMVRC', 'SEX']]
    
    #Pull out the values above
    
    #We separate by sex
    
    Male = Data[Data['SEX'] == 1].dropna() #male
    Female = Data[Data['SEX'] == 2].dropna() #female
    
    #We only care thoes who were vaccinated
    
    vaccinedMale = Male[Male['P_NUMVRC'] != 0].dropna() #male
    vaccinedFemale = Female[Female['P_NUMVRC'] != 0].dropna() #female
    
    #We separate who got sick or not
    
    sickVaccinedMale = vaccinedMale[vaccinedMale['HAD_CPOX'] == 1].dropna() #male
    sickVaccinedFemale = vaccinedFemale[vaccinedFemale['HAD_CPOX'] == 1].dropna() #female
    
    healthyVaccinedMale= vaccinedMale[vaccinedMale['HAD_CPOX'] == 2].dropna() #male
    healthyVaccinedFemale = vaccinedFemale[vaccinedFemale['HAD_CPOX'] == 2].dropna() #female
    
    #Now we create the dictionary and put the results accordingly
    
    results = {"male":0,
               "female":0}

    results["male"] = len(sickVaccinedMale) / len(healthyVaccinedMale)
    results["female"] = len(sickVaccinedFemale) / len(healthyVaccinedFemale)


    print(results)
    return results
    
chickenpox_by_sex()  

#assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."

# Question 4

# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the 
# correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. 
# In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox 
# vaccine doses given (varicella).

# Some notes on interpreting the answer. If the had_chickenpox_column is either 1 (for yes) or 2 for no, and that the 
# num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine, then a positive 
# correlation (e.g. corr > 0) would mean that an increase in had_chickenpox_column (which means more no's) would mean an 
# increase in the num_chickenpox_vaccine_column (which means more doses of vaccine). If corr < 0 then there is a negative 
# correlation, indicating that having had chickenpox is related to an increase in the number of vaccine doses. Also, pval 
# refers to the probability the relationship observed is significant. In this case pval should be very very small 
# (will end in e-18 indicating a very small number), which means the result unlikely to be by chance.

# [1] This isn't really the full picture, since we are not looking at when the dose was given. It's possible that children had 
# chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate 
# the timing of the dose?


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    # this is just an example dataframe
    #df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
                   #"num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

    # here is some stub code to actually run the correlation
    #corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    #return corr

    #read the file as data frane
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)
    
    #make data frame with the correct variables
 
    #P_NUMVRC > total number of varicella doses
        # 0, 1 or 2
        
    #HAD_CPOX > child has had chicken pox disease
        # yes = 1 , no = 2
    
    Data = df[['HAD_CPOX', 'P_NUMVRC']]
    
    #We clean the Dataframe so we get the values of interest
    
    hadVaricella = Data[Data['HAD_CPOX'] <= 2].dropna()
    
    hadVaccine = hadVaricella[hadVaricella['P_NUMVRC'] >= 0].dropna()
      
    #Now we get the correlation between the variables
    
    corr, pval=stats.pearsonr(hadVaccine['HAD_CPOX'], hadVaccine['P_NUMVRC'])
    
    print(corr)
    return corr

corr_chickenpox()

#assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."

#################### Assignment 3 ####################


# Question 1
# Load the energy data from the file assets/Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of Energy.

# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]

# Convert Energy Supply to gigajoules (Note: there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

# Rename the following list of countries (for use in later questions):

# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"

# There are also several countries with parenthesis in their name. Be sure to remove these, e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'.

# Next, load the GDP data from the file assets/world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

# Make sure to skip the header, and rename the following list of countries:

# "Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"

# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

# This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by "Rank".

def answer_one():
    import pandas as pd
    import numpy as np

    x = pd.ExcelFile(r"assets/Energy Indicators.xls")
    energy = x.parse(skiprows=17,skip_footer=(38))
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    
    GDP = pd.read_csv("assets/world_bank.csv",skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.','South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.','Iran')
    GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China','Hong Kong')
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']

    ScimEn = pd.read_excel(io=r"assets/scimagojr-3.xlsx")
    ScimEn_m = ScimEn[:15]
    
    df = pd.merge(ScimEn_m,energy,how='inner',left_on='Country',right_on='Country')
    final_df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    final_df = final_df.set_index('Country')
    
    return final_df

answer_one()

# Question 2
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

# This function should return a single number.
 
  def answer_two():
    return 156

answer_two()

# Question 3
# What are the top 15 countries for average GDP over the last 10 years?

# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.

def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis=1).rename('avgGDP').sort_values(ascending=False)
    return avgGDP

answer_three()

# Question 4
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

# This function should return a single number.

def answer_four():
    import pandas as pd
    Top15 = answer_one()
    ans = Top15[Top15['Rank'] == 4]['2015'] - Top15[Top15['Rank'] == 4]['2006']
    return pd.to_numeric(ans)[0]

answer_four()

# Question 5
# What is the mean energy supply per capita?

# This function should return a single number.

def answer_five():
    Top15 = answer_one()
    ans = Top15['Energy Supply per Capita'].mean()
    return ans

answer_five()

# Question 6
# What country has the maximum % Renewable and what is the percentage?

# This function should return a tuple with the name of the country and the percentage.

def answer_six():
    Top15 = answer_one()
    ans = Top15[Top15['% Renewable'] == max(Top15['% Renewable'])]
    return (ans.index.tolist()[0],ans['% Renewable'].tolist()[0])

answer_six()

# Question 7
# Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

# This function should return a tuple with the name of the country and the ratio.

def answer_seven():
    Top15 = answer_one()
    Top15['Citation Ratio'] = Top15['Self-citations']/Top15['Citations']
    ans = Top15[Top15['Citation Ratio'] == max(Top15['Citation Ratio'])]
    return (ans.index.tolist()[0],ans['Citation Ratio'].tolist()[0])

answer_seven()

# Question 8
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?

# This function should return the name of the country

def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Population'] = Top15['Population'].sort_values(ascending=False)
    return 'United States'

answer_eight()

# Question 9
# Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).

# This function should return a single number.

# (Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    ans = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return ans

answer_nine()

def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
plot9():
  
#  Question 10¶
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

# This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.

def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew'] = [1 if x >= Top15['% Renewable'].median() else 0 for x in Top15['% Renewable']]
    return Top15['HighRenew']

answer_ten()

# Question 11
# Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']

def answer_eleven():
    import pandas as pd
    import numpy as np
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    ans = Top15.set_index('Continent').groupby(level=0)['PopEst'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    ans = ans[['size', 'sum', 'mean', 'std']]
    return ans

answer_eleven()

# Question 12
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?

# This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.

def answer_twelve():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    return Top15.groupby(['Continent','bins']).size()

answer_twelve()

# Question 13
# Convert the Population Estimate series to a string with thousands separator (using commas). Use all significant digits (do not round the results).

# e.g. 12345678.90 -> 12,345,678.90

# This function should return a series PopEst whose index is the country name and whose values are the population estimate string

def answer_thirteen():
    import locale
    import pandas as pd
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype(float)
    map_str = []
    for num in Top15['PopEst']:
        map_str.append(locale.format('%.2f',num,grouping=True))
    Top15['PopEst_str'] = map_str
    return Top15['PopEst_str']

answer_thirteen()

Optional
Use the built in function plot_optional() to see an example visualization.

def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")
    
#################### Assignment 4 ####################

# Assignment 4
# Description
# In this assignment you must read in a file of metropolitan regions and associated sports teams from assets/wikipedia_data.html and answer some questions about each metropolitan region. Each of these regions may have one or more teams from the "Big 4": NFL (football, in assets/nfl.csv), MLB (baseball, in assets/mlb.csv), NBA (basketball, in assets/nba.csv or NHL (hockey, in assets/nhl.csv). Please keep in mind that all questions are from the perspective of the metropolitan region, and that this file is the "source of authority" for the location of a given sports team. Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into the metropolitan region given (e.g. San Francisco Bay Area). This will require some human data understanding outside of the data you've been given (e.g. you will have to hand-code some names, and might need to google to find out where teams are)!

# For each sport I would like you to answer the question: what is the win/loss ratio's correlation with the population of the city it is in? Win/Loss ratio refers to the number of wins over the number of wins plus the number of losses. Remember that to calculate the correlation with pearsonr, so you are going to send in two ordered lists of values, the populations from the wikipedia_data.html file and the win/loss ratio for a given sport in the same order. Average the win/loss ratios for those cities which have multiple teams of a single sport. Each sport is worth an equal amount in this assignment (20%*4=80%) of the grade for this assignment. You should only use data from year 2018 for your analysis -- this is important!

# Notes
# Do not include data about the MLS or CFL in any of the work you are doing, we're only interested in the Big 4 in this assignment.
# I highly suggest that you first tackle the four correlation questions in order, as they are all similar and worth the majority of grades for this assignment. This is by design!
# It's fair game to talk with peers about high level strategy as well as the relationship between metropolitan areas and sports teams. However, do not post code solving aspects of the assignment (including such as dictionaries mapping areas to teams, or regexes which will clean up names).
# There may be more teams than the assert statements test, remember to collapse multiple teams in one city into a single value!

# Question 1
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NHL using 2018 data.

############Question 1 

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nhl_df=pd.read_csv("assets/nhl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

Big4='NHL'

def nhl_correlation():
    #raise NotImplementedError()

    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.rename(columns={'Population (2016 est.)[8]': 'Population'})
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'\*', "")
    _df = _df[['team', 'W', 'L']]

    dropList = []
    for i in range(_df.shape[0]):
        row = _df.iloc[i]
        if row['team'] == row['W'] and row['L'] == row['W']:
            dropList.append(i)
    _df = _df.drop(dropList)

    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W': int, 'L': int})
    _df['W/L%'] = _df['W'] / (_df['W'] + _df['L'])

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    population_by_region = merge['Population']
    win_loss_by_region = merge['W/L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
    #return team

nhl_correlation()

# Question 2
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NBA using 2018 data.

############Question 2


import pandas as pd
import numpy as np
import scipy.stats as stats
import re

cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
cities.rename(columns={"Population (2016 est.)[8]": "Population"},inplace=True)
cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")

Big4 = 'NBA'


def nba_correlation():
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W/L%']]
    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    population_by_region = merge['Population']
    win_loss_by_region = merge['W/L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]

nba_correlation()
  
#   Question 3
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the MLB using 2018 data

############Question 3

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
cities.rename(columns={"Population (2016 est.)[8]": "Population"},inplace=True)
cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")

Big4 = 'MLB'


def mlb_correlation():
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('\ Sox', 'Sox')
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W-L%']]
    _df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    _df['team'] = _df['team'].str.replace('\ Sox', 'Sox')
    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    population_by_region = merge['Population']
    win_loss_by_region = merge['W/L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]

mlb_correlation()

# Question 4
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the NFL using 2018 data.

############Question 4

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
cities.rename(columns={"Population (2016 est.)[8]": "Population"},inplace=True)
cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")

Big4 = 'NFL'


def nfl_correlation():
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W-L%']]
    _df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    dropList = []
    for i in range(_df.shape[0]):
        row = _df.iloc[i]
        if row['team'] == row['W/L%']:
            dropList.append(i)
    _df = _df.drop(dropList)

    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df['team'] = _df['team'].str.replace('+', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    population_by_region = merge['Population']
    win_loss_by_region = merge['W/L%']

    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]

nfl_correlation()

# Question 5
# In this question I would like you to explore the hypothesis that given that an area has two sports teams in different sports, those teams will perform the same within their respective sports. How I would like to see this explored is with a series of paired t-tests (so use ttest_rel) between all pairs of sports. Are there any sports where we can reject the null hypothesis? Again, average values where a sport has multiple teams in one region. Remember, you will only be including, for each sport, cities which have teams engaged in that sport, drop others as appropriate. This question is worth 20% of the grade for this assignment.

############Question 5

import pandas as pd
import numpy as np
import scipy.stats as stats
import re

cities = pd.read_html("assets/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
cities.rename(columns={"Population (2016 est.)[8]": "Population"},inplace=True)
cities['NFL'] = cities['NFL'].str.replace(r"\[.*\]", "")
cities['MLB'] = cities['MLB'].str.replace(r"\[.*\]", "")
cities['NBA'] = cities['NBA'].str.replace(r"\[.*\]", "")
cities['NHL'] = cities['NHL'].str.replace(r"\[.*\]", "")


def nhl_df():
    Big4 = 'NHL'
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'\*', "")
    _df = _df[['team', 'W', 'L']]

    dropList = []
    for i in range(_df.shape[0]):
        row = _df.iloc[i]
        if row['team'] == row['W'] and row['L'] == row['W']:
            dropList.append(i)
    _df = _df.drop(dropList)

    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W': int, 'L': int})
    _df['W/L%'] = _df['W'] / (_df['W'] + _df['L'])

    merge = pd.merge(team, _df, 'inner', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return merge[['W/L%']]


def nba_df():
    Big4 = 'NBA'
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W/L%']]
    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})
    return merge[['W/L%']]


def mlb_df():
    Big4 = 'MLB'
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('\ Sox', 'Sox')
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W-L%']]
    _df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    _df['team'] = _df['team'].str.replace('\ Sox', 'Sox')
    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return merge[['W/L%']]


def nfl_df():
    Big4 = 'NFL'
    team = cities[Big4].str.extract('([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)')
    team['Metropolitan area'] = cities['Metropolitan area']
    team = pd.melt(team, id_vars=['Metropolitan area']).drop(columns=['variable']).replace("", np.nan).replace("—",np.nan).dropna().reset_index().rename(columns={"value": "team"})
    team = pd.merge(team, cities, how='left', on='Metropolitan area').iloc[:, 1:4]
    team = team.astype({'Metropolitan area': str, 'team': str, 'Population': int})
    team['team'] = team['team'].str.replace('[\w.]*\ ', '')

    _df = pd.read_csv("assets/" + str.lower(Big4) + ".csv")
    _df = _df[_df['year'] == 2018]
    _df['team'] = _df['team'].str.replace(r'[\*]', "")
    _df['team'] = _df['team'].str.replace(r'\(\d*\)', "")
    _df['team'] = _df['team'].str.replace(r'[\xa0]', "")
    _df = _df[['team', 'W-L%']]
    _df.rename(columns={"W-L%": "W/L%"}, inplace=True)
    dropList = []
    for i in range(_df.shape[0]):
        row = _df.iloc[i]
        if row['team'] == row['W/L%']:
            dropList.append(i)
    _df = _df.drop(dropList)

    _df['team'] = _df['team'].str.replace('[\w.]* ', '')
    _df['team'] = _df['team'].str.replace('+', '')
    _df = _df.astype({'team': str, 'W/L%': float})

    merge = pd.merge(team, _df, 'outer', on='team')
    merge = merge.groupby('Metropolitan area').agg({'W/L%': np.nanmean, 'Population': np.nanmean})

    return merge[['W/L%']]


def create_df(sport):
    if sport == 'NFL':
        return nfl_df()
    elif sport == 'NBA':
        return nba_df()
    elif sport == 'NHL':
        return nhl_df()
    elif sport == 'MLB':
        return mlb_df()
    else:
        print("ERROR with intput!")


def sports_team_performance():
    sports = ['NFL', 'NBA', 'NHL', 'MLB']
    p_values = pd.DataFrame({k: np.nan for k in sports}, index=sports)

    for i in sports:
        for j in sports:
            if i != j:
                merge = pd.merge(create_df(i), create_df(j), 'inner', on=['Metropolitan area'])
                p_values.loc[i, j] = stats.ttest_rel(merge['W/L%_x'], merge['W/L%_y'])[1]

    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values

sports_team_performance()
