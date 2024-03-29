#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2013-2015 Akretion (http://www.akretion.com)

{
    'name': 'France - FEC',
    'category': 'Localization',
    'summary': "Fichier d'Échange Informatisé (FEC) for France",
    'author': "Akretion,Odoo Community Association (OCA)",
    'version': '1.1.1',
    'website': 'http://www.akretion.com',
    'depends': ['l10n_fr', 'account_accountant'],
    'data': [
        'wizard/account_fr_fec_view.xml',
    ],
    'auto_install': True,
}
