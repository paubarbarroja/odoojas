# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"

    atleta = fields.Many2one('berp.socio',string="Socio")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    marca = fields.Float(string="Marca")


    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''