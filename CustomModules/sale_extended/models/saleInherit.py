from odoo import api,fields,models

class MartProducts(models.Model):
	_inherit='sale.order'

	mobile=fields.Integer(string="mobile number")

	price = fields.Integer(string="price")
	price_for_replace = fields.Integer(string="Price For replace")

	# customer = fields.Char(string="customer")

	state = fields.Selection(selection_add=[
        ('sent', 'Quotation Sent'),
        ('to_approve', 'To Approve'),
        ('sale', 'Sales Order'),
        ], string='Status')

	# cities = fields.Char(string = 'city')


	def get_price(self):
		print("_____________--------------------Button Executed")

	# def name_get(self):
	# 	result = []
	# 	for record in self:
	# 		result.append((record.id, "{} + {} ".format(record.name, record.country_id.code)))
	# 	return result	
