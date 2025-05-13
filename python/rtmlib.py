class rtmlib:
    def __init__(self):
        pass
    #Return a dataframe containing a list of duplicates from a csv file
    #Returns one row for each duplicate
    #Ex:
    #   dtype = {'EVENT_NAME': str,'EVENT_TYPE': str,'DATE':str,'START_TIME':str,'SUBMITTED':str} 
    #   my_df=get_csv_duplicates("submitted_events.csv",dtype,'dup.csv')
    def get_csv_duplicates(self,csv_file_path:str=None,dtype:dict=None,ofile_path:str=None):
        import pandas as pd
        df=pd.read_csv(csv_file_path, dtype=dtype)
        dup=df[df.duplicated(keep=False)]
        dup.drop_duplicates(keep='first', inplace=True)
        if ofile_path:
            dup.to_csv(ofile_path, index=False)
        return dup
    #Returns a selenium brwoser object
    def initSelenium(self):
        from selenium import webdriver
        from selenium.webdriver import ChromeOptions

        options=ChromeOptions()
        options.add_argument("--log-level=0")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        return browser
    #
    #Init tkinter, Python's native GUI library
    def initTk(self):
        import tkinter as tk
        from tkinter import ttk
        root=tk.Tk()
        button=ttk.Button(master=root,text="click me")
        button.pack()
        root.state("zoomed")
        root.mainloop()
    #Init the usb library and list all devices
    def usbcom(self):
        import usb.util

        # Find all connected USB devices
        devices = usb.core.find(find_all=True)

        if devices is None:
            raise ValueError('Device not found')

        # Iterate through each device and print information
        for device in devices:
            print(f"Device: {device}")
            print(f"  Vendor ID: {hex(device.idVendor)}")
            print(f"  Product ID: {hex(device.idProduct)}")
            try:
                print(f"  Manufacturer: {usb.util.get_string(device, device.iManufacturer)}")
                print(f"  Product: {usb.util.get_string(device, device.iProduct)}")
            except Exception as e:
                print(f"  String descriptors not available: {e}")

    #Detect outliers
    def detect_outliers(self):
        import pandas as pd
        import seaborn as sns
        from pyod.models.mad import MAD
        from pyod.models.iforest import IForest

        # Load a sample dataset
        diamonds = sns.load_dataset("diamonds")
        # Extract the feature we want
        X = diamonds[["price"]]

        # Initialize and fit a model
        forest=IForest().fit(X)
        #mad = MAD().fit(X)

        # Extract the outlier labels
        labels = forest.labels_
        print(pd.Series(labels).value_counts())
lib=rtmlib()
lib.detect_outliers()