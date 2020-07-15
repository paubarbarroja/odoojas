# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_solicitud_escuela(models.TransientModel):
    _name = 'berp.solicitud_escuela'
    _description = 'berp_solicitud_escuela'


    # Datos atleta escuela
    nombre = fields.Char(string='Nom')
    apellido1 = fields.Char(string='Primer Cognom')
    apellido2 = fields.Char(string='Segon Cognom')
    fecha_nacimiento = fields.Date(string='Data de Naixement')
    dni = fields.Char(string='DNI')
    direccion = fields.Char(string='Adreça')
    poblacion = fields.Char(string='Població')
    cp = fields.Char(string='Codi Postal')

    # Datos familiares
    nombre_1 = fields.Char(string='Nom i Cognoms')
    mail_1 = fields.Char(string='Correu electronic ')
    telefono_1 = fields.Char(string='Nº Telèfon /Movil')
    dni_1 = fields.Char(string='DNI')
    
    nombre_2 = fields.Char(string='Nom i Cognoms')
    mail_2 = fields.Char(string='Correu electronic')
    telefono_2 = fields.Char(string='Nº Telèfon /Movil')
    dni_2 = fields.Char(string='DNI')

    telefono_alternativo = fields.Char(string='Nº Telèfon /Movil Alternatiu')
    cat_salut_atleta = fields.Char(string='Numero CatSalut')
    salut = fields.Text(string='Salut')