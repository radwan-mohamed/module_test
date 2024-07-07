# real_estate/__manifest__.py

{
    'name': 'Real Estate Management',
    'summary': 'Manage properties, agents, and customers',
    'description': 'This module allows you to manage real estate properties, agents, and customers in Odoo.',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'category': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/agent_views.xml',
        'views/customer_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
