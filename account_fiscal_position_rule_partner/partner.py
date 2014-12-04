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

from openerp.osv import orm


class Partner(orm.Model):
    _name = _inherit = 'res.partner'

    def onchange_apply_fiscal_rule(self, cr, uid, ids, state_id, country_id,
                                   source_field=None, context=None):
        fpr_obj = self.pool['account.fiscal.position.rule']
        res = {'value': {}}
        if source_field == 'state_id':
            res.update(self.onchange_state(cr, uid, ids, state_id,
                                           context=context))

        if state_id and country_id:
            rule = fpr_obj.search(
                cr, uid,
                [
                    ('partner_state', '=', state_id),
                    ('partner_country', '=', country_id),
                    ('use_partner', '=', True),
                ],
                limit=1,
                context=context,
            )
            if rule:
                res['value']['property_account_position'] = fpr_obj.browse(
                    cr, uid, rule[0], context=context).fiscal_position_id.id
        else:
            res['value']['property_account_position'] = False

        return res
