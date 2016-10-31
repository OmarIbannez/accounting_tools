from lxml import etree
from HTMLParser import HTMLParser

IVA = ['16', '16.0', '16.00', '16.0000']

class XmlParser:
	""" Parsea el XML de la factura y retorna una lista """
	def __init__(self, file_name):
		self.file_name = file_name

	def get_data(self):
		try:
			parser = etree.XMLParser(recover=True, remove_blank_text=True)
			root = etree.parse(self.file_name, parser)
		except Exception as e:
			raise e

		comprobante = root.getroot()

		fecha = comprobante.get('fecha')
		if fecha: fecha = fecha.encode("utf-8")
		serie = comprobante.get('serie')
		if serie: serie = serie.encode("utf-8")
		folio = comprobante.get('folio')
		if folio: folio = folio.encode("utf-8")
		metodo_pago = comprobante.get('metodoDePago')
		if metodo_pago: metodo_pago = metodo_pago.encode("utf-8")
		num_cta = comprobante.get('NumCtaPago')
		if num_cta: num_cta = num_cta.encode("utf-8")
		emisor = comprobante.find('{http://www.sat.gob.mx/cfd/3}Emisor')
		razon_social = emisor.get('nombre')
		if razon_social: razon_social = razon_social.encode("utf-8")
		rfc = emisor.get('rfc')
		if rfc: rfc = rfc.encode("utf-8")
		subtotal = comprobante.get('subTotal')
		if subtotal: subtotal = subtotal.encode("utf-8")
		total = comprobante.get('total')
		if total: total = total.encode("utf-8")

		impuestos = comprobante.find('{http://www.sat.gob.mx/cfd/3}Impuestos')
		impuestos_traslados = impuestos.find('{http://www.sat.gob.mx/cfd/3}Traslados')
		traslados = []
		iva = 0
		ieps = 0

		if impuestos_traslados is not None:
			for traslado in impuestos_traslados:
				if traslado.get('impuesto') == 'IVA' and traslado.get('tasa') in IVA:
					iva = traslado.get('importe')
				if traslado.get('impuesto') == 'IEPS':
					ieps = traslado.get('importe')

		comprobante_conceptos = comprobante.find('{http://www.sat.gob.mx/cfd/3}Conceptos')
		data = []
		for concepto in comprobante_conceptos:
			descripcion = HTMLParser().unescape(concepto.get('descripcion'))
			if descripcion: descripcion = descripcion.encode("utf-8")
			importe = concepto.get('importe')
			if importe: importe = importe.encode("utf-8")
			concepto_object = [fecha, serie, folio, metodo_pago, num_cta, rfc, razon_social, descripcion, importe, iva, ieps, total]
			data.append(concepto_object)


		return data