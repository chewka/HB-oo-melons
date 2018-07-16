
from random import randint
"""Classes for melon orders."""
class AbstractMelonOrder:
	"""An abstract base class that other Melon Orders inherit from."""

	def __init__(self, species, qty, country_code=None):
		self.species = species
		self.qty = qty
		self.shipped = False

		if country_code:
			self.country_code = country_code

	def get_country_code(self):
		"""Return the country code."""
		
		return self.country_code

	def mark_shipped(self):
		self.shipped = True

	def get_base_price(self):

		random_num = randint(5,9)

		return random_num

	def get_total(self):
		"""Calculate price, including tax."""
		
		# base_price = 5
		base_price = self.get_base_price()

		xmas_price = 1.5 * base_price
		international_fee = 3

		total = (1 + self.tax) * self.qty * base_price

		if self.species == 'xmas':
			total = total = (1 + self.tax) * self.qty * xmas_price

		if self.country_code != "US" and self.qty < 10:
			total = total + international_fee

		return total




class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""
	order_type = "domestic"
	tax = 0.08
	country_code = 'US'


class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""
	order_type = "international"
	tax = 0.17


class GovernmentMelonOrder(AbstractMelonOrder):

	order_type = "government"
	tax = 0
	country_code = 'US'

	passed_inspection = False

	def mark_inspection(self, passed):
		
		self.passed_inspection = passed
		
		return self.passed_inspection
