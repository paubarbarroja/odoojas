# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.tools import email_re, email_split
from odoo.exceptions import UserError, AccessError

from . import crm_stage

_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit = "crm.lead"

    genre = fields.Char(string="Genere")
    dni = fields.Char(string="DNI")
    direccion_postal = fields.Char(string="Direcció Postal")
    birthday_date = fields.Char(string="Data de Naixement")
    compte_bancari = fields.Char(string="Compte Bancari")
    banc = fields.Char(string="Banc")
    poblacion = fields.Char(string="Població")
    codigo_postal = fields.Char(string="Codi Postal")