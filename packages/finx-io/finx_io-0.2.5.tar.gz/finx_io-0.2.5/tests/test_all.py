#! python
import os
import datetime

from finx.finx_rest import FinXRest


def main():
    finx_api_key = os.environ['FINX_API_KEY']
    if finx_api_key:
        finx_rest_client = FinXRest(finx_api_key)
    else:
        print("set your FINX_API_KEY environment variable like os.environ[FINX_API_KEY] = my_api_key")
    print('CONNECTED to FinXRest')
    print('TESTING GET_REFERENCE_DATA')
    reference_data = finx_rest_client.get_reference_data('BTC')
    print('GET_REFERENCE_DATA(BTC): ', reference_data)
    print('TESTING LIST_DERIBIT_CONTRACTS')
    deribit_contracts = finx_rest_client.list_deribit_contracts()
    print('LIST_DERIBIT_CONTRACTS(): ', deribit_contracts)
    print('TESTING LIST_PAIRS')
    pairs = finx_rest_client.list_pairs()
    print('LIST_PAIRS(): ', pairs)
    print("TESTING PAIR_QUOTE('BTC:USDT')")
    test_date = '9/1/2022'
    test_date_formatted = datetime.datetime.strptime(test_date, "%m/%d/%Y")
    test_date_unix = datetime.datetime.timestamp(test_date_formatted)
    print('test_date_unix:', int(test_date_unix))
    this_pair_quote = finx_rest_client.pair_quote('BTC:USDT', str(int(test_date_unix)), '30')
    print('TESTIMG PAIR_QUOTE("BTC:USDT"): ', this_pair_quote)
    # print("TESTING PAIR_QUOTE_SERIES('BTC:USDT')")
    # test_date = '9/1/2022'
    # end_date = '9/3/2022'
    # test_date_formatted = datetime.datetime.strptime(test_date, "%m/%d/%Y")
    # test_date_unix = datetime.datetime.timestamp(test_date_formatted)
    # end_date_formatted = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    # end_date_unix = datetime.datetime.timestamp(end_date_formatted)
    # this_pair_quote_series = finx_rest_client.pair_quote_series('BTC:USDT', str(int(test_date_unix)), str(int(end_date_unix)),'30')
    # print('TESTING PAIR_QUOTE_SERIES("BTC:USDT"): ', this_pair_quote_series)
    print("TESTING GET_OPTIONS_TIMESLICE('BTC')")
    test_date = '9/1/2022'
    test_date_formatted = datetime.datetime.strptime(test_date, "%m/%d/%Y")
    test_date_unix = datetime.datetime.timestamp(test_date_formatted)
    this_options_timeslice = finx_rest_client.get_options_timeslice(str(int(test_date_unix)), '30', 'BTC')
    print('TESTING GET_OPTIONS_TIMESLICE("BTC"): ', this_options_timeslice)
    print("TESTING GET_OPTIONS_TIMESLICE_SERIES('BTC')")
    test_date = '9/1/2022'
    end_date = '9/3/2022'
    test_date_formatted = datetime.datetime.strptime(test_date, "%m/%d/%Y")
    test_date_unix = datetime.datetime.timestamp(test_date_formatted)
    end_date_formatted = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    end_date_unix = datetime.datetime.timestamp(end_date_formatted)
    this_pair_quote_series = finx_rest_client.get_options_timeslice_series(str(int(test_date_unix)), str(int(end_date_unix)),'60', 'BTC')
    print('TESTING GET_OPTIONS_TIMESLICE_SERIES("BTC"): ', this_pair_quote_series)

if __name__ == '__main__':
    print('-----> FinX Test Runner ----->')
    print(' ')
    finx_api_key = input("Please enter your FinX API Key --> ")
    os.environ['FINX_API_KEY'] = finx_api_key
    main()
