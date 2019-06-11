# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_grupo_entreno(models.Model):
    _name = "berp.grupo_entreno"
    _rec_name = "nombre"


    nombre = fields.Char(string="Nombre")
    atletas = fields.One2many('berp.socio','grupo_entreno',string="Atletas")
