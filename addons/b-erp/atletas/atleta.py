# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_atleta(models.Model):
    _inherit = "hr.employee"

    @api.model
    def create(self, values):
        record = super(berp_atleta, self).create(values)
        vals = {
            'name': values['name'],
            'login': values['work_email'],
        }
        self.env['res.users'].create(cr, uid, vals)
        return record