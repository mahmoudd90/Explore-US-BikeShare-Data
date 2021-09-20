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
    city = input('please select the city you want to explore (chicago, new york city, washington):   ').lower()
    city_group= ['chicago', 'new york city', 'washington']
    while True:
        if city not in city_group:
            city = input('please choose a correct city name from list (chicago, new york city, washington): ').lower()
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please select the month you want to explore (january, february, march, april, may, june) or type all for all months : ').lower()

    month_group = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    
    if month not in month_group:
             month = input('please select a correct month to explore (january, february, march, april, may, june) or type all for all months : ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('please select the day you want to explore (saturday, sunday, monday, tuesday, wednesday, thurusday, friday) or type all for all days : ').lower()
    day_group = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thurusday', 'friday', 'all']

    while day in day_group:
        break
    else:
         day = input('please select the correct day of the week to explore or type all for all days : ').lower()

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
    #filter by city name
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    
    if month != 'all' :   
        month_of_interest= month_dict[month]   
        df = df[df['month'] == month_of_interest]
    else:
        df=df
  
    # filter by day of week if applicable
    if day != 'all' :
        df = df[df['day_of_week'] == day.title()]
    else:
        df=df
    
    return df
    
def raw_data(df):
    """ Give the user the ability to show raw data. """
    request=input('Do you want to view the first 5 rows of your selected raw data? Yes or No : '.lower())
    ind= 0
    list=['yes', 'no']
    if request not in list:
        request=input('please specify a correct answer! Do you want to view the first 5 rows of your selected raw data? Yes or No : '.lower())
        while request == 'yes' :
                print(df.iloc[ind: ind+5, :])
                request=input('Do you want to view the next 5 rows of your selected raw data? Yes or No : '.lower())
                if request =='yes':
                    ind = ind+5
                else:
                     break    
    else:
        while request == 'yes' :
            print(df.iloc[ind: ind+5, :])
            request=input('Do you want to view the next 5 rows of your selected raw data? Yes or No : '.lower())
            if request =='yes':
                ind = ind+5
            else:
                 break

        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   
    month_names = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    common_month_name = month_names[common_month - 1]
    print ('The Most Common Month is ' + str(common_month_name))
    
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The Most Common Day is ' + str (common_day))
    
    # TO DO: display the most common start hour
    df['Start_hour']= df['Start Time'].dt.hour
    common_hour = df['Start_hour'].mode()[0]
    print('The Most Common start hour is : ' + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station_start = df['Start Station'].mode()[0]
    print('The Most Common Start Station is ' + str(common_station_start)+'.')

    # TO DO: display most commonly used end station
    common_station_end = df['End Station'].mode()[0]
    print('The Most Common End Station is {}.'.format(common_station_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Stations Combination'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['Stations Combination'].mode()[0]
    print('The Most Common Start - End Stations combination is ' + str(common_combination) +'.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_hrs = total_travel_time / 3600
    total_travel_time_days = total_travel_time_hrs / 24
    print('The Total Travel time is {:0.2f} Hrs / {:0.2f} Days.'.format(total_travel_time_hrs, total_travel_time_days))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time is {:0.2f} Hrs / {:0.2f} Days.'.format(average_travel_time/ 3600, average_travel_time / 3600 /24))
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types : \n' , user_type_counts)
    
    # TO DO: Display counts of gender
    
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts(dropna= True)
        print('\nCounts for gender: \n', gender_count)
    else:
        print('\nNo gender data available to calculate gender counts!')
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest= df['Birth Year'].min()
        recent= df['Birth Year'].max()
        common= df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth is {:.0f}, The most recent year of birth is {:.0f}, The most common year of birth is {:.0f}.'.format(earliest, recent, common))
    else:
        print('\nNo Birth Year data available!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
