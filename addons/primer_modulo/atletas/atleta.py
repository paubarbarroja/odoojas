# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Atleta(models.Model):
    _inherit = "hr.employee"

    ficha               = fields.Char(string='ficha',required=True)
