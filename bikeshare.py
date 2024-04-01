import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
weekday_data = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    while True:
        try:
            city = input("Enter which city (chicago, new york city or washington) to analyse: ").lower()
        
            if city in ("chicago", "new york city", "washington"):
                break # Break out of the loop
            else:
                print("Invalid input. Please enter chicago or new york or washington")
        except ValueError:
            print("Invalid input. Please try again!")          
    # next we go chapter to month
    # get user input for month (all, january, february, ... , june)
                     
    while True:
        try:
            month = input("Enter name of the month (E.g all, january, february, till june): ").lower()     
        
            if month in month_data:
                break # Break out of the loop
            else:
             print("Invalid input. Please enter correct month")
        except ValueError:
            print("Invalid input. Please try again!")     

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter name of the day of week (E.g monday, tuesday ... or all): ").lower()     
        
            if day in weekday_data:
                break # Break out of the loop
            else:
                print("Invalid input. Please enter name of the day of week again.")
        except ValueError:
            print("Invalid input. Please try again!")     

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_data.index(month) 
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    # find the most common month 
    common_month = df['month'].mode()[0]
    print("The most common month to travel is : " + month_data[common_month-1].title())

    # find the most common day of week 
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day)
    
    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)
    
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    #display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + 'to ' + df['Start Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is: " + common_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_travel_time))

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of the user types: " + str(user_types))
    #Display counts of gender
    if  city in ("new york city", "chicago"):
            gender = df['Gender'].value_counts()
            print("The count of the gender: " + str(gender))
      
    #Display earliest, most recent, and most common year of birth
            earliest_birth = df['Birth Year'].min()
            recent_birth = df['Birth Year'].max()
            common_birth = df['Birth Year'].min()
            print('Earliest birth is: {}\n'.format(earliest_birth))
            print('Most recent birth is: {}\n'.format(recent_birth))
            print('Most common birth is: {}\n'.format(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    y = 0
    # Display 5 rows of raw data. 
    while True:
        view_data = input('\nWould you like to display raw data? Enter yes or no.\n')
        if view_data.lower() == 'yes':
            five_rows = df.iloc[y:y+5]
            y += 5
            print(five_rows)
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
