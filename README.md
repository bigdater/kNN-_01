# kNN-_01
Title: Blood Transfusion Service Center Data Set

Abstract: Data taken from the Blood Transfusion Service Center in Hsin-Chu City 
in Taiwan -- this is a classification problem.
	

-----------------------------------------------------

Data Set Characteristics: Multivariate
Number of Instances: 748
Area: Business
Attribute Characteristics: Real
Number of Attributes: 5
Date Donated: 2008-10-03
Associated Tasks: Classification
Missing Values? N/A

-----------------------------------------------------

Data Set Information:

To demonstrate the RFMTC marketing model (a modified version of RFM), this study 
adopted the donor database of Blood Transfusion Service Center in Hsin-Chu City 
in Taiwan. The center passes their blood transfusion service bus to one 
university in Hsin-Chu City to gather blood donated about every three months. To 
build a FRMTC model, we selected 748 donors at random from the donor database. 
These 748 donor data, each one included R (Recency - months since last 
donation), F (Frequency - total number of donation), M (Monetary - total blood 
donated in c.c.), T (Time - months since first donation), and a binary variable 
representing whether he/she donated blood in March 2007 (1 stand for donating 
blood; 0 stands for not donating blood).

-----------------------------------------------------

Attribute Information:

Given is the variable name, variable type, the measurement unit and a brief description. 
The "Blood Transfusion Service Center" is a classification problem. 
The order of this listing corresponds to the order of numerals along the rows of the database.

R (Recency - months since last donation),
F (Frequency - total number of donation),
M (Monetary - total blood donated in c.c.),
T (Time - months since first donation),
and a binary variable representing whether he/she donated blood in March 2007 (1 stand for donating blood; 0 stands for not donating blood).


Variable Data Type Measurement Description min max mean std(各特征最小值、最大值、均值、标准差)
Recency quantitative Months Input 0.03 74.4 9.74 8.07
Frequency quantitative Times Input 1 50 5.51 5.84
Monetary quantitative c.c. blood Input 250 12500 1378.68 1459.83
Time quantitative Months Input 2.27 98.3 34.42 24.32
Whether he/she donated blood in March 2007 binary 1=yes 0=no Output 0 1 1 (24%) 0 (76%)
