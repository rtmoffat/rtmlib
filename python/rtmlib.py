class rtmlib:
    def __init__(self):
        pass
    #Return a dataframe containing a list of duplicates from a csv file
    #Returns one row for each duplicate
    #Ex:
    #   dtype = {'EVENT_NAME': str,'EVENT_TYPE': str,'DATE':str,'START_TIME':str,'SUBMITTED':str} 
    #   my_df=get_csv_duplicates("submitted_events.csv",dtype,'dup.csv')
    def get_csv_duplicates(csv_file_path:str=None,dtype:dict=None,ofile_path:str=None):
        import pandas as pd
        df=pd.read_csv(csv_file_path, dtype=dtype)
        dup=df[df.duplicated(keep=False)]
        dup.drop_duplicates(keep='first', inplace=True)
        if ofile_path:
            dup.to_csv(ofile_path, index=False)
        return dup
    #Returns a selenium brwoser object
    def initSelenium():
        from selenium import webdriver
        from selenium.webdriver import ChromeOptions

        options=ChromeOptions()
        options.add_argument("--log-level=0")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        return browser