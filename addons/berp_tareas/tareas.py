# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class berp_tarea(models.Model):
    _name = "berp.tarea"
    _rec_name = "descripcion"

    @api.multi
    def _get_tiempo_imputado(self):
        for record in self:
            record.tiempo_imputado = 0

    descripcion         = fields.Char('Descripción')
    comentario          = fields.Text('Comentario')
    fecha_demanda       = fields.Date('Fecha de demanda')
    solicitado_por      = fields.Many2one('res.users','Solicitado por')
    tiempo_imputado     = fields.Float(compute='_get_tiempo_imputado',string='Tiempo imputado')
    publicado           = fields.Boolean('Publicado')
    estado              = fields.Selection([('pendiente','Pendiente'),('acabada','Acabada'),('cerrada','Cerrada')], default="pendiente", string="Estado")
