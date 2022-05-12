import json


class ctr_json_object:
	ctr_json=None
	def __init__(self,json_obj):
		self.ctr_json = json_obj

	def ctr_json(self):
		return ctr_json;

	def is_ctr_json(self):
		return (self.contains_node("AWSContactTraceRecordFormatVersion") and
			self.contains_node("AWSAccountId") and
			self.contains_node("ContactId") and
			self.contains_node("Recordings"))

	def contains_node(self, keyword):
		return not self.ctr_json.get(keyword) is None

