# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools, exceptions, _
from odoo.modules import get_module_resource
import base64
import logging

_logger = logging.getLogger(__name__)

class berp_solicitud_escuela(models.Model):
    _name = 'berp.solicitud_escuela'
    _description = 'berp_solicitud_escuela'

    @api.model
    def _get_default_image(self,aa,bb,cc):
        image = False
        img_path = get_module_resource('berp_usuarios', 'static/src/img', 'avatar.png')
        if img_path:
            with open(img_path, 'rb') as f:
                image = f.read()
        if image:
            image = tools.image_colorize(image)
        return tools.image_resize_image_big(base64.b64encode(image))

    # Datos atleta escuela
    imagen                  = fields.Binary("Imagen", attachment=True, default=lambda self:self._get_default_image('a','b','c'))
    nombre                  = fields.Char(string='Nombre')
    apellido1               = fields.Char(string='Primer Apellido')
    apellido2               = fields.Char(string='Segon Apellido')
    fecha_nacimiento        = fields.Date(string='Fecha de Nacimiento')
    dni                     = fields.Char(string='DNI')
    direccion               = fields.Char(string='Dirección')
    poblacion               = fields.Char(string='Población')
    cp                      = fields.Char(string='Codigo Postal')

    # Datos familiar1
    nombre_1                = fields.Char(string='Nombre y Apellidos')
    mail_1                  = fields.Char(string='Correo electronico')
    telefono_1              = fields.Char(string='Nº Teléfono /Movil')
    dni_1                   = fields.Char(string='DNI')

    # Datos familiar2
    nombre_2                = fields.Char(string='Nombre y Apellidos')
    mail_2                  = fields.Char(string='Correo electronico')
    telefono_2              = fields.Char(string='Nº Teléfono /Movil')
    dni_2                   = fields.Char(string='DNI')

    #Otros datos
    telefono_alternativo    = fields.Char(string='Nº Teléfono /Movil Alternativo')
    cat_salut_atleta        = fields.Char(string='Numero CatSalut')
    salut                   = fields.Text(string='Salut')
    otros                   = fields.Text(string='Otros')
    