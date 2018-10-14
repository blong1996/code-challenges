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
    def __init__(self, name, size):
        """
        Initialize party object
        :param name: Name of party (uid)
        :param size:
        """
        self.name = name
        self.size = size
        self.dislikes = []
        self.seated = False

    def __str__(self):
        """
        Create string representation of party

        :return:
        """
        return "{}, party of {}".format(self.name, self.size)

    def add_dislike(self, party):
        """
        Add a party to this party's list of dislikes

        :param party: party to add
        :return:
        """
        self.dislikes.append(party)

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
    def __init__(self, letter: str, seats: int):
        """
        Initialize table object

        :param letter: Represents table (uid)
        :param seats: Represents number of seats at table
        """
        self.letter = letter
        self.seats = seats
        self.open_seats = seats
        self.parties = []

    def __str__(self):
        """
        Create string representation of table

        :return:
        """
        return "Table {}:\n\t{}".format(self.letter, "\n\t".join(self.parties))

    def is_seated(self, party: Party):
        """
        Check if a party is seated at this table

        :param party: party to check for

        :return: true if party is seated here, false if not
        """
        return any(p.name == party.name for p in self.parties)

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
        return "Venue {}:\n\n{}".format(self.name, "\n\n".join(self.tables))

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

    def enough_space(self, party):
        """
        Check if there is enough space for this party

        :param party: party to be added to group
        :return: true if there is enough space, false if not
        """
        group_total = sum(p.size for p in self.parties) + party.size

        return group_total <= self.total_capacity()