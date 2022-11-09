from odoo import api,fields,models

class SaleConfiguration(models.Model):
	_inherit = 'res.company'
	

	status = fields.Char(string = "whats the status")
	