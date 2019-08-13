# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_inscripcion_evento(models.Model):
    _name = "berp.inscripcion_evento"
    _rec_name = "atletas"


    evento = fields.Many2one('berp.evento')
    atleta = fields.Many2one('berp.socio',string="Atletas")
    pruebas = fields.One2many('berp.prueba','nombre',string="Pruebas")
