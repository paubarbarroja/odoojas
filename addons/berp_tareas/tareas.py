# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class berp_tarea(models.Model):
    _name = "berp.tarea"
    _rec_name = "descripcion"

    @api.multi
    def cerrar_tarea(self):
        for record in self:
            record.estado = 'cerrada'

    @api.multi
    def acabar_tarea(self):
        for record in self:
            record.estado = 'acabada'

    @api.multi
    def reabrir_tarea(self):
        for record in self:
            record.estado = 'pendiente'

    @api.multi
    def imputar_horas(self):
        for record in self:
            context = {
                'default_tarea_id'      : record.id,
                'default_descripcion'   : record.descripcion,
                'default_imputado_por'  : self.env.user.id
            }
            view_ref = self.env.ref('berp_tareas.berp_20200221_1233_form')
            view_id = view_ref and view_ref.id or False
            return {
                'type'     : 'ir.actions.act_window',
                'name'     : 'Imputar Horas',
                'res_model': 'berp.tarea_tiempo',
                'view_type': 'form',
                'view_mode': 'form',
                'view_id'  : view_id,
                'target'   : 'new',
                'context'  : context,
                'flags': {'form': {'action_buttons': True},}
            }
    
    @api.depends('solicitado_por')
    def _uid_ok(self):
        uid = self.env.user.id
        for record in self:
            if record.solicitado_por.id == uid:
                record.uid_ok = True
            else:
                record.uid_ok = False

    def _search_uid_ok(self, operator, value):
        uid = self.env.user.id
        self = self.search([])
        ids = []
        for record in self:
            if record.solicitado_por.id == uid:
                ids.append(record.id)
        return [('id', 'in', ids)]




    nombre              = fields.Char('Titulo / Nombre')
    descripcion         = fields.Text('Descripción')
    fecha_demanda       = fields.Date('Fecha de demanda',default=fields.Date.context_today)
    solicitado_por      = fields.Many2one('res.users','Solicitado por',default=lambda self: self.env.user)
    tiempo_imputado     = fields.Float(string='Tiempo imputado')
    publicado           = fields.Boolean('Publicado')
    estado              = fields.Selection([('pendiente','Pendiente'),('acabada','Acabada'),('cerrada','Cerrada')], default="pendiente", string="Estado")
    tarea_tiempo_id     = fields.One2many('berp.tarea_tiempo','tarea_id','Tarea Tiempo')
    uid_ok              = fields.Boolean(compute='_uid_ok',string='uid Ok',search='_search_uid_ok',store=False)
    