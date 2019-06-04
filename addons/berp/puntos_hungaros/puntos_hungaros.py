# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_puntos_hungaros(models.Model):
    _name = "berp.puntos_hungaros"
    _rec_name = "puntos"


    puntos = fields.Integer(string="Nombre")
    pruebas = fields.Many2one('berp.prueba',string="Pruebas")
    marca = fields.Float(string="Marca")