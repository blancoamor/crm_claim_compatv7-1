# -*- coding: utf-8 -*-
##############################################################################
# CRM Claim Backwards Compatiblity
# Copyright (C) 2015 Moldeo (http://www.moldeo.coop)
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
#
##############################################################################
{
    'name': 'crm_claim_v7_compat',
    'version': '1.0.0',
    'category': 'CRM',
    'sequence': 1,
    'author': "Moldeo",
    'summary': 'CRM Claims v7.0 compatability',
    'depends': [
        "crm_claim",
    ],
    'data': [
        "crm_claim_view.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
