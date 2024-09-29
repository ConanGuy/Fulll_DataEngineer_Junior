import time

import numpy as np
import pandas as pd

CITY_DATA = {
    "chicago": "data/chicago.csv",
    "new york city": "data/new_york_city.csv",
    "washington": "data/washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some bikeshare data!")
    
    def get_input(prompt: str, possible_values: list) -> str:
        """
        Get input from the user and validate it against a list of possible values.
        
        Args:
            prompt (str): The message to display to the user.
            possible_values (str): A list of possible values the user can input.
            
        Returns:
            value (str): The user's input.
        """
        while True:
            value = input(prompt).lower()

            if value in possible_values:
                break
            
            print("Invalid value. Please try again.")
        
        return value
    
    city = get_input("Choose a city to analyze: Chicago, New York City, Washington\n", CITY_DATA.keys()) # Get the city
    month = get_input("Choose a month to analyze: all, january, february, ... , june\n", ["all", "january", "february", "march", "april", "may", "june"]) # Get the month
    day = get_input("Choose a day to analyze: all, monday, tuesday, ... sunday\n", ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]) # Get the day

    print("-" * 40)
    return city, month , day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city]) # Load the data
    
    # Filter by month and day
    if month != "all":
        df = df[pd.to_datetime(df['Start Time']).dt.month_name().str.lower() == month]
    if day != "all":
        df = df[pd.to_datetime(df['Start Time']).dt.day_name().str.lower() == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    results = {}

    # TO DO: Display the most common month 
    monthsOccurences = pd.to_datetime(df['Start Time']).dt.month_name().str.lower().value_counts() # Get the occurences of each month
    maxMonth = monthsOccurences.idxmax() # Get the most common month, which is the id of the max value
    maxMonthCount = monthsOccurences.max() # Get the max value
    
    print(f"The most common month is {maxMonth} with {maxMonthCount} trips.")
    results["mostCommonMonth"] = maxMonth
    
    # TO DO: Display the most common day of week
    dayOccurences = pd.to_datetime(df['Start Time']).dt.day_name().str.lower().value_counts()
    maxDay = dayOccurences.idxmax() # Get the most common day, which is the id of the max value
    maxDayCount = dayOccurences.max() # Get the max value
    
    print(f"The most common day is {maxDay} with {maxDayCount} trips.")
    results["mostCommonDay"] = maxDay

    # TO DO: Display the most common start hour
    hourOccurences = pd.to_datetime(df['Start Time']).dt.hour.value_counts()
    maxHour = hourOccurences.idxmax() # Get the most common hour, which is the id of the max value
    maxHourCount = hourOccurences.max() # Get the max value
    
    print(f"The most common hour is {maxHour}H with {maxHourCount} trips.")
    results["mostCommonHour"] = maxHour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return results


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    results = {}

    # TO DO: Display most commonly used start station
    startStationOccurences = df['Start Station'].value_counts()  # Get the occurrences of each start station
    maxStartStation = startStationOccurences.idxmax()  # Get the most common start station, which is the id of the max value
    maxStartStationCount = startStationOccurences.max()  # Get the max value
    
    print(f"The most common start station is {maxStartStation} with {maxStartStationCount} trips.")  # Print the most common start station and its count
    results["mostCommonStartStation"] = maxStartStation  # Store the most common start station in the results dictionary

    # TO DO: Display most commonly used end station
    endStationOccurences = df['End Station'].value_counts()  # Get the occurrences of each end station
    maxEndStation = endStationOccurences.idxmax()  # Get the most common end station, which is the id of the max value
    maxEndStationCount = endStationOccurences.max()  # Get the max value
    
    print(f"The most common end station is {maxEndStation} with {maxEndStationCount} trips.")  # Print the most common end station and its count
    results["mostCommonEndStation"] = maxEndStation  # Store the most common end station in the results dictionary

    # TO DO: Display most frequent combination of start station and end station trip
    stationCombination = df['Start Station'] + " -> " + df['End Station']  # Create a combination of start and end stations
    stationCombinationOccurences = stationCombination.value_counts()  # Get the occurrences of each station combination
    maxStationCombination = stationCombinationOccurences.idxmax()  # Get the most common station combination, which is the id of the max value
    maxStationCombinationCount = stationCombinationOccurences.max()  # Get the max value
    
    print(f"The most common station combination is {maxStationCombination} with {maxStationCombinationCount} trips.")
    results["mostCommonStationCombination"] = maxStationCombination

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

    return results


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    def seconds_to_human_readable(seconds: int) -> str:
        """
        Convert seconds to a human readable format.
        
        Args:
            seconds (int): The number of seconds to convert.
            
        Returns:
            human_readable (str): The human readable format of the seconds.
        """
        
        humanReadable = ""
        
        years, seconds = seconds // 31536000, seconds % 31536000
        if years > 0: humanReadable += f"{years}Y "
        
        days, seconds = seconds // 86400, seconds % 86400
        if days > 0 or humanReadable != "": humanReadable += f"{days}D "
        
        hours, seconds = seconds // 3600, seconds % 3600
        if hours > 0 or humanReadable != "": humanReadable += f"{hours}H "
        
        minutes, seconds = seconds // 60, seconds % 60
        if minutes > 0 or humanReadable != "": humanReadable += f"{minutes}M "
        
        humanReadable += f"{seconds}S"
        
        return humanReadable

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    results = {}

    # TO DO: Display total travel time
    totalTravelTime = df['Trip Duration'].sum()  # Calculate the total travel time
    print(f"The total travel time is {seconds_to_human_readable(int(totalTravelTime))}.")  # Print the total travel time in a human-readable format
    results["totalTravelTime"] = totalTravelTime  # Store the total travel time in the results dictionary

    # TO DO: Display mean travel time
    meanTravelTime = df['Trip Duration'].mean()  # Calculate the mean travel time
    print(f"The mean travel time is {seconds_to_human_readable(int(meanTravelTime))} seconds.")  # Print the mean travel time in a human-readable format
    results["meanTravelTime"] = meanTravelTime  # Store the mean travel time in the results dictionary

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return results


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()
    
    results = {}

    # TO DO: Display counts of user types
    userTypeOccurences = df['User Type'].value_counts()  # Get the occurrences of each user type
    results["userTypeOccurences"] = {}  # Initialize the dictionary to store user type occurrences
    print("User types:")
    for userType, count in userTypeOccurences.items():  # Print the occurrences of each user type
        print(f"\tThere are {count} {userType} users.")
        results["userTypeOccurences"][userType] = count  # Store the count in the results dictionary

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:  # Check if the Gender column exists in the DataFrame
        genderOccurences = df['Gender'].value_counts()  # Get the occurrences of each gender
        results["genderOccurences"] = {}  # Initialize the dictionary to store gender occurrences
        print("User genders:")
        for gender, count in genderOccurences.items():  # Print the occurrences of each gender
            print(f"\tThere are {count} {gender} users.")
            results["genderOccurences"][gender] = count  # Store the count in the results dictionary
    else:
        print("No gender data available.")
        results["genderOccurences"] = None  # Set the value to None if the Gender column does not exist

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:  # Check if the Birth Year column exists in the DataFrame
        earliestBirthYear = int(df['Birth Year'].min())  # Get the earliest birth year
        mostRecentBirthYear = int(df['Birth Year'].max())  # Get the most recent birth year
        mostCommonBirthYear = int(df['Birth Year'].value_counts().sort_values(ascending=False).index[0])  # Get the most common birth year

        print(f"The earliest birth year is {earliestBirthYear}.")
        print(f"The most recent birth year is {mostRecentBirthYear}.")
        print(f"The most common birth year is {mostCommonBirthYear}.")

        results["earliestBirthYear"] = earliestBirthYear  # Store the earliest birth year in the results dictionary
        results["mostRecentBirthYear"] = mostRecentBirthYear  # Store the most recent birth year in the results dictionary
        results["mostCommonBirthYear"] = mostCommonBirthYear  # Store the most common birth year in the results dictionary
    else:
        print("No birth year data available.")
        results["earliestBirthYear"] = None  # Set the value to None if the Birth Year column does not exist
        results["mostRecentBirthYear"] = None  # Set the value to None if the Birth Year column does not exist
        results["mostCommonBirthYear"] = None  # Set the value to None if the Birth Year column does not exist

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

    return results

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
