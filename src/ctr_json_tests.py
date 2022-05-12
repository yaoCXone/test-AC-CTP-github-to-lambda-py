from ctr_json import ctr_json_object as ctr_obj
import event_samples as evnts # import event_1, event_ctr_01
#from event_samples import event_ctr_01 as ctr_01
import unittest
import json

# unit test inherit unittest.TestCase
class test_ctr_json_obj(unittest.TestCase):
	# unit test's name must start with "test_"
	def test_is_ctr_json_should_be_false_whith_not_ctr_json(self):
		ctr = ctr_obj(evnts.event_1())
		self.assertFalse(ctr.is_ctr_json())

	def test_is_ctr_json_should_be_true_whith_ctr_json(self):
		ctr = ctr_obj(evnts.event_ctr_01())
		self.assertTrue(ctr.is_ctr_json())

if __name__ == '__main__':
	unittest.main()