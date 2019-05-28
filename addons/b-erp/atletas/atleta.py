# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_atleta(models.Model):
    _inherit = "hr.employee"

    @api.model
    def create(self, values):
        record = super(berp_atleta, self).create(values)
        _logger.debug(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
        _logger.debug(" ---------------- >>   Hello %s",record)
        _logger.debug(" ---------------- >>   Hello %s",values)
        _logger.debug(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
        return record