# -*- coding: utf-8 -*-
{
    'name': "Employee Management System",

    'summary': """Manage trainings""",

    'description': """
        Employee Management module for managing employee details:
        
        """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'other',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_attendance', 'hr_holidays', 'project', 'hr_payroll'],

    # always loaded
    'data': ['security/ir.model.access.csv',
             'views/employee_views.xml',
             ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
