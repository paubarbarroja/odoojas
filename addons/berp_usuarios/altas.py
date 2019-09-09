# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_altas_popup(models.TransientModel):
    _name = 'berp.altas_popup'
    _description = 'berp_altas_popup'

    @api.multi
    def abrir_popup_crear_socio(self):
        print('##################################-------------------------> socio')

    @api.multi
    def abrir_popup_crear_atleta(self):
        print('##################################-------------------------> atleta %r', self)

        view_ref = self.env.ref('berp_usuarios.berp_29082019_2241_form')
        view_id = view_ref and view_ref.id or False
        return {
            'type'     : 'ir.actions.act_window',
            'name'     : 'Alta Atleta',
            'res_model': 'res.partner',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id'  : view_id,
            'target'   : 'new',
            'res_id'   : False,
        }


    atleta_id = fields.Many2one('res.partner', string="Atleta", domain="[('is_atleta', '=', True)]")
    socio_id = fields.Many2one('res.partner', string="Socio", domain="[('is_socio', '=', True)]")
