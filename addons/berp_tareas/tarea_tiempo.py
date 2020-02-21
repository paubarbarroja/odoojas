# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class berp_tarea_tiempo(models.Model):
    _name = "berp.tarea_tiempo"
    _rec_name = "descripcion"


    @api.onchange('hora_ini','hora_fin')
    def onchange_hora_ini(self):
        tiempo_trabajado = self.hora_fin-self.hora_ini
        self.write({'tiempo_trabajado':tiempo_trabajado})



    tarea_id            = fields.Many2one('berp.tarea','Tarea')
    descripcion         = fields.Char('Descripción')
    comentario          = fields.Text('Comentario')
    fecha               = fields.Date('Fecha', default=fields.Date.context_today)
    hora_ini            = fields.Float('Hora Inicio')
    hora_fin            = fields.Float('Hora Fin')
    tiempo_trabajado    = fields.Float('Tiempo Trabajado')
    imputado_por        = fields.Many2one('res.users','Imputado por')
