import sys
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def second_converter(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return hours, minutes, seconds

def leave():
    """Shortcut exit from script"""
    exit()

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
         city = input('Please choose the City (chicago, new york city or washington):\n')
         city = city.lower()
         if city in CITY_DATA.keys():
                      city = city
                      break
         elif city == 'exit' or city == '0':            
            leave()
         else:
                      print('This is not a valid city. Please select one of the following cities: chicago, new york city or washington ')
                      
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
         month = input('Please choose the month (all, january, february, march, april, may, june):\n')
         month = month.lower()
         if month in months:
                      month = month
                      break
         elif month == 'exit' or month == '0':            
            leave()
         else:
                      print('This is not a valid month. Please choose e.g all, january, february, march, april, may, june\n ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         day = input('Please choose the day (all, monday, tuesday,...):\n')
         day = day.lower()
         if day in days:
                      day = day
                      break
         elif day == 'exit' or day == '0':            
            leave()
         else:
                      print('This is not a valid day. Please select e.g all, monday, tuesday,..:\n')

    print('-'*40)
    return city, month, day

# Best funktion EVER wirtten

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

# Same here. I rule! Best funktion EVER wirtten

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
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

    # TO DO: display the most common month
    most_common_month_num = df['month'].mode()[0]
    most_common_month = months_dict[most_common_month_num]
    print(f'The most common month is {most_common_month}.')
   
    # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print(f'The most common day of week is {most_common_dow}.')

    # TO DO: display the most common start hour
    most_common_start_time = pd.to_datetime(df['Start Time'].mode()[0])
    start_hour = most_common_start_time.strftime('%H') 
    print(f'The most common start hour is {start_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is: {most_common_start_station}.')

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f'The most common end station is: {most_common_end_station}.')

    # TO DO: display most frequent combination of start station and end station trip
    df['StartEnd'] = 'FROM: ' + df['Start Station'] + '  TO:  ' + df['End Station']
    most_frequent_start_end_station = df['StartEnd'].mode()[0]
    print(f'The most frequent combination of start station and end station is: {most_frequent_start_end_station}')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    hours, minutes, seconds = second_converter(total_travel_time)
    print(f'Total travel time:\n Hours: {hours}, Minutes: {minutes}, Seconds: {seconds} ')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    hours, minutes, seconds = second_converter(mean_travel_time)
    print(f'Mean travel time:\n Hours: {hours}, Minutes: {minutes}, Seconds: {seconds} ')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(f'counts of user types:\n{user_type_count}\n')
    
    # TO DO: Display counts of gender
    unknowngender = df.get('Gender')
    if unknowngender is not None:
        unknowngender = df['Gender'].fillna('unknown')
        counts_of_gender = unknowngender.value_counts()
        print(f'counts of user types:\n{counts_of_gender}\n')
    else:
          return
    
    # TO DO: Display earliest, most recent, and most common year of birth
    birth_years = df.get('Birth Year')
    if birth_years is not None:
        birth_years = df['Birth Year'].dropna()
        earliest = int(birth_years.min())
        print(f'The earliest year of birth is: {earliest}\n')
        most_recent = int(birth_years.max())
        print(f'The most recent year of birth is: {most_recent}\n')
        most_common = int(birth_years.mode()[0])     
        print(f'Themost common year of birth is: {most_common}\n')
    else:
         return

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    i = 5
    j = 0
    answer = 'yes'
    while answer.lower() != 'no':
        answer = input('Would you like to see 5 lines of raw data? (input yes or no)\n').lower()
        if answer == 'yes':
            print(df.iloc[j:i])
            j = i
            i += 5                   
        elif answer == 'no':
            return        
        else:
             print('please enter yes or no')
                          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
