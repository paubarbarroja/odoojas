# -*- coding: utf-8 -*-
from odoo import models, fields, api


class jas_atleta(models.Model):
    _name = 'jas.atleta'
    _rec_name = 'nombre'

    nombre              = fields.Char(string='Nombre',required=True)
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Char(string='Apellido',required=True)
    dni                 = fields.Char(string='Apellido',required=True)
    edad                = fields.Char(string='Apellido',required=True)
    genero              = fields.Char(string='Apellido',required=True)
    telefono            = fields.Char(string='Apellido',required=True)
    mail                = fields.Char(string='Apellido',required=True)