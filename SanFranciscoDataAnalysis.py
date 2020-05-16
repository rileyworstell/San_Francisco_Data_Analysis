import numpy as np
import pandas as pd

sal = pd.read_csv('Salaries.csv')
print(sal)

#Check head of DataFrame # First Two Rows
# print(sal.head(2))

#Use .info() method to find out how many entries there are
# print(sal.info())

#What is the average Base Pay of San Francisco City Employees
# print(sal["BasePay"].mean())

#What is the highest amount of overtimepay in the dataset
# print(sal["OvertimePay"].max())

# What is the job title of Joseph Driscoll?
# print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]) 

#How much does Joseph Driscoll make (including Benefits)
# print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])

# Name of the highest Paid person
# print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]["EmployeeName"])

# Name of lowest paid person
# print(sal.iloc[sal["TotalPayBenefits"].argmin()])

# What is the average Base Pay of all employees per year? (2011 - 2014)
# print(sal.groupby("Year").mean()["BasePay"])


# How many unique job titles are there
# print(sal["JobTitle"].nunique())

# What are the top 5 common jobs?
# print(sal["JobTitle"].value_counts().head(5))

# How many job Titles were represented by only one person in 2013?
# print(sum(sal[sal["Year"] == 2013]["JobTitle"].value_counts()) == 1) 



