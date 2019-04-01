# Data-Preprocessing-Template
A simple template to process your data in an optimal form for you to use in machine learning/regression models

## Libraries Required
For this template you will need to install the following libraries using `pip install libraryName`
- Pandas
- Numpy
- sklearn
In addition the `csv` file should have the dependant varaible at the last column 

## Funtion Description
The code contains one main function namely 
>dataPreprocess(dataset,test_size,random_state,feature_scaling)

#### Return Values
  This function returns *four* outputs:
  - `X_train`: The test set of dependant values needed to train your model which is plotted on the X-axis. 
  - `y_train`: The test set of independant values needed to train your model which is plotted on the Y-axis. 
  - `X_test`: The test set of dependant values for which you shall test your model against. 
  - `y_test`: The test set of dependant values for which you shall test your model against.
  
#### Parameters
- `dataset`: This is the name of the csv file containing the dataset. Do not forget to add `.csv` with your file name.
- `test_size`: This is to decide the ratio of test data to training data you want to divide your data into. Its default value is 0.8(80%).
- `random_state`: This parameter determines how randomly the data is divided. Its default value is 0.
- `feature_scaling`: Set to **True** if you want to standardize your data range of the dependant and independant varaibles.

## Citation 
Code idea inspired from [Machine Learning A-Z™: Hands-On Python & R In Data Science](https://www.udemy.com/machinelearning/).

## Contact
For more details contact me at moonisrasheed18@gmail.com


  
