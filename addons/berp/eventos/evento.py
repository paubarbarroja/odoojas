# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_evento(models.Model):
    _name = "berp.eventop"


    nombre = fields.Char(string="Nombre")
    pista = fields.Many2one('berp.pista',string="Pista")
    fecha = fields.Date(string="Fecha")
