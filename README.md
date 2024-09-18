# ECE 2112 Programming Assignment 3
This repository showcases a series of Python scripts aimed at solving various programming problems with a focus on data analysis using the pandas library. Each script is crafted to address specific challenges, demonstrating different techniques and functionalities of pandas.

## PROBLEM 1 

### (A) Load the corresponding .csv file into a data frame named cars using pandas

* Function/s : pd.read_csv
* Description : It loads the a CSV file with the actual path user want to load.

* EXACT CODES : PART (A)
cars = pd.read_csv('cars.csv')
cars

*OUTPUT 
- ![image](https://github.com/user-attachments/assets/5746a610-4b5a-49f0-8054-b1b7c246cde5)




### (B) Display the first five and last five rows of the resulting cars.


* Function/s : head() and tail() 
* Description : head() displays the first five rows by default and tail() displays the last five rows by default.

* EXACT CODES : PART (B)
print ( 'The first five and last five rows of the resulting cars')
print (cars.head()) # PRINT THE FIRST 5 ROWS OF THE DATA SETS 
print (cars.tail()) # PRINT THE LAST 5 ROWS OF THE DATA SETS

* Output

![image](https://github.com/user-attachments/assets/1f1012d9-4f81-4e67-bbf9-453abd2acd8c)


## PROBLEM 2 

### (A) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

* Functions/s : pd.read_csv() and  
* Description : The pd.read_csv() function loads the CSV file into a DataFrame, allowing for data manipulation and analysis. Then,The iloc function is utilized for integer-location-based indexing; in this context, cars.iloc[:5, ::2] selects the first five rows and every second column,

* EXACT CODES : PART (A)
cars = pd.read_csv('cars.csv') # Load my data set        
print("First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])  # Using iloc to select specific rows and columns 
                           # :5 value will show the first 5 rows in the data set 
                           # ::2 which will slice the dataset in columns 


* OUTPUT :

![image](https://github.com/user-attachments/assets/dff82d1a-e7f5-4baf-ad67-d9706ab6029a)

### (B) Display the row that contains the ‘Model’ of ‘Mazda RX4’

* Functions/s : pd.read_csv(), loc
* Description : After loading the dataset with pd.read_csv(), the loc function is employed to filter the DataFrame based on the condition cars['Model'] == 'Mazda RX4'

* EXACT CODES :  PART (B)

cars = pd.read_csv('cars.csv') # Load my data set 
cars.loc[[1],['Model','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']]   # Using slicing to get a portion Row 1 of my data set 
                                                                                                 

* OUTPUT :

![image](https://github.com/user-attachments/assets/73d8348c-ea57-4c52-b340-2e60497e8b89)


### (C) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

Functions/s : pd.read_csv(), loc
Description : The pd.read_csv() function loads the CSV file, and then loc is used to filter the DataFrame to the row where the 'Model' is 'Camaro Z28'. Accessing the 'cyl' column.

* EXACT CODES :  PART (C)
cars = pd.read_csv('cars.csv') # Load my data set 
cars.loc[[1],['Model','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']]   # Using slicing to get a portion Row 1 of my data set 


* OUTPUT

![image](https://github.com/user-attachments/assets/1a392193-1cbe-4188-b4e3-df24e1bca7d2)


### (D) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

Functions/s : pd.read_csv(), loc
Description : The pd.read_csv() function loads the CSV file into the DataFrame, making the data accessible for manipulation. The loc function is then used to apply a condition that filters the dataset for the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'. 
After filtering, the function retrieves the 'cyl' (cylinders) and 'gear' type for these models, giving a concise result of the requested information.

* EXACT CODES : PART (D) 
cars = pd.read_csv('cars.csv') # Load my data set 
selected_models = cars[ # Storing Values for proper output 

(cars['Model'] == 'Mazda RX4 Wag') |  (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic') ][['Model', 'cyl', 'gear']]  # Assigning and checking car model to slice the data ----- # extract only the 'Model', 'cylinders' (cyl), and 'gear' from model 
print(selected_models) # Print the result

* OUTPUT

![image](https://github.com/user-attachments/assets/4ade990d-5cd3-47a9-a680-4f1052723cc1)


### AUTHOR 
## DE GUZMAN , JAN DENVER F. 

### REFERENCES
## ECE2112 Lecture Notes by Prof. Engr. Ma. Madecheen S. Pangaliman, MSc, and Prof. Engr. Nico John Leo S. Lobos.

