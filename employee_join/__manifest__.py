# -*- coding: utf-8 -*-
{
    'name': "Employee Joining",

    'summary': """
        Now easily Manage employee with few clicks""",

    'description': """
        Manage Every details of Employee in few touch
    """,

    'author': "Erp Harbor",
    'website': "http://www.erpharbor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'HR',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/exit_checklist_view.xml',
        'views/joining_view.xml',
        'views/pre_experience_view.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
