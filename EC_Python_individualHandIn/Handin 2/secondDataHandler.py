import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv as cv
import sys
import joypy

class secondDataHandler():
    """[This class checks that the arguments provided by the user do not coincide. It checks that those arguments match to datapoints \
        in the dataset and later makes a plot based on if the user wants to make a separate plot for both countries or not.]"""
    
    def __init__(self, list_user_input_country: list, user_input_datapoint: str):
        """[Sets the attributes which are two lists, one for the userprovided countries and the second for the userprovided datapoints. \
            and it also calls to the different private methods which do all the nessecary work to amount to some plotting.]

        Args:
            list_user_input_country (list): [The list of country arguments provided by the user.]
            list_user_input_datapoint (list): [The datapoint argument provided by the user.]
        """
        self.list_user_input_country = list_user_input_country
        self.user_input_datapoint = user_input_datapoint
        self.__unpacks_the_index_values_and_column_titles()
        self.__checks_uniqueness_user_arguments()
        self.__checks_existence_user_arguments()

    def __unpacks_the_index_values_and_column_titles(self):
        """[This method unpacks the unique column and row titles from the dataset and puts them into a list.]"""
        self.datapoint_list = set(pd.read_csv("covid-19_vaccine_data.csv", nrows=0))
        self.country_list = np.unique(pd.read_csv("covid-19_vaccine_data.csv", usecols=['country']).values)

    def __checks_uniqueness_user_arguments(self):
        """[This method checks whether the user provided arguments coincide or not.]

        Args:
            checked_thing ([type]): [The values that is being checked.]
        """
        if len(set(self.list_user_input_country)) < len(self.list_user_input_country):
            print(f"You chose two or more countries that were the same. Please try again!")
            sys.exit()

    def __checks_existence_user_arguments(self):
        """[This method checks whether the user provided arguments match up to the ones in the dataset.]"""
        for country in self.list_user_input_country:
            if country not in self.country_list:
                print(f"{country} is not in the dataframe.")
                sys.exit()
        if  self.user_input_datapoint not in self.datapoint_list:
                print(f"{self.user_input_datapoint} is not in the dataframe.")
                sys.exit()

    def plot_method(self):
        """[Here is where all the plotting takes place.]
        """
        df = pd.read_csv("covid-19_vaccine_data.csv")
        country1 = df[df.country.isin([f'{self.list_user_input_country[0]}'])]
        country1 = country1.set_index("date").sort_index()
        prefix_c1 = f"{country1['iso_code'][0]}_"
        country1 = country1.add_prefix(prefix_c1)
        country2 = df[df.country.isin([f'{self.list_user_input_country[1]}'])]
        country2 = country2.set_index("date").sort_index()
        prefix_c2 = f"{country2['iso_code'][0]}_"
        country2 = country2.add_prefix(prefix_c2)
        combine = pd.concat([country1, country2])
        complot = combine.loc[:,[f"{prefix_c1}{self.user_input_datapoint}", f"{prefix_c2}{self.user_input_datapoint}"]]
        complot = complot.ffill()
        complot.plot()
        plt.show()