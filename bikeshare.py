import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Submit any name of these cities: chicago, new york or washington\n')
    while(city not in ['chicago', 'new york', 'washington']):
        city = input('Submit any name of these cities: chicago, new york or washington\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january','february','march','april','may','june']
    month = input('Submit month name (all, january, february, ... , june)\n')
    while(month not in months):
        month = input('Submit month name (all, january, february, ... , june)\n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'saturday', 'sunday','monday','tuesday','wednesday','thursday','friday']
    day = input('Submit day name (all, saturday, sunday, ..., friday)\n')
    while(day not in days):
        day = input('Submit day name (all, saturday, sunday, ..., friday)\n')


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
    CITY_DATA = {
    'chicago':'chicago.csv',
        'new york': 'new_york_city.csv',
        'washington':'washington.csv'
    }
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month:',df.month.mode()[0])

    # TO DO: display the most common day of week
    print('Most common day of week:',df.day_of_week.mode()[0])

    # TO DO: display the most common start hour
    print('Most common start hour:',df.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station:',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most common end station:',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most common combination of start and end station\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Avergae travel time:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types\n', df['User Type'].value_counts())
    print('\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender\n', df['Gender'].value_counts())
    else:
         print('No available data for gender')
    print('\n')        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
         print('Earliest year of birth:', df['Birth Year'].min())
         print('Most recent year of birth:', df['Birth Year'].max())
         print('Most common year of birth:', df['Birth Year'].mode()[0])
    else:
         print('No available data for birth year')
    print('\n')
    
    print('First 5 rows of data: ')
    show_next = 'yes'
    counter = 5
    while(show_next in ['yes','y']):
        print(df.iloc[counter - 5:counter].stack())
        show_next = input('Would you like to show the next 5 rows of data? yes or no\n')
        print('\n')
        counter += 5
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
