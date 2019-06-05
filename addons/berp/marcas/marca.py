# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"
    # todo
    #  Pensar bien la manera de mostrar las marcas en los otros formularios,
    #  1-  para crear una variable conjunta de todas como pn/sn/ref.origen/lote de helipistas
    #  2-  o si al contrario se mostrara en O2M y se veran todas las variables en forma de tree
    #_rec_name = "nombre"

    '''
    def hlp_str_to_float_time(time_string):
        fields = time_string.split(":")
        hours = fields[0] if len(fields) > 0 else 0.0
        minutes = fields[1] if len(fields) > 1 else 0.0
        seconds = fields[2] if len(fields) > 2 else 0.0
        return float(hours) + (float(minutes) / 60.0) + (float(seconds) / pow(60.0, 2))
'''

    @api.onchange('marca_s')
    def onchange_marca_s(self):
        float = 0.00
        if self.marca_s:
            _logger.error('ERROR ------------------------------------------ campo prueba --> %r', self.prueba)
            prueba = self.env['berp.prueba'].browse(self.prueba)
            _logger.error('ERROR ------------------------------------------ browse prueba --> %r', prueba)

            #self.marca = float
            #raise exceptions.ValidationError('Not valid message')
            #raise exceptions.UserError('Business logic error')
        return True

    atleta = fields.Many2one('berp.socio',string="Socio")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    marca = fields.Float(string="Marca")
    marca_s = fields.Char(string="Marca")



    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''