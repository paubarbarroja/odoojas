# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools, exceptions, _
from odoo.modules import get_module_resource
import base64
import logging

_logger = logging.getLogger(__name__)

class berp_solicitud_renovacion_ficha(models.Model):
    _name = 'berp.solicitud_renovacion_ficha'
    _description = 'berp_solicitud_renovacion_ficha'
    _rec_name = "titulo"

    @api.multi
    def get_titulo(self):
        for item in self:
            item.titulo = ''
            if item.nombre != False:
                item.titulo = item.nombre
            if item.apellido1 != False:
                item.titulo = item.titulo+" "+item.apellido1
            if item.apellido2 != False:
                item.titulo = item.titulo+" "+item.apellido2


    titulo                  = fields.Char(compute='get_titulo',string='Nombre completo',store=False)
    nombre                  = fields.Char(string='Nombre')
    apellido1               = fields.Char(string='Primer Apellido')
    apellido2               = fields.Char(string='Segon Apellido')
    phone                   = fields.Char(string='Nº telèfon/mòvil')
    email                   = fields.Char(string='Correu electronic')
    ficha                   = fields.Selection([('territorial','Territorial'),('nacional','Nacional')],string='Tipo de ficha')
    
    