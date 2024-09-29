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

    # TO DO: Display the most common month

    # TO DO: Display the most common day of week

    # TO DO: Display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: Display most commonly used start station

    # TO DO: Display most commonly used end station

    # TO DO: Display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: Display total travel time

    # TO DO: Display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types

    # TO DO: Display counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        city, month, day = "chicago", "february", "friday"# get_filters()
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
