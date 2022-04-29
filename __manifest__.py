# -*- coding: utf-8 -*-
{
    'name': "projects",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nikita Vornik",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/work_view.xml',
        'views/invoice_view.xml',
        'views/hr_employee_inherited_view.xml',
        'views/res_partner_inherited_view.xml',
        'views/templates.xml',
        'views/wizard_view.xml',
        'reports/project_report.xml',
        'reports/invoice_report.xml',
        'views/project_dash.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
