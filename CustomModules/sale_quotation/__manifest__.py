{
    'name': 'sale quotation',
    'version': '1.0',
    'category': 'sale quotation',
    'summary': 'sale quotation',
    'sequence': -600,
    'description': """
This module contains all the common inherted features for sale quotation.
    """,
    'depends': ['base','sale'],
    'data':[
    'security/ir.model.access.csv',

    'wizard/getQuotationWizard.xml',
    'wizard/quotationFillWizard.xml',

    'data/sale_order_mail.xml',
    'data/sale_quotation_mail.xml',

    'report/report_inherit.xml',

    'views/so_custom_menuView.xml',
    'views/so_country_inheritView.xml',
    
    'views/resConfigViews.xml',
    'views/quotationFillViews.xml',
    'views/m2m_views.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    
       
    'license': 'LGPL-3',
}
