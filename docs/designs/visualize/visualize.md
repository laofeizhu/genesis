This is to visualize the result.

# Data serialization

Data visualization has dependency on data serialization.

For simplicity, data serialization for bug world only. Data will be saved in JSON format.

There will be a metadata of the world configuration, e.g. size.

This is a to save dynamic data. At any timestamp (step), the saved info will be all the bugs and all the food.

For each bug, the saved info will be point, size, and age.

For each food, the saved info will be point and size.

The JSON file will be saved in the logs file.

# Data visualization

Use python notebook to make an interactive interface that reads the JSON file.

The interactive notebook can have the following features:
* Select log file
* Select different steps

Pandas and csv file seems more appropriate. Since JSON file seems not good for appending new data.

Final decision: bug and food status are saved to bug.csv and food.csv file.
Each row in the csv file indicates the status of one bug/food at one time instance.
