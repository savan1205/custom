from odoo import api,fields,models

class ResConfig(models.TransientModel):
	_inherit = 'res.config.settings'
	


	status = fields.Char(related="company_id.status" , string="stat",readonly=False)
	
