# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_solicitud_socio(models.Model):
    _name = 'berp.solicitud_socio'
    _description = 'berp_solicitud_socio'


    image                   = fields.Binary("Imatge", attachment=True, default=lambda self:self._get_default_image('a','b','c'))
    name                    = fields.Char(string="Nom")
    apellido1               = fields.Char(string="Primer cognom")
    apellido2               = fields.Char(string="Segon cognom")
    fecha_nac               = fields.Date(string="Data de naixement")
    dni                     = fields.Char(string="DNI")
    cuenta_bancaria         = fields.Char(string="Compte bancari")
    banco                   = fields.Char(string='Nom del banc')
    titular_cuenta_bancaria = fields.Char(string='Nom del titular')
    genero                  = fields.Selection([('1', 'Masculí'), ('2', 'Femení')], string='Gènere')
    street                  = fields.Char(string='Adreça')
    city                    = fields.Char(string='Ciutat')
    cp                      = fields.Char(string='Codi postal')
    country_id              = fields.Many2one(comodel_name='res.country', string='Nacionalitat')
    phone                   = fields.Char(string='Nº telèfon/mòvil')
    phone_alt               = fields.Char(string='Nº telèfon/mòvil alternatiu')
    email                   = fields.Char(string='Correu electronic')


    fecha_formulario        = fields.Date(string='Data solicitud')
    otros                   = fields.Text(string='Otros')
