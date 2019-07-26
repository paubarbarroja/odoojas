# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_evento(models.Model):
    _name = "berp.evento"
    _rec_name = "nombre"

    @api.multi
    def inscripcion_atleta(self):
        socio = self.env['berp.socio'].search([('user','=',self.env.user.id)])
        socios = []
        if socio:
            socios.append(socio.id)
            if self.atletas:
                for atleta in self.atletas:
                    socios.append(atleta.id)
            self.write({'atletas':[(6,0,socios)]})

    @api.multi
    def cerrar_evento(self):
        self.state = 'cerrado'

    @api.multi
    def abrir_evento(self):
        self.state = 'abierto'


    nombre = fields.Char(string="Nombre")
    pista = fields.Many2one('berp.pista',string="Pista")
    fecha = fields.Date(string="Fecha")
    pista_cubierta = fields.Boolean(string="Pista Cubierta")
    atletas = fields.Many2many('berp.socio',string="Atletas")
    state = fields.Selection([('abierto', 'Abierto'), ('cerrado', 'Cerrado')], required=True, default='abierto', string="Estado")
    pruebas = fields.Many2many('berp.prueba',string="Pruebas")
    attachment_ids = fields.Many2many('ir.attachment',string="Reglamento y Horario")
