# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
import logging
_logger = logging.getLogger(__name__)

class berp_prueba(models.Model):
    _name = "berp.prueba"
    _rec_name = "nombre"




    nombre = fields.Char(string="Nombre")
    genero = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='Genero')
    especialidad = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
