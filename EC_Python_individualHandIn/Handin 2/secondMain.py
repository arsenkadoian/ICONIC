from secondDataHandler import *
import argparse

def main(user_country_list: list, datapoint: str):
    the_instance = secondDataHandler(user_country_list, datapoint)

    the_instance.plot_method()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="The program", description="Analysis of COVID-19 data.")
    parser.add_argument('--country1', help='A country of your choice.', required=True, type=str)
    parser.add_argument('--country2', help='A fourth country of your choice.', default="Armenia", type=str)
    parser.add_argument('--datapoint1', help='A dataset of your choice.', required=True, type=str)
    args = parser.parse_args()

    user_country_list = [args.country1.capitalize(), args.country2.capitalize()]
    argument = args.datapoint1.lower()

    main(user_country_list, argument)