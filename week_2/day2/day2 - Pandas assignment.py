import pandas as pd
import scipy.stats as st
import os

path = os.getcwd()
print(path)

#ensure working directory is correct
os.chdir('.\\Smoothstack-Assignments\\week_2\\day2')

print(os.getcwd())

file = "resources/Salaries.csv"

original_df = pd.read_csv(file, low_memory=False)
print(original_df.head())

# get information about dataframe
print(original_df.info())

# average base pay first 10,000 rows
original_df["BasePay"] = pd.to_numeric(original_df.loc[:,"BasePay"], downcast="float", errors='coerce')

# filter to first 10000 rows of datafrome
first_10000_df = original_df.head(10000)
bp_avg = first_10000_df["BasePay"].mean()
print(f'Average base pay first 10,000 rows {bp_avg}')

# max total pay
original_df["TotalPayBenefits"] = pd.to_numeric(original_df["TotalPayBenefits"], downcast="float")

max_tb = original_df["TotalPayBenefits"].max()
print(f'Highest total pay with benefits: {max_tb}')

#Grab the data contained within the "Berry" row and the "Phone Number" column
driscoll_title = original_df.loc[(original_df["EmployeeName"] == "JOSEPH DRISCOLL"), "JobTitle"]
print("Joseph Driscoll's job title is: " + driscoll_title)

# driscoll totalpay with benefits
driscoll_tpb = original_df.loc[(original_df["EmployeeName"] == "JOSEPH DRISCOLL"), "TotalPayBenefits"]
print("Joseph Driscoll's pay with benefits is: " + str(driscoll_tpb))

# name of the person with highest pay
highest_paid = original_df.loc[original_df["TotalPayBenefits"]==(original_df["TotalPayBenefits"].max()), "EmployeeName"]
print("The person with the highest pay is: " + str(highest_paid))

# name of the person with lowest pay
lowest_pay = original_df.loc[original_df["TotalPayBenefits"]==(original_df["TotalPayBenefits"].min()), "TotalPayBenefits"]
print("The lowest pay is: " + str(lowest_pay))

lowest_paid = original_df.loc[original_df["TotalPayBenefits"]==(original_df["TotalPayBenefits"].min()), "EmployeeName"]
print("The person with the lowest pay is: " + str(lowest_paid))
#strange that the pay is negative
print("It's strange this pay is negative.")

# average total pay
avg_tp = original_df["TotalPay"].mean()
print(f'Average total pay 2011-2014: {avg_tp}')

# number of unique job titles
num_titles = original_df.JobTitle.nunique()
print(f'Number of unique job titles: {num_titles}')

#7 most common job titles
print("7 most common job titles:")
print(original_df.JobTitle.value_counts()[:7].sort_values(ascending=False))

# job titles represented by only one person
df_year = original_df.loc[(original_df['Year'] == 2013),:]

job_count = df_year.groupby('JobTitle').agg(count=('JobTitle', 'count'))

one_job_count = job_count.loc[job_count['count'] == 1].count()

print(f'Number of jobs with only 1 person in 2013: {one_job_count}')

# find people with Chief in title
print(f'Number of people with the word "Chief" in their title: {original_df.JobTitle.str.count("CHIEF").sum()}')

# The next example will compute the Pearson correlation coefficient between "length of job title string" and "salary"
job_title_len = original_df.iloc[:,2].str.len()
salary = original_df.iloc[:,7]
correlation = st.pearsonr(job_title_len,salary)
print(f"The correlation length of job title and total salary is: {round(correlation[0],2)}")



