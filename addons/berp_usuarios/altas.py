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
        partner_id = False
        if self.partner_id:
            partner_id = self.partner_id.id
            self.partner_id.write({'is_socio':True})


        context = {
            'default_is_socio': True,
        }
        view_ref = self.env.ref('berp_usuarios.berp_29082019_2241_form')
        view_id = view_ref and view_ref.id or False
        return {
            'type'     : 'ir.actions.act_window',
            'name'     : 'Alta Socio',
            'res_model': 'res.partner',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id'  : view_id,
            'target'   : 'new',
            'res_id'   : partner_id,
            'context'  : context,
        }

    @api.multi
    def abrir_popup_crear_atleta(self):
        partner_id = False
        if self.partner_id:
            partner_id = self.partner_id.id
            self.partner_id.write({'is_atleta':True})

        context = {
            'default_is_atleta' : True,
        }
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
            'res_id'   : partner_id,
            'context'  : context,
        }




    partner_id = fields.Many2one('res.partner', string="Usuario")
