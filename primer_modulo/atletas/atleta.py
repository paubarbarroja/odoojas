from odoo import models, fields, api, _


class jas_atleta(models.Model):
    _name = 'jas.atleta'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
