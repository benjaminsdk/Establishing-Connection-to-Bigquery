# Foodpanda_assignment

### Environment and Versions

Install Python: 3.7

Google Service Account: foodpanda@foodpanda-342717.iam.gserviceaccount.com.

### Installation Process

Run "pip install --upgrade google-cloud-bigquery" in cmd.

### Setup process

Create Google Cloud account.

Create project "Foodpanda" with a given ID "foodpanda-342717" and save the service account keyfile (JSON file) in the config file.

Run "set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH" in cmd, where "KEY_PATH" is replaced by the path where the service account keyfile is located.

### Approach

The schema and data preview was observed for geo_international_ports data prior to solving the questions.
To solve the questions, a mixture of Python and SQL was used to obtain the results.
________________________________________________________________________________________
#### Question 1:

An initial query was used to determine the longitude and latitude of "JURONG ISLAND" (The initial query can be found in Foodpanda_Q1.py in the comments).
The values obtained for the longitude and latitude of "JURONG ISLAND" was then used as the point of origin to measure the 5 other nearest port through the use of pythagorean theorem formula.

#### Output:
![image](https://user-images.githubusercontent.com/100575372/156392021-cbe63a70-5f79-41ca-b015-473ea250d77d.png)
________________________________________________________________________________________
#### Question 2:
An aggregate function COUNT was used to determine the number ports for each country whereby cargo_wharf = True.

#### Output:
![image](https://user-images.githubusercontent.com/100575372/156392272-e8543f87-aa0e-4ba0-a272-5b69ce19d421.png)
________________________________________________________________________________________
#### Question 3:
The approach for this question was to use a nested SQL query, whereby the nested code has the same approach as in Question 1 (To find the ports and their distance away from a point of origin. The point of origin for Question 3 is the location where the destress was received)
The outer query then selects the nearest port to the location of destress.

#### Output:
![image](https://user-images.githubusercontent.com/100575372/156404544-0af215d6-ffd0-4ab3-8d42-2d6c25ed056a.png)
