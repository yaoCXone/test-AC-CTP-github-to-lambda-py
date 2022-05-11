import json
from pathlib import Path

def read_file_binary(file_path):
	return Path(file_path).read_bytes() # Python 3.5+


def has_records(response):
	try:
		json.loads()
		pass
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass


