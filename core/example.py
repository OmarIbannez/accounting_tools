from xmlparser import XmlParser
from csvexport import CsvExport
import os
import sys

data = []
header = ['Fecha', 'Serie', 'Folio', 'Metodo de Pago', '#cta', 'RFC', 'Razon Social', 'Concepto', 'Importe', 'IVA', 'IEPS', 'Total']
data.append(header[:])

'''file_name = 'xmls/0BA84398-2706-4EF0-B733-E5CED270BE1D.xml'
xml = XmlParser(file_name)
for row in xml.get_data():
	data.append(row)'''


walk_dir = 'xmls'
for root, subdirs, files in os.walk(walk_dir):
	for xml in files:
		xml = XmlParser(root + '/' + xml)
		for row in xml.get_data():
			data.append(row)

csv_writer = CsvExport(data, 'alpha.csv')
csv_writer.create()