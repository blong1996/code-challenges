"""
    File:        wedding_seating.py
    Author:      Brandon Long
    Description: This file contains the core logic of the wedding seating app
"""

from models.models import Venue, Party, Table


def seat_parties(venue: Venue):
    return True


def main():

    # prompt user for name of venue and init venue
    venue_name = input("Enter a name for your venue: ")
    venue = Venue(venue_name)

    # loop until table entry is valid
    # prompt user for tables in letter-size format
    # validate tables

    # add tables to venue

    # loop until user is finished entering parties
    # enter party as name-size ! party name, party name, ...
    # validate party input
    # validate venue space for party
    # add party to venue list

    # attempt to seat parties
    if seat_parties(venue):
        print(venue)
    else:
        print("Unable to sit this party!")


if __name__ == "__main__":
    main()
