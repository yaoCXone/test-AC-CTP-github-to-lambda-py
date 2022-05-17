import json


class ctr_json_object:
	ctr_json=None
	def __init__(self,json_obj):
		self.ctr_json = json_obj

	def ctr_json(self):
		return ctr_json;

	def is_ctr_json(self):
		return (self.contains_key("AWSContactTraceRecordFormatVersion") and
			self.contains_key("AWSAccountId") and
			self.contains_key("ContactId") and
			self.contains_key("Recordings"))

	def contains_key(self, keyword):
		return not self.ctr_json.get(keyword) is None



