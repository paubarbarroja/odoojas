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
            '''
            #Todo hacer bien la insripcion al evento por parte del atleta
            #     abrir popup de la clase inscripcion_evento y escojer las pruebas puestas en el evento por parte del director tecnico, o administrador
            #     una vez inscrito veremos una lista de atletas inscritos y para ver las pruebas o podemos hacer un campo en el suyo que sea un function de todas las pruebas escritas o
            #     puede ser al clikar encima del atleta que se abra un ventana o otra vista con la informacion de la inscripcion entre ello las pruebas a las que se ha inscrito
            
            view_ref = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'operacion_comercial',
                                                                           'hlp_rel_oc_toc_form')
            view_id = view_ref and view_ref[1] or False

            if isinstance(ids, list):
                ids = ids[0]

            return {
                'type': 'ir.actions.act_window',
                'name': 'Notas',
                'res_model': 'helipistas.rel_oc_toc',
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': view_id,
                'res_id': ids,
                'target': 'new'
            }'''
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
    atletas = fields.One2many('berp.inscripcion_evento','evento',string="Atletas")
    state = fields.Selection([('abierto', 'Abierto'), ('cerrado', 'Cerrado')], required=True, default='abierto', string="Estado")
    pruebas = fields.Many2many('berp.prueba',string="Pruebas")
    attachment_ids = fields.Many2many('ir.attachment',string="Reglamento y Horario")
