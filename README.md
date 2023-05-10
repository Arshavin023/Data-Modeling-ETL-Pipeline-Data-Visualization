# data-modeling-ETL-Pipeline-Data-Visualization

## `Scenario`
In this project, ride data of Uber csv files were provided. The data engineer was tasked with creating a data model clearly displaying the facts and dimension tables and building an ETL data pipeline.

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

[IBM_Cognos_Dashboard](https://dataplatform.cloud.ibm.com/dashboards/a2f9bd1d-9a21-49b3-b651-b4b1892ee154/view/641ecb6463b411c241e5c4e407ca7800783f775bb1bb870ad3d07b495a687497f33a1194c82a4c0cdd195665f5be410b9a)

![softcartRelationships](https://user-images.githubusercontent.com/77532336/218350662-231a0727-c0b9-42db-a5e2-a3d13a0de7b1.jpg)
