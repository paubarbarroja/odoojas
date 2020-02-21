# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class berp_tarea_tiempo(models.Model):
    _name = "berp.tarea_tiempo"
    _rec_name = "descripcion"


    tarea_id            = fields.Many2one('berp.tarea','Tarea')
    descripcion         = fields.Char('Descripción')
    comentario          = fields.Text('Comentario')
    fecha               = fields.Date('Fecha')
    hora_ini            = fields.Float('Hora Inicio')
    hora_fin            = fields.Float('Hora Fin')
    tiempo_trabajado    = fields.Float('Tiempo Trabajado')
    imputado_por        = fields.Many2one('res.users','Imputado por')
