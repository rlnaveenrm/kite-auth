import nsepy as nse
import pandas as pd
import numpy as np
import sys
from nsetools import Nse
from datetime import date, timedelta
import matplotlib.pyplot as plt



def calculate_perc_matrix(data_frame, number_of_day, percentage_calc = [1,2,3,4,5,6,7,8,9,10]):
    close = np.array(data_frame['Close'])
    high = np.array(data_frame['High'])
    low = np.array(data_frame['Low'])
    open = np.array(data_frame['Open'])
    matrix_stock = np.zeros((number_of_day-1,len(percentage_calc)))
    for k in range(number_of_day-1):
        percentage =  calc_one_wait_period(close,high,k+1)
        #print(percentage)
        for i in range(len(percentage_calc)):
            if(np.sum(percentage!=-9999999)):            
                matrix_stock[k,i] = (np.sum((percentage)>=percentage_calc[i]))/np.sum(percentage!=-9999999)
            else:
                matrix_stock[k,i] = 0
    #print(matrix_stock)
    return matrix_stock


def calc_one_wait_period(close,high,wait_period):
    percentage = -9999999*np.ones((len(close)))
    try:
        for i in range(len(close)):
            percentage[i] = ((high[i+wait_period]/close[i])-1)*100 
    except IndexError:
        return percentage
    return percentage
    
def main():
    '''
    '''
    # Initiate nse connection and get stock names
    nsel = Nse()
    stock_list = nsel.get_stock_codes()
    # Get the stock list
    stock_list= {v: k for k, v in stock_list.items()}
    no_of_comapies = len(stock_list)
    iterator = iter(stock_list.items())
    break_cons = 0
    company_list = []
    company_code = []
    # start  date should be a working stock market day
    start_date_year = sys.argv[1]
    start_date_month = sys.argv[2]
    start_date_day = sys.argv[3]
    # no of days should account for the holidays in between
    no_of_days = sys.argv[4]
    start_date = date(int(start_date_year), int(start_date_month), int(start_date_day))
    end_date = start_date + timedelta(days = int(no_of_days))
    print(start_date, end_date)

    for i in iterator:
        if break_cons>=1:
            company_list.append(i[0])
            company_code.append(i[1])
        break_cons += 1
        #if break_cons==100:
        #    break
    #company_list.append('ALOKINDS')
    percentage_calc = [1,2,3,4,5,6,7,8,9,10]
    stock_data = list(company_list)
    perc_matrix = []

    for i in range(len(stock_data)):
        data_frame = nse.get_history(symbol = company_list[i], start = start_date, end = end_date)
        data_frame.drop(['VWAP','Series'], axis = 1,inplace =True)
        if i==0:
            no_of_days = len(np.array(data_frame['Close']))
            perc_matrix = np.zeros((int(no_of_days)-1,len(percentage_calc),len(stock_data)))
        perc_matrix[:,:,i] =  calculate_perc_matrix(data_frame, int(no_of_days), percentage_calc)
    plt.figure()
    plt.axes()
    plt.plot(perc_matrix[2,2,:])
    plt.xticks(range(len(company_code)), company_code, size='small', rotation='vertical')
    plt.show()


if __name__ == "__main__":
    main()



