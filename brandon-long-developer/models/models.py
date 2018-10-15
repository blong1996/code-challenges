"""
    File:        models.py
    Author:      Brandon Long
    Description: This file contains the classes necessary for the core
                 logic
"""


class Party(object):
    """
    Class to represent a party
    """

    def __init__(self, name, size, dislikes):
        """
        Initialize party object
        :param name: Name of party (uid)
        :param size:
        """
        self.name = name
        self.size = size
        self.dislikes = dislikes
        self.seated = False

    def __str__(self):
        """
        Create string representation of party

        :return:
        """
        dislike_string = ""
        if len(self.dislikes) > 0:
            dislike_string = "; Dislikes: {}".format(", ".join(self.dislikes))
        return "{}, party of {}{}".format(self.name, self.size, dislike_string)

    def add_dislike(self, party_name):
        """
        Add a party to this party's list of dislikes

        :param party_name: party_name to add
        :return:
        """
        self.dislikes.append(party_name)

    def has_dislikes(self):
        """
        Check if this party has dislikes
        :return:
        """
        return len(self.dislikes) > 0


class Table(object):
    """
    Class to represent a table at the venue
    """

    def __init__(self, name: str, seats: int):
        """
        Initialize table object

        :param name: Represents table name
        :param seats: Represents number of seats at table
        """
        self.name = name
        self.seats = seats
        self.open_seats = seats
        self.parties = []

    def __str__(self):
        """
        Create string representation of table

        :return:
        """
        return "Table {} - {}/{} Seats Open:\n\t{}" \
            .format(self.name, self.open_seats, self.seats, "\n\t".join([str(p) for p in self.parties]))

    def is_seated(self, party_name):
        """
        Check if a party is seated at this table

        :param party_name: party to check for

        :return: true if party is seated here, false if not
        """
        return any(p.name == party_name for p in self.parties)

    def space_available(self, party: Party):
        """
        Check if this table has space for this party

        :param party: party to be seated
        :return: true if space, false if not enough
        """
        return self.open_seats >= party.size

    def dislikes_seated(self, party: Party):
        """
        Check if any disliked parties are seated at this table

        :param party: party to check for
        :return: true if there are disliked parties seated, false if not
        """
        return any(self.is_seated(p) for p in party.dislikes)

    def add_party(self, party: Party):
        """
        Add party to this table

        :param party: party to be added
        :return:
        """
        party.seated = True
        self.parties.append(party)
        self.open_seats -= party.size


class Venue(object):
    """
    Class to represent venue
    """

    def __init__(self, name):
        """
        Initialize venue object

        :param name: Name of venue
        """
        self.name = name
        self.tables = []
        self.parties = []

    def __str__(self):
        """
        Create string representation of venue

        :return:
        """
        return "Venue - {}:\n\n{}".format(self.name, "\n\n".join([str(t) for t in self.tables]))

    def all_seated(self):
        """
        Check if all parties are seated

        :return: return true if all parties are seated, false if not
        """

        # any() will return true if any party is not seated so we negate that before returning
        return not any(not party.seated for party in self.parties)

    def total_capacity(self):
        """
        Calculate total capacity of venue

        :return: return number of seats total
        """
        if len(self.tables) == 0:
            return 0
        else:
            return sum(table.seats for table in self.tables)

    def party_exists(self, party: Party):
        """
        Check if party already exists

        :param party: party to check for
        :return: True if party exists, false if not
        """
        return any(p.name == party.name for p in self.parties)

    def space_left(self):
        """
        Get space left in venue

        :return: number of spots left in venue
        """
        return self.total_capacity() - sum(p.size for p in self.parties)

    def has_enough_space(self, party: Party):
        """
        Check if there is enough space for this party

        :param party: party to be added to group
        :return: true if there is enough space, false if not
        """
        group_total = sum(p.size for p in self.parties) + party.size

        return group_total <= self.total_capacity()

    def add_party(self, party: Party):
        """
        ADd party to venue parties list

        :param party: party to be added
        :return:
        """
        self.parties.append(party)

    def seat_parties(self):
        """
        Seat all parties by iterating through every possible
        combination of tables and parties

        :return: true if all parties were seated, false if not
        """

        # right rotate parties len(parties) times
        for p in self.parties:

            # right rotate tables len(tables) times
            for t in self.tables:

                # call recursive function to attempt seating
                if self.attempt_seating():
                    return True

                # refresh tables
                self.refresh_tables()

                # right rotation
                self.tables = [self.tables[-1]] + self.tables[0:-1]

            # right rotation
            self.parties = [self.parties[-1]] + self.parties[0:-1]

        return False

    def attempt_seating(self):
        """
        Attempt to seat all parties

        :return: true if all parties are seated, false if not
        """
        for p in self.parties:
            for t in self.tables:
                if p.seated:
                    continue

                # check for dislikes and space
                if not t.dislikes_seated(p) and t.space_available(p):
                    t.add_party(p)

        return self.all_seated()

    def refresh_tables(self):
        """
        Refresh tables

        :return:
        """
        for table in self.tables:
            for party in table.parties:
                party.seated = False
            table.open_seats = table.seats
            table.parties = []
