# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class berp_tarea(models.Model):
    _name = "berp.tarea"

    descripcion         = fields.Char('Descripción')
    comentario          = fields.Text('Comentario')
    fecha_demanda       = fields.Date('Fecha de demanda')
    solicitado_por      = fields.Many2one('res.users','Solicitado por')
    tiempo_imputado     = fields.Float(compute='_get_tiempo_imputado',string='Tiempo imputado')
    publicado           = fields.Boolean('Publicado')
