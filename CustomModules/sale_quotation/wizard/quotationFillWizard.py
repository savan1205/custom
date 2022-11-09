# import csv
from odoo import fields, models,api
from datetime import date,datetime


class QuotationFillWizard(models.TransientModel):
    _name = "fill.wizard"
    _description = "create quotation between two dates"
    # _rec_name="quoteFill_id"

    quotations_id = fields.Many2one(comodel_name="sale.order", string="Quotations",domain=[('state','=','draft')],required=True)
    quoteFill_ids = fields.One2many(comodel_name="quotation.data",inverse_name="quote_id", string="Quotations",required=True)
    partner_ids = fields.Many2many(comodel_name = "res.partner",string="Partner Name",required=True)

    def action_fill(self):
        add_data = []
        for result in self.quoteFill_ids:
            print("__________________________",self.quotations_id)
            add_data.append((0,0,{
                'product_id':result.product_id.id,
                'product_uom_qty':result.quantity,
                'price_unit':result.unit,
                }))
            print("---------------------------",add_data)
            # ids=self.partner_ids.ids

        self.quotations_id.write({
            'order_line':add_data,
            'partner_ids':[(6,0,self.partner_ids.ids)]
            })

            # m2m_contacts=({"partner_ids":[[(6,0,ids)]]})
        
        # ids=self.partner_ids.ids
        # self.write({"partner_ids":[(6,0,ids)]})      



class QuotationData(models.TransientModel):
    _name='quotation.data'

    quote_id = fields.Many2one(comodel_name="fill.wizard",string="quote" )
    product_id = fields.Many2one(comodel_name="product.product",string="product")
    quantity = fields.Float(string="quantity")
    unit = fields.Float(string="Unit")

















        