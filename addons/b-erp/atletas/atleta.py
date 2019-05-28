# -*- coding: utf-8 -*-
from odoo import models, fields, api


class berp_atleta(models.Model):
    _inherit = "hr.employee"

    @api.model
    def create(self, values):
        record = super(berp_atleta, self).create(values)
        print 'Hello'

        return record