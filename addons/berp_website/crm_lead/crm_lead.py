# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class CrmLead(models.Model):
    _inherit = "crm.lead"

    genre = fields.Char(string="Genere")
    dni = fields.Char(string="DNI")
    direccion_postal = fields.Char(string="Direcció Postal")
    birthday_date = fields.Char(string="Data de Naixement")
    compte_bancari = fields.Char(string="Compte Bancari")
    banc = fields.Char(string="Banc")
    poblacion = fields.Char(string="Població")
    codigo_postal = fields.Char(string="Codi Postal")