
# preprocessing
import math
import random

def calulcate_percent_r(highest_high=None, lowest_low=None, close=None):
    try:
        williamPcR = (highest_high-close)/(highest_high-lowest_low)
        return williamPcR*-100
    except ZeroDivisionError:
        print(f'Highest high and lowest low cannot be same')


def calculate_mom(close_values_now = None, close_values_lookback=None):
    '''
        Inputs:
        look_back : the index of N days ago, should be a positive number
        
        day_to_check : index of the date today
    '''
    try:
        return close_values_now - close_values_lookback
    except TypeError as err:
        print(err)



def calculate_roc(close_values_now = None, close_values_lookback=None):
    '''
        Inputs:
        look_back : the index of N days ago, should be a positive number
        
        day_to_check : index of the date today
    '''
    try:
        return (close_values_now - close_values_lookback)/close_values_now
    except ZeroDivisionError as err:
        print(err)
    




