# MONGO INVENTORY

## An inventory database management system designed for grocery stores like Wal-Mart
This project is meant to simulate an inventory database management for real-time

## Technologies Used

* Pymongo - version 4.1.1
* MongoDB Compass - version 1.32.2
* Python - version 3.10

## Features

List of features ready and TODOs for future development
* Sanitized user inputs to reduce errors and improve database security
* Utilized unique indices to simulate the one-to-one relation of SKU numbers to consumer goods
* Allows users to perform CRUD operations on inventory databases through an easy-to-use command line menu

To-do list:
* Integrate machine learning algorithms to find the ideal stock level and alert management when they need to place an order
* Integrate with bar code scanners to allow real-time displays of inventory vs cyclical estimates
* Fully integrate cloud HDFS infrastructure to truly harness the power of the Spark ecosystem

## Getting Started
   
gh repo clone jmyeary/Revature-Project-0-Inventory

> Project utilizes MongoDB so it will only work with that technology. Not compatible with SQL or other RDBs.

* Ensure the following variables are adjusted for your particular database:

cluster = MongoClient("YOUR SERVER IP")
db = cluster["YOUR CLUSTER NAME"]


collection1 = db["YOUR COLLECTION1"] #on-hand inventory

collection2 = db["YOUR COLLECTION2"] #master inventory

collection3 = db["YOUR COLLECTION3"] #inventory on-order

## Usage

> Simply run the project file on your machine, and follow the easy to understand prompts..



## License

This project uses the following license: [GPL-3.0](<https://opensource.org/licenses/GPL-3.0>).
