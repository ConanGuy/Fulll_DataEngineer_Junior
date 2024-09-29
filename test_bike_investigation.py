import unittest
import pandas as pd
from bike_investigation import time_stats, station_stats, trip_duration_stats, user_stats

class TestBikeShareData(unittest.TestCase):

    def test_time_stats(self):
        data = {
            'Start Time': ['2017-01-01 09:07:57', '2017-01-02 09:07:57', '2017-01-03 00:07:57'],
            'End Time': ['2017-01-01 09:20:53', '2017-01-02 09:20:53', '2017-01-03 00:20:53'],     
        }

        # TO DO : create a panda DataFrame from the data dictionary
        df = pd.DataFrame(data)

        result = time_stats(df)

        self.assertIn(result['mostCommonMonth'], ['january', 'february', 'march'])
        # TO DO : add more tests for the other keys in the result dictionary
        self.assertIn(result['mostCommonDay'], ['sunday', 'monday', 'tuesday'])
        self.assertEqual(result['mostCommonHour'], 9)

    def test_time_stats_missing_data(self):
    # TO DO : base on the above test, create tests for station_stats, trip_duration_stats and user_stats function. Make sure you cover common corner cases.  
        data = {
            'Start Time': ['2017-01-01 09:07:57', '2017-01-02 09:07:57', '2017-01-03 00:07:57'],
            'End Time': ['2017-01-01 09:20:53', '2017-01-02 09:21:53', '2017-01-03 00:26:53'],
            'Start Station': ['A', 'A', 'B'],
            'End Station': ['B', 'B', 'C'],  
            'Trip Duration': [13, 13, 19],
            'User Type': ['Subscriber', 'Customer', 'Subscriber'],
            'Birth Year': [1990, 1991, 1991]
        }

        df = pd.DataFrame(data)

        station_result = station_stats(df)
        self.assertEqual(station_result['mostCommonStartStation'], 'A')
        self.assertEqual(station_result['mostCommonEndStation'], 'B')
        self.assertEqual(station_result['mostCommonStationCombination'], ('A -> B'))
        
        trip_duration_result = trip_duration_stats(df)
        self.assertEqual(trip_duration_result['totalTravelTime'], 45)
        self.assertEqual(trip_duration_result['meanTravelTime'], 15)
        
        user_result = user_stats(df)
        self.assertEqual(user_result['userTypeOccurences']['Subscriber'], 2)
        self.assertEqual(user_result['userTypeOccurences']['Customer'], 1)
        self.assertEqual(user_result['genderOccurences'], None)
        self.assertEqual(user_result['earliestBirthYear'], 1990)
        self.assertEqual(user_result['mostRecentBirthYear'], 1991)
        self.assertEqual(user_result['mostCommonBirthYear'], 1991)
    
if __name__ == '__main__':
    unittest.main()