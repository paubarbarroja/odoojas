# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Company(models.Model):
    _inherit = "res.company"


    propagation_minimum_delta = fields.Integer('Minimum Delta for Propagation of a Date Change on moves linked together', default=1)
    internal_transit_location_id = fields.Integer('internal_transit_location_id')