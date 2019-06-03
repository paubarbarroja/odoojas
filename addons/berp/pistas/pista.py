# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_pista(models.Model):
    _name = "berp.pista"


    nombre = fields.Char(string="Nombre")
    ciudad = fields.Char(string="Ciudad")
    direccion = fields.Char(string="Dirección")
