# -*- coding: utf-8 -*-
{
    'name': 'Odoo CRM Dashboard',
	'category': 'General',
    'author':'Arun Reghu Kumar',
	'license': "LGPL-3",
    'version': '1.0', 
    'description': """    
                       Odoo CRM Dashboard   

    """,
    'maintainer': 'Arun Reghu Kumar',
    'depends': [
        'base','crm',      
    ],
    'data': [ 
         'views/crm_leads_view.xml',      
         'views/crm_dashboard.xml',
        
    ],
    'qweb': [
         "static/src/xml/crm_dashboard.xml",
    ],
    'images': ["static/description/banner.gif"],
    'installable': True,
    'auto_install': False,
}
