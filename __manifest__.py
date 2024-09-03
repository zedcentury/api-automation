# -*- coding: utf-8 -*-
{
    'name': "API Automation",

    'summary': "API Automation",

    'description': """
API Automation
    """,

    'author': "UIC Group",
    'website': "https://uic.group",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'token_authentication'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/api_endpoint.xml'
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': 'LGPL-3'
}
