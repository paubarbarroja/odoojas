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
    _rec_name = "titulo"

    @api.multi
    def create_usuario_escuela(self):
        for item in self:
            values = {
                'imagen'                : item.imagen,
                'nombre'                : item.nombre,
                'apellido1'             : item.apellido1,
                'apellido2'             : item.apellido2,
                'fecha_nacimiento'      : item.fecha_nacimiento,
                'dni'                   : item.dni,
                'direccion'             : item.direccion,
                'poblacion'             : item.poblacion,
                'cp'                    : item.cp,
                'nombre_1'              : item.nombre_1,
                'mail_1'                : item.mail_1,
                'telefono_1'            : item.telefono_1,
                'dni_1'                 : item.dni_1,
                'nombre_2'              : item.nombre_2,
                'mail_2'                : item.mail_2,
                'telefono_2'            : item.telefono_2,
                'dni_2'                 : item.dni_2,
                'grupo_entreno'         : item.grupo_entreno,
                'telefono_alternativo'  : item.telefono_alternativo,
                'cat_salut_atleta'      : item.cat_salut_atleta,
                'salut'                 : item.salut,
                'otros'                 : item.otros,
                'cuenta_bancaria'       : item.cuenta_bancaria,
                'fecha_ingreso'         : item.fecha_ingreso,
                'comentario'            : item.comentario,
                'contact_google'        : item.contact_google,
                'fecha_aceptar_ingreso' : date.today(),
                'solicitud'             : item.id
            }
            self.env['berp.usuario_escuela'].create(values)
            item.inscrito = True

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

    @api.multi
    def get_titulo(self):
        for item in self:
            if item.nombre != False:
                item.titulo = "SIE - "+item.nombre
            if item.apellido1 != False:
                item.titulo = item.titulo+" "+item.apellido1
            if item.apellido2 != False:
                item.titulo = item.titulo+" "+item.apellido2

    # Datos atleta escuela
    titulo                  = fields.Char(compute='get_titulo',string='Titulo',store=True)
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
    grupo_entreno = fields.Selection(string='Grup entrenament', selection=[ ('1', 'INSCRIPCIONS TANCADES  ---  Pre-Benjamins Sub8 (anys 2014-2015)'),
                                                                            ('2', 'Benjamins Sub10 (anys 2012-2013) dilluns i dimecres 18:00h-19:30h'),
                                                                            ('3', 'INSCRIPCIONS TANCADES  ---  Benjamins Sub10 (anys 2012-2013)'),
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
    fecha_ingreso           = fields.Date(string="Fecha inscripción", default=fields.Date.context_today)
    comentario              = fields.Text(string='Comentario')
    contact_google          = fields.Boolean(string='Contacto Google')
    inscrito                = fields.Boolean(string='Inscrito')
    
    