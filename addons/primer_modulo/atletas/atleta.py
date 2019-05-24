# -*- coding: utf-8 -*-
from odoo import models, fields, api


class berp_atleta(models.Model):
    _inherit = "hr.employee"

    nombre              = fields.Char(string='Nombre',required=True)
