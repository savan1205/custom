from odoo import fields, models,api
from datetime import date,datetime



class Many2ManyTask(models.Model):
	_inherit="sale.order"


	partner_ids=fields.Many2many(comodel_name="res.partner",string="Partner Names")
	product_id=fields.Many2one('product.product',string='product')
	quantity=fields.Float(string='quantity')


	def action_confirm(self):
		print("______________________________",self)
		template_id = self.env.ref('sale_quotation.email_template_send_mail')
		self.env['mail.template'].browse([(template_id.id)]).send_mail(self.id,force_send=True)
		return super(Many2ManyTask,self).action_confirm()

	

# static input for special method in many@many
	

	def insert_tags(self):
		print("_________________clicked")
		ids=[14,26,33]
		print("++++++++++++++++",self.write({"partner_ids":[(6,0,ids)]}))
		self.write({"partner_ids":[(6,0,ids)]})




	@api.onchange('product_id','quantity')
	def add_product(self):
		if self.product_id in self.order_line.product_id:
			print("_________________===============product already exists")
			
			for value in self.order_line:
				print("va;ue---------------value---------",value.id)
				if self.product_id == value.product_id:
					
					add_list=[(1,value.id,{
						'product_uom_qty':self.quantity,
						})]

					self.write({
						'order_line':add_list,
						})


				# self.order_line.write({(1,value.product_uom_qty,{
			 #        'product_uom_qty':self.quantity,
			 #        })})
		else:		
			add_data = []	
			for result in self.order_line:
				
				print("__________________________",result)


				add_data.append((0,0,{
					'product_id':self.product_id.id,
			        'product_uom_qty':self.quantity,
			        }))
			    # print("---------------------------",add_data)
			    # ids=self.partner_ids.ids

			self.write({
			    'order_line':add_data,
			    })


	

        
