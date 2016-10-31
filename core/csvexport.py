import csv

class CsvExport:
	""" Crea un archivo CSV con una lista de listas"""
	def __init__(self, rows, out_file):
		self.rows = rows
		self.out_file = out_file

	def create(self):
		out_file  = open(self.out_file, "wb")
		csv_writer = csv.writer(out_file, quoting=csv.QUOTE_MINIMAL)
		for row in self.rows:
			csv_writer.writerow(row)
		out_file.close()