# -#- coding: utf-8 -#-
##############################################################################
# CRM Claim - Backward Compatiblity 
# Copyright (C) 2014 Moldeo Interactive www.moldeo.coop
# @author Gustavo Orrillo <gustavo.orrillo@moldeo.coop>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from openerp.osv import fields, osv

AVAILABLE_STATES = [
    ('draft', 'New'),
    ('cancel', 'Cancelled'),
    ('open', 'In Progress'),
    ('pending', 'Pending'),
    ('done', 'Closed')
]


class crm_claim_stage(osv.osv):
	_name = "crm.claim.stage"
	_description = "Claim Stage"
	_inherit = 'crm.claim.stage'

	_columns = {
		'state': fields.selection(selection=AVAILABLE_STATES,string="CRM Status",required=True),
		}

	_defaults = {
		'state': 'draft',
		}

crm_claim_stage()

class crm_claim(osv.osv):
	""" Crm claim
	"""
	_name = "crm.claim"
	_description = "Claim"
	_order = "priority,date desc"
	_inherit = 'crm.claim'

	_columns = {
	        'state': fields.related('stage_id', 'state', type="selection", store=True,
                selection=AVAILABLE_STATES, string="Status", readonly=True,
                help='The status is set to \'Draft\', when a case is created.\
                      If the case is in progress the status is set to \'Open\'.\
                      When the case is over, the status is set to \'Done\'.\
                      If the case needs to be reviewed then the status is \
                      set to \'Pending\'.'),
	}

crm_claim()
