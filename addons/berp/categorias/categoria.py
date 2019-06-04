# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_categoria(models.Model):
    _name = "berp.categoria"

    nombre = fields.Char(string="Nombre")