# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools, exceptions, _
from odoo.modules import get_module_resource
import base64
import logging

_logger = logging.getLogger(__name__)

class berp_usuario_escuela(models.Model):
    _inherit = 'berp.usuario_escuela'

    solicitud               = fields.Many2one('berp.solicitud_escuela','Solicitud')
    
    
    