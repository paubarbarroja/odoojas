# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"
    # todo
    #  Pensar bien la manera de mostrar las marcas en los otros formularios,
    #  1-  para crear una variable conjunta de todas como pn/sn/ref.origen/lote de helipistas
    #  2-  o si al contrario se mostrara en O2M y se veran todas las variables en forma de tree
    #_rec_name = "nombre"


    atleta = fields.Many2one('berp.socio',string="Socio")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    marca = fields.Float(string="Marca")


    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''