# -*- coding: utf-8 -*-
from odoo import models, fields, api


class berp_atleta(models.Model):
    _name = "berp.atleta"
    _inherit = "hr.employee"

    nombre = fields.Char(string="nombre")
    genero = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='Genero')

    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''