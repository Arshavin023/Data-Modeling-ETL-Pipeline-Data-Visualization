# data-modeling-ETL-Pipeline-Data-Visualization


## Architecture
![architecture](https://github.com/Arshavin023/Data-Modeling-ETL-Pipeline-Data-Visualization/assets/77532336/e9062ef6-0172-434b-9eb4-f551224f16af)


## `Scenario`
In this project, ride data of Uber csv files were provided. The data engineer was tasked with creating a data model and using the data model to build a data warehouse to be used for analytics by Data Analysts and Data Scientists

## `Tools Used`
- Lucid Platform for data modeling (lucid.app)
- Python (Pandas, Numpy, etc)
- Mage-ai ETL Platform
- Google Cloud Platform (GCP)
- Google BigQuery



## `Steps Taken:`
- The existing sample data was studied to understand the fact and dimension tables
- Lucid App was used to create a data model 
- Python scripts for data cleaning and generating dimentsion table were carefully written
- raw_data in csv files were uploaded into the Google Cloud Storage and approriate permissions were granted to allow public access
- A virtual machine was created with Google Cloud Compute, accessed through ssh and the following commands were ran
  a. sudo apt-get update && sudo apt-get upgrade -y
  b. sudo apt-get install python3-distutils
  c. sudo apt-get install python3-apt
  d. sudo apt-get install wget
  e. wget https://bootstrap.pypa.io/get-pip.py
  f. sudo python3 get-pip.py
  g. pip install pandas
  h. pip install mage-ai
- New Firewall rule was created to allow the Mage ETL platform with port "6789" access the Virtual machine
- The public IP address of the virtual machine and the Mage port i.e., PUBLIC_IP:6789 was used to access the Mage User Interface
- Mage UI was used to perform the ETL process and the ifnal facts and dimension tables were uploaded to Google BigQuery
- An Analytical query was generated and used to create a view to serve as data source for the analytics dashboard


## `Data Model:`
![Data Model](https://github.com/Arshavin023/Data-Modeling-ETL-Pipeline-Data-Visualization/assets/77532336/aa2d42fa-a52a-42e1-a74d-fdfd7a7dab68)
