from odoo import api,models,fields

class AllCities(models.Model):
	_name = "cities.cities"
	_rec_name = "city"
	_description="This model stores data of citiess"


	state_id = fields.Many2one('res.country.state', string = "state")
	city = fields.Char(string = "city")



 



