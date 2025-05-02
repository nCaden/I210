# import the csv module
import csv

def read_data(file_name):
    # open and read the file
    with open(file_name, 'r', encoding="utf-8-sig") as csvfile: # The file contains some funky characters - keep this encoding
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
    return data
        # Use a Dictionary Reader to read the data 
        # use a loop or list expression to create a new nested list from the data (for example, Loop over the DictReader and add each item to a list)
        # each element will be a Dictionary representing the band information from the csv file
    # return the list for use in other functions

def num_total_bands():
    # Call read_data to get the data
    # Calculate and return the total number of bands in the data set
    data = read_data("metal_bands.csv")
    return len(data)
    
def get_bands_starting_with(letter):
    # Call read_data to get the data
    # Create an return a list of the names of all bands whose name starts with the given letter
    data = read_data("metal_bands.csv")
    bands = []
    for bands in data:
       bands = [band['band_name'] for band in data if 'band_name' in band and band['band_name'].lower().startswith(letter.lower())]
    return bands


def get_bands_from_country(country):
    # Call read_data to get the data
    # Create and return a list of the names of all bands from the given country
    data = read_data("metal_bands.csv")
    bands = []
    for bands in data:
        bands = [band['band_name'] for band in data if 'origin' in band and band['origin'].lower() == country.lower()]
    return bands


def get_bands_formed_in_year(year):
    # Call read_data to get the data
    # Create and return a list of the names of all bands who formed in a given year
    data = read_data("metal_bands.csv")
    bands = []
    for bands in data:
        bands = [band['band_name'] for band in data if 'formed' in band and band['formed'] == year]
    return bands
    
def get_year_with_most_bands():
    # Call read_data to get the data
    data = read_data("metal_bands.csv")
    # Create a dictionay to tally up the number of bands formed in each year (the years will be the keys, and the number of bands will be the values)
    amount_in_year = {}
    for band in data:
        try:
            year = int(band['formed'])
            if year in amount_in_year:
                amount_in_year[year] += 1
            else:
                amount_in_year[year] = 1
        except (KeyError, ValueError):
            continue 
    #skips rows with possible missing fields, cannot remeber if this was covered in lecture or not as I was in a car accident and have not been in class but I learned this while in C200
    # Create a list from the keys and values in your tally dictionary
    sorted_years = sorted(amount_in_year.items(), key=lambda x: x[1], reverse=True)
    # Sort the list in descending order using the number of bands as the comparison (the year the most number of bands formed should be the first item in the list)
    # Return the first item in the list
    return sorted_years[0] if sorted_years else (None, 0)


# main (call your functions here)
file_name = "metal_bands.csv"
data = read_data(file_name)
print(data)
#How many bands are in the data set?
total_bands = num_total_bands()
print(f"There are {total_bands} bands in the data set.")
# Ask the user for a country
# Print out the bands from that country
country = input("Which country would you like to look up?: ")
bands_from_country = (get_bands_from_country(country))
print(bands_from_country)
# Ask the user for a letter
# Print out the bands whose names start with that letter
letter = input("Enter in a letter to see what bands start with that letter: ")
bands_that_start_with = (get_bands_starting_with(letter))
print(bands_that_start_with)
# Ask the user for a year
# Print out the bands who formed in that year
year = input("Look up bands formed in the year: ")
bands_formed_in_year = (get_bands_formed_in_year(year))
print(bands_formed_in_year)
#Print out the year that the most bands formed, as well as the number of bands that formed that year
year_with_most_bands = (get_year_with_most_bands())
year, count = year_with_most_bands 
print(f"The most formative year for metal was {year}. {count} bands formed that year")