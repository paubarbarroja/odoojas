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
    def _get_default_image(self):
        image = False
        img_path = get_module_resource('berp_usuarios', 'static/src/img', 'avatar.png')
        if img_path:
            with open(img_path, 'rb') as f:
                image = f.read()
        if image:
            image = tools.image_colorize(image)
        return tools.image_resize_image_big(base64.b64encode(image))

    # Datos atleta escuela
    imagen                  = fields.Binary("Imagen", attachment=True, default=lambda self:self._get_default_image())
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
    grupo_entreno = fields.Selection(string='Grup entrenament', selection=[ ('1', 'Pre-Benjamins Sub8 (anys 2014-2015) dimarts i dijous 18:00h-19:30h'),
                                                                            ('2', 'Benjamins Sub10 (anys 2012-2013) dilluns i dimecres 18:00h-19:30h'),
                                                                            ('3', 'Benjamins Sub10 (anys 2012-2013) dimarts i dijous 18:00h-19:30h'),
                                                                            ('4', 'Alevins Sub12 (anys 2010-2011) dilluns i dimecres 18:00h-19:30h'),
                                                                            ('5', 'Alevins Sub12 (anys 2010-2011) dimarts i dijous 18:00h-19:30h'),
                                                                            ('6', 'Infantils Sub14 (anys 2008-2009) dilluns, dimecres i divendres 18:00h-19:30h'),
                                                                            ('7', 'Infantils Sub14 (anys 2008-2009) dimarts, dijous i divendres 18:00h-19:30h'),
                                                                            ('8', 'Cadets Sub16 (anys 2006-2007) dilluns, dimecres i divendres 18:00h-19:30h'),
                                                                            ('9', 'Juvenils Sub18 (anys 2004-2005) dilluns, dimecres i divendres 18:00h-19:30h'),])
    
    telefono_alternativo    = fields.Char(string='Nº Teléfono /Movil Alternativo')
    cat_salut_atleta        = fields.Char(string='Numero CatSalut')
    salut                   = fields.Text(string='Salut')
    otros                   = fields.Text(string='Otros')
    cuenta_bancaria         = fields.Char(string='Cuenta bancaria')
    