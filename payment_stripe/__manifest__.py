# -*- coding: utf-8 -*-

{
    'name': 'Stripe Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Stripe Implementation',
    'version': '1.1.1',
    'description': """Stripe Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_stripe_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
}
