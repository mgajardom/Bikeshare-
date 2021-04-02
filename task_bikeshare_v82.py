chiimport time
import pandas as pd

def get_filters():
    
   #  Asking to suser to specify a city, month, and day to analyze.

    print(''*3)
    print('-'*50)
    print('\nHello! Let\'s explore some US bikeshare data!')

    while True:
        print('\n')
        print('chicago ', 'new_york ', 'washigton')
        city = input("Please type the three first letter of the city: ").lower()
        if city not in ('chi', 'new', 'was', 'Chi', 'New', 'Was'):
            print("Not an appropriate choice,  try again please.")
        else:
            break

#------------------ ebd city subroutine-------------------#

    while True:
        print('\n')
        print('jan ', 'feb ', 'mar', 'apr', 'may', '...')
        month = input("Please type the three first letter of the MONTH ").lower()
        if month not in ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'):
            print("Not an appropriate choice,  try again please.")
        else:
            mon= {'jan': 'January', 'feb':'February', 'mar':'March', 'apr':'April', 'may':'May', 'jun':'June', 'jul':'July', 'aug':'August',
                  'sep':'September', 'oct':'October', 'nov':'November', 'dec':'December'}
            month = (mon.get(month))
            break
        
# -----------------  end month subroutine -----------------#

    while True:
        print('\n')
        print('The days of the week available to select are:')
        print('mon ', 'tue ', 'wed', 'thu', 'fri', 'sat', 'sun')
        day = input("Please type the three first letter of the DAY: ").lower()
        if day not in ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'):
            print("Not an appropriate choice,  try again please.")
        else:
            dai= {'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday', 'thu':'Thursday', 'fri':'Friday', 'sat':'Saturday', 'sun':'Sunday', 'all':''}
            day = (dai.get(day))
            break
        
#------------------  end day subroutine  ------------

    return city, month, day

# loading datafile and clean
def load_data(city, month, day):
    
    if city.lower() == 'chi':
         df = pd.read_csv('chicago.csv')
         df = df.dropna(subset=["Gender", "Birth Year"])
    if city.lower() =='new':
         df = pd.read_csv('new_york_city.csv')
         df = df.dropna(subset=["Gender", "Birth Year"])
    if city.lower() =='was':
         df = pd.read_csv('washington.csv')
         df = df.dropna()

        
#  This is the most imoortant section of this program
#  ==================================================
    df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S')   
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    
       
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
        
    df['Time'] = df['Start Time'].dt.time
    dg=df[(df['Day']==day)&(df['Month']==month)]
       
    return dg
    
def time_stats(df):
    # statistics on the most frequent times of travel.
    print('-'*60)
    print('-'*60)
    print('\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  
    mon_mode = df['Month'].mode()
    print('The most common month : '+mon_mode)

    # displaying most common day
    most_day = df['Day'].mode()
    print('The most common day  : '+most_day)
    
    # diplaying hour
    most_hour = df.groupby('Time').count().index.max()
    print('The most common hour  : '+str(most_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is : {}'.format(start_station))
    
    end_station = df['End Station'].mode()[0]

    print('\nThe most commonly used end station is : {} '.format(end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    # Statistics on the total and average trip duration

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    duration = df['Trip Duration'].sum()
    duration = duration/60
    print('The duration is: {} horas'.format(duration))
    time.sleep(5)
    
    duration = round(df['Trip Duration'].mean())
    duration = duration/60
    
    print('\nThe average trip duration is {} hours'.format(duration))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    #Statistics on bikeshare users

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # counts of user types
    user_type=str(df.groupby('User Type').size())
    print('The counts of user types : {}'.format(user_type))

    # counts of gender
    if 'Gender' in df.columns:
       user_gend=str(df.groupby('Gender').size())
       print('The counts of user gender : {}'.format(user_gend))
    else:
        print('Count of Gender  :    Without registers')

    # Earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest = str(df['Birth Year'].min())
        recent = str(df['Birth Year'].max())
        frecue = str(df.groupby('Birth Year').count().index.max())
        print('\nThe oldest year of birth is '+oldest)
        print('\nThe most recent year of Birth is '+(recent))
        print('\nThe most common year of birth is '+(frecue))
    else:
        print('Earliest, most recent and common year of birth:  Without registers')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    # Asking to user if he wants more details
    answers = ['y', 'n']
    while answers not in answers:
        print("\n")
        print("Do you want display more data?  'y' or 'n'")
        more_data = input().lower()
        
        if more_data == "y":
            print(df.head(10))
        else:
            break
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' :
                break

if __name__ == "__main__":
	main()
