from odoo import api,fields,models

class StateInherit(models.Model):
	_inherit='res.country.state'

	def name_get(self):
		result = []
		for record in self:
		   result.append((record.id, "{} - {}".format(record.name, record.country_id.code)))
		return result
