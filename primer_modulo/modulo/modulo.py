from odoo import models, fields, api, _


class Helipistas_modulo(models.Model):
    _name = 'helipistas.modulo'
    _rec_name = 'descripcion'

    descripcion = fields.Char(string='Descripcion')
