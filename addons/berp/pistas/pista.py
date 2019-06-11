# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_pista(models.Model):
    _name = "berp.pista"
    _rec_name = "nombre_mostrado"

    @api.multi
    def _get_nombre_mostrado(self):
        for record in self:
            record.nombre_mostrado = record.nombre+"("+record.ciudad+")"


    nombre = fields.Char(string="Nombre Pista")
    ciudad = fields.Char(string="Ciudad")
    direccion = fields.Char(string="Dirección")
    nombre_mostrado = fields.Char(compute="_get_nombre_mostrado",string="Nombre")
