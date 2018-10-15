"""
    File:        wedding_seating.py
    Author:      Brandon Long
    Description: This file contains the core logic of the wedding seating app
"""
import time
from models.models import Venue, Party, Table


def validate_table_input(tables_string):
    tables = []
    table_pairs = tables_string.split(" ")
    for pair in table_pairs:
        t = pair.split("-")
        name = t[0]
        seats = int(t[1])

        # validate number of seats
        if seats < 1:
            print('Invalid number of seats provided for table {}'.format(name))
            return tables, False

        # check if table name already exists
        if any(t.name == name for t in tables):
            print('Duplicate table entered: {}'.format(name))
            return tables, False

        # create table object
        table = Table(name, seats)
        tables.append(table)
    return tables, True


def validate_party(party_string):
    party_details = party_string
    dislikes = []

    # check for dislikes
    if "!" in party_string:
        party_string_pair = party_string.split(" ! ")
        party_details = party_string_pair[0]
        dislikes_string = party_string_pair[1]
        dislikes = dislikes_string.split(" ")

    # parse name and size
    party_pair = party_details.split("-")
    name = party_pair[0]
    size = int(party_pair[1])

    if size < 1:
        print('Invalid party size for party {}!'.format(name))
        return None, False

    # create party object
    party = Party(name, size, dislikes)

    return party, True


def main():
    # prompt user for name of venue and init venue
    venue_name = input("Enter a name for your venue: ")
    venue = Venue(venue_name)
    valid_tables = False

    # loop until table entry is invalid
    while not valid_tables:

        # prompt user for tables in name-size format
        tables_string = input("Enter venue tables in single line separated by spaces (Ex: 'table_name'-'capacity')\n"
                              "Ensure table name has no spaces and capacity is a valid integer greater than 0:\n\n")

        # validate tables
        try:
            tables, valid = validate_table_input(tables_string)

            if not valid:
                continue

            # add tables to venue
            venue.tables = tables
            valid_tables = True

        except Exception:
            print("Error: Invalid Input!")

    party_string = ""

    # loop until user is finished entering parties
    while party_string is not "done":

        # enter party as name-size ! party name, party name, ...
        party_string = input("Enter parties (one per line) in the format 'party-name'-'party-size'. If a party does\n"
                             "not like another party(ies), it should be in the following format:\n\n"
                             "\t'party-name'-'party-size' ! 'party-name' 'party-name' 'party-name' ...\n\n"
                             "Note: Party names must not have spaces in them and 'party-size' must be "
                             "greater than 0:\n\n")

        # check if input is finished
        if party_string == "done":
            break

        # validate party input
        try:
            party, valid = validate_party(party_string)

            if not valid:
                continue

            # validate venue space for party
            if not venue.has_enough_space(party):
                print("Venue does not have enough space for a party this size. Spots left: {}/{}\n"
                      .format(venue.space_left(), venue.total_capacity()))
                continue

            # check for duplicate party names
            if venue.party_exists(party):
                print('Duplicate party entered: {}\n'.format(party.name))
                continue

            # add party to venue list
            venue.add_party(party)
            print("The following party has been added:\n\n\t{}\n".format(party))

        except Exception:
            print("Error: Invalid Input!")

    # track runtime
    start = time.time()

    # attempt to seat parties
    if venue.seat_parties():
        print(venue)
    else:
        print("Unable to sit these parties!")

    print("\n--- Finished in %s seconds ---" % (time.time() - start))


if __name__ == "__main__":
    main()
