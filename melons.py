"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """ sets default attributes adn methods for subclasses DomesticMelonOrder and 
    InternationalMelonOrder"""

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        if country_code:
            self.country_code = country_code
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = 0

        if self.species == "Christmas melons":
            base_price = base_price * 1.5
            if self.order_type == "international" and self.qty < 10:
                total += 3

        total = total + (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # country_code = country_code
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)


class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0.00
    passed_inspection = False

    def mark_inspection(self):
        """Return the country code."""

        passed_inspection = True
