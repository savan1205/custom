
import csv
from odoo import fields, models,api
from datetime import date,datetime


class GetQuotationsWizard(models.TransientModel):
    _name = "quotation.wizard"
    _description = "get quotation between two dates"
    # _rec_name="patient_id"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    
    
   
    def get_quotations(self):
            print("________________button executed")
            res = self.env['sale.order'].search([('state','=','draft')])
            print('__________________________res',res)           
            header=['sr_no','customer_name','quot_date','Total','sales_person']

            srno=0

            f= open('/home/odoo/Desktop/CustomModules/sale_quotation/csvFile/requiredQuotes.csv','w')

            writer = csv.writer(f)
            writer.writerow(header)

            for checkDate in res:
                if checkDate.date_order.date() > self.start_date and checkDate.date_order.date() < self.end_date:
                    print("_______+++++++++++__________",checkDate.partner_id.name)
                    srno+=1
                    plain=[]
                    plain.append(srno) 
                    plain.append(checkDate.partner_id.name) 
                    plain.append(checkDate.date_order) 
                    plain.append(checkDate.amount_total) 
                    plain.append(checkDate.user_id.name)
                    writer.writerow(plain)



            f.close()

            # print("________________",self.patient_id)
            # if self.patient_id.stat == 'draft':
            #     self.patient_id.stat = 'cancelled'
            # else:
            #     raise ValidationError(("You can only cancel an Draft appointment."))



        # return{
        # 'type':'ir.actions.act_window',
        # 'name':'Quotations',
        # 'res_model':'sale.view_quotation_tree_with_onboarding',
        # 'domain':[(self.state,'==','draft')],
        # 'view_mode':'tree,form',
        # 'target':'current',
        # # 'context': {'date': self.id}
        #  }


       