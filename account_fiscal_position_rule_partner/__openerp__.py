# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account Fiscal Position Rule Partner',
    'version': '1.r',
    'category': 'Generic Modules/Accounting',
    'author': 'Savoir-faire Linux',
    'license': 'AGPL-3',
    'website': 'http://www.savoirfairelinux.com',
    'description': """
    Include a rule to decide the correct fiscal position for Partners
    """,
    'depends': [
        'account_fiscal_position_rule',
        'base',
    ],
    'data': [
        'partner_view.xml',
        'fiscal_position_rule_view.xml',
    ],
    'demo': [],
    'installable': True,
}
