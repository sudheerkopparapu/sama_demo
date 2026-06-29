import pandas as pd

# Define DateTimeExtractor class
class DateTimeExtractor:
    
    def __init__(self, df, datetime_col):
        self.df = df
        self.datetime_col = datetime_col
        self._convert_to_datetime()

    def _convert_to_datetime(self):
        self.df[self.datetime_col] = pd.to_datetime(self.df[self.datetime_col])

    def set_year(self):
        self.df['Year'] = self.df[self.datetime_col].dt.year

    def set_month(self):
        self.df['Month'] = self.df[self.datetime_col].dt.month

    def set_day(self):
        self.df['Day'] = self.df[self.datetime_col].dt.day
        
    def set_hour(self):
        self.df['Hour'] = self.df[self.datetime_col].dt.hour

    def set_all(self):
        self.set_year()
        self.set_month()
        self.set_day()
        self.set_hour()    
        
#comment for commit

if __name__ == '__main__':
    pass