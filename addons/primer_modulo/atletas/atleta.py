# -*- coding: utf-8 -*-
from odoo import models, fields, api


class jas_atleta(models.Model):
    _name = 'jas.atleta'
    _rec_name = 'nombre'

    nombre              = fields.Char(string='Nombre',required=True)
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
