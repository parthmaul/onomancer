import unittest
import onomancer as ono
import onomancer.utils

class TestOnomancer(unittest.TestCase):

	def test_single(self):
		self.assertEqual(ono.predict("PaRth"), {"PARTH":"M"})

	def test_many(self):
		self.assertEqual(ono.predict(["PaRTH", "GandALF","zelda"]), {'PARTH': 'M', 'GANDALF': 'M', 'ZELDA': 'F'})

	def test_utils(self):
		self.assertEqual(onomancer.utils.standardize("PARTH"), "Parth")


if __name__ == '__main__':
    unittest.main()
