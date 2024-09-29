# Code documentation

In this project, I've completed a few functions to analyze data related to bike share systems. I will explain what I have done and why I made those choices.

# Table of content

1. [Function 1: Get filters](#function-1-get-filters)
2. [Function 2: Load data](#function-2-load-data)
3. [Function 3: Time Statistics](#function-3-time-statistics)
4. [Function 4: Station Statistics](#function-4-station-statistics)
5. [Function 5: Trip duration Statistics](#function-5-trip-duration-statistics)
6. [Function 6: User Statistics](#function-6-user-statistics)
7. [Tests](#tests)

# Function 1: Get filters

## The subfunction `get_input`:

As I have to do the same work three times, I have decided to create a subfunction that I will use multiple times inside the get_filters function.

This function takes 2 parameters:
- `prompt`: The message to display to the user
- `possible_values`: A list of possible values the user can input

The prompt will ask the user to send an input, and the given possible values will allow the script to run again if the user didn't send an allowed value. This way, I am ensuring that the user will not create bugs by sending incoherent values.

## Getting the inputs

Then I simply ask the user for the city, the month, and the day they want to focus on, and return those values.

# Function 2: Load data

## Read the file:

I used the function `pandas.read_csv` provided by Pandas to open the selected file.

## Filter month and day:

I began by checking if the month/day selected by the user was not `all`, which would not require any filtering.

Then I converted the column `Start Time` into datetime. Finally, I filtered the series by month/day name.

# Function 3: Time Statistics

For the three different values, I did pretty much the same thing.

I started by converting the column `Start Time` into datetime, and then counted every occurrence of the month/day/hour with the function `pandas.Series.value_counts`. Finally, I used `pandas.Series.idxmax` to get the index of the highest value in the series.

# Function 4: Station Statistics

In this function I did pretty much the same thing than the previous one. 

The particularity was that I needed the create a series containing values for both start and end station. I simply concatenated the two column to create it and then looked for the most common trip.

# Function 5: Trip duration Statistics

In this function I simply used the functions `pandas.Series.sum` and `pandas.Series.mean` to get the two values I needed.

# Function 6: User Statistics

In this function, for the user types and the genders, I got the amount of occurences for every values with `pandas.Series.value_counts` and iterate through the series to store every counts into the result dictionary.

For the year of birth elements, I had to use `pandas.Series.min` and `pandas.Series.min` for the earliest and latest values.
For the most common year of birth, I decided to sort the amount of occurences for each year descending with `pandas.Series.sort_values`, and to take the first element with `pandas.Series.index`. 