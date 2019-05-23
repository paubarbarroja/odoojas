# -*- coding: utf-8 -*-
from odoo import models, fields, api


class jas_atleta(models.Model):
    _name = 'jas.atleta'
    _rec_name = 'nombre'

    nombre              = fields.Char(string='Nombre',required=True)
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Char(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Char(string='edad',required=True)
    genero              = fields.Char(string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
