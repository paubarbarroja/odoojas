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
        user = self.env['res.users'].create(vals)
        _logger.debug('hola --> %r', user.id)
        vals = {
            'user_id' : user.id
        }
        self.write(vals)
        return record

    @api.multi
    def unlink(self):
        user = self.user_id
        _logger.debug('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     hola --> %r',self.user_id.id)
        _logger.debug('#########################################################################     hola --> %r',user)
        res = super(berp_atleta, self).unlink()

        self.env['res.users'].unlink(user)

        return res