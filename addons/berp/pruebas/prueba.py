# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_prueba(models.Model):
    _name = "berp.prueba"


    nombre = fields.Char(string="Nombre")
    genero = fields.Selection()