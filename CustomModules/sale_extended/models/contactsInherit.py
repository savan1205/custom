from odoo import api,models,fields

class NewCities(models.Model):
	_inherit = "res.partner"



	city = fields.Many2one("cities.cities", string = "city",domain="[('state_id','=?',state_id)]")
	# state_id = fields.Many2one('res.country.state',string="state")
	

	# @api.model
	# def get_city(self):
	# 	for rec in self:
	# 		if rec.state_id:
	# 			res = self.env['']	




    # @api.onchange('country_id')
    # def _onchange_country_id(self):
    #     if self.country_id and self.country_id != self.state_id.country_id:
    #         self.state_id = False

    # @api.onchange('state_id')
    # def _onchange_state(self):
    #     if self.state_id.country_id:
    #         self.country_id = self.state_id.country_id

    


 



