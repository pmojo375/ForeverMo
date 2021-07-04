from django.test import TestCase
from main.models import *

class AddGuestTestCase(TestCase):
	def setUp(self):

		guest1 = Guest(firstname="Jim", lastname="Smith", foodchoice=1)
		guest2 = Guest(firstname="Jon", lastname="James", foodchoice=0)
		guest3 = Guest(firstname="Hank", lastname="Mojo", foodchoice=2)
		guest4 = Guest(firstname="Gary", lastname="Granger", foodchoice=2)

		guest1.save()
		guest2.save()
		guest3.save()
		guest4.save()

		plusone1 = PlusOne(firstname="Bob", lastname="White", foodchoice=1, host=guest2)
		plusone2 = PlusOne(firstname="Bill", lastname="Builder", foodchoice=2, host=guest3)
		plusone3 = PlusOne(firstname="Brad", lastname="Brown", foodchoice=3, host=guest4)

		plusone1.save()
		plusone2.save()
		plusone3.save()


	def testAddGuestNoPlusOne(self):
		guest = Guest(firstname="Tim", lastname="Black", foodchoice=1)
		guest.save()

		dbGuest = Guest.objects.get(firstname="Tim", lastname="Black")

		self.assertEqual(dbGuest.firstname, "Tim")
		self.assertEqual(dbGuest.lastname, "Black")
		self.assertEqual(dbGuest.foodchoice, 1)

	def testAddGuestWithPlusOne(self):
		guest = Guest(firstname="Tim", lastname="Black", foodchoice=1)
		guest.save()

		p1 = PlusOne(firstname="Boomer", lastname="Kane", foodchoice=2, host=guest)
		p1.save()

		dbGuest = Guest.objects.get(firstname="Tim", lastname="Black")

		self.assertEqual(dbGuest.firstname, "Tim")
		self.assertEqual(dbGuest.lastname, "Black")
		self.assertEqual(dbGuest.foodchoice, 1)
		self.assertEqual(dbGuest.plusone.firstname, "Boomer")
		self.assertEqual(dbGuest.plusone.lastname, "Kane")
		self.assertEqual(dbGuest.plusone.foodchoice, 2)

	def amendGuestWithPlusOne(self):
		guest = Guest.objects.get(firstname="Jim", lastname="Smith")

		p1 = PlusOne(firstname="Boomer", lastname="Kane", foodchoice=2, host=guest)
		p1.save()

		dbGuest = Guest.objects.get(firstname="Jim", lastname="Smith")

		self.assertEqual(dbGuest.firstname, "Jim")
		self.assertEqual(dbGuest.lastname, "Smith")
		self.assertEqual(dbGuest.foodchoice, 1)
		self.assertEqual(dbGuest.plusone.firstname, "Boomer")
		self.assertEqual(dbGuest.plusone.lastname, "Kane")
		self.assertEqual(dbGuest.plusone.foodchoice, 2)

	def amendGuestsPlusOne(self):
		guest = Guest(firstname="firstname1", lastname="lastname1", foodchoice=1)
		

		p1 = PlusOne(firstname="p1firstname1", lastname="p1lastname1", foodchoice=2, host=guest)
		p1.save()

		self.assertEqual(p1.host, guest)

		p2 = PlusOne(firstname="p1firstname2", lastname="p1lastname2",foodchoice=1, host=guest)
		p2.save()

		guest = Guest.objects.get(firstname="firstname1")
		#p1 = PlusOne.objects.get(firstname="p1firstname1")
		p2 = PlusOne.objects.get(firstname="p1firstname2")

		self.assertEqual(p2.host, guest)
		self.assertEqual(p1.host, guest)
		self.assertEqual(guest.plusone, p1)
		self.assertEqual(guest.plusone, p2)

		gp1 = guest.plusone

		self.assertEqual(gp1.firstname, "p1firstname1")
		self.assertEqual(gp1.firstname, "p1firstname2")

