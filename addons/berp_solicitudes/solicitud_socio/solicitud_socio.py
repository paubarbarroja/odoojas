# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_solicitud_socio(models.TransientModel):
    _name = 'berp.solicitud_socio'
    _description = 'berp_solicitud_socio'

    
    