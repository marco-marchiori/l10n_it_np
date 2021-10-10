# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Italy - Accounting Non Profit',
    'version': '0.1',
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'author': 'marco marchiori',
    'description': """
Piano dei conti italiano per non profit
================================================

Italian accounting chart and localization.
    """,
    'category': 'Localization',
    'website': 'http://www.odoo.com/',
    'data': [
        'data/l10n_it_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.tax.group.csv',
        'data/account_tax_template.xml',
        'data/account.fiscal.position.template.csv',
        'data/account.chart.template.csv',
        'data/account_chart_template_data.xml',
        ],
}
