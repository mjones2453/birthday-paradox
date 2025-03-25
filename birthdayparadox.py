"""Birthday Paradox Simulation
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem """

import datetime, random

def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        """The year is unimportant for our simulation, as long as all
        birthdays have the same year. """
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in a birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.
    
    # Compare each birthday to every other birthday:
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a # Return the matching birthday.
            

# Display the intro:
print('''Birthday Paradox
      
The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
      
(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')




