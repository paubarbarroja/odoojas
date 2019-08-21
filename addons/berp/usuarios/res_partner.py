# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    fecha_nac = fields.Date(string="Fecha de Nacimiento", required=True)
    dni = fields.Char(string="DNI", required=True)
