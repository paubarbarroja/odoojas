# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_atleta(models.Model):
    _inherit = "hr.employee"

    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)

    @api.model
    def create(self, values):
        '''vals = {
            'name': values['name'],
            'login': values['work_email'],
            'email': values['work_email'],
        }
        user = self.env['res.users'].create(vals)
        values.update({'user_id': user.id})'''
        record = super(berp_atleta, self).create(values)
        return record

    @api.multi
    def unlink(self):
        res = super(berp_atleta, self).unlink()
        return res