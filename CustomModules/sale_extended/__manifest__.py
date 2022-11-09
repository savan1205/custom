{
    'name': 'sale ext',
    'version': '1.0',
    'category': 'sale ext',
    'summary': 'sale ext management',
    'sequence': -500,
    'description': """
This module contains all the common inherted features of sale.
    """,
    'depends': ['base','sale','contacts'],
    'data':[
    'security/ir.model.access.csv',
    'views/saleInherit.xml',
    'views/contactsInheritedViews.xml',
    'views/citiesViews.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    
       
    'license': 'LGPL-3',
}
