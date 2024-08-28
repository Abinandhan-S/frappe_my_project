# Copyright (c) 2024, Abinandhan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DemoDoctype2(Document):
	def before_save(self):
		doc=frappe.new_doc({
			'doctype':'Student Database',
			'roll_no':'ABC0003',
			'name1':'Abinandhan'
		})
		
