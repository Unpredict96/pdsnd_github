import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    sentence1 = "Would you like to see data for Chicago, New York City or Washington"
    print(sentence1)
    
    while True:
        answer1 = input("Your answer: ")
        
        if answer1.lower() == "chicago":
            print("Data for Chicago is ready!")
            break
        elif answer1.lower() == "new york city":
            print("Data for New York City is ready!")
            break
        elif answer1.lower() == "washington":
            print("Data for Washington is ready!")
            break
        else:
            print("No data for such city")
            

    # TO DO: get user input for month (all, january, february, ... , june)
    sentence2 = "Which month would you like to see?"
    print(sentence2)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    answer2 = input("Your answer: ").lower()
    while answer2 not in months:
        answer2 = input('Month out of range')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    sentence3 = "Which day of the week you would like to see?"
    print(sentence3)
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    answer3 = input("Your answer: ").lower()
    while answer3 not in days:
            print("Day out of range")
    
    print('-'*40)
    return answer1, answer2, answer3

def load_data(answer1, answer2, answer3):
    df = pd.read_csv(CITY_DATA[answer1])
    
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    df["End Time"] = pd.to_datetime(df['End Time'])
    df['day'] = df['Start Time'].dt.weekday
    if answer3 != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(answer3) + 1
                
        df = df[df['day'] == day]
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    if answer2 != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(answer2) + 1
        
        df = df[df['month'] == month]



    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Popular_month = df['month'].mode()[0]
    print("The most popular month is ", Popular_month)

    # TO DO: display the most common day of week
    Popular_day = df['day'].mode()[0]
    print("The most popular day is ", Popular_day)

    # TO DO: display the most common start hour
    Popular_hour = df['hour'].mode()[0]
    print("The most popular hour is ", Popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_start = df['Start Station'].mode()[0]
    print("Most used Start Station is ", Popular_start)

    # TO DO: display most commonly used end station
    Popular_end = df['End Station'].mode()[0]
    print("Most used End Station is ", Popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    Popular_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most combination is ", Popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Time_takes = df["End Time"].dt.minute - df["Start Time"].dt.minute
    Total_time = Time_takes.sum()
    print("Total travel time is ", Total_time)

    # TO DO: display mean travel time
    Mean_time = Time_takes.mean()
    print("Mean travel time is ", Mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('NA')

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest is ", df['Start Time'].min())
    print("Recent is ", df['Start Time'].max())
    if 'Birth Year' in df:
        print("Most common is ", df['Birth Year'].mode()[0])
    else:
        print('NA')

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

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
       
        while view_data == 'yes':
                start_loc = 0
                print(df.iloc[start_loc : start_loc + 5])
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
