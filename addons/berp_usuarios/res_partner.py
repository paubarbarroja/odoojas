# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"


    is_socio = fields.Boolean(string="Socio")
    is_atleta = fields.Boolean(string="Atleta")
    fecha_nac = fields.Date(string="Fecha de Nacimiento", required=True)
    dni = fields.Char(string="DNI", required=True)

    # socio
    fecha_alta = fields.Date(string="Fecha de Alta", required=True, default=fields.Date.context_today)
    fecha_baja = fields.Date(string="Fecha de Baja")
    socio_honorario = fields.Boolean(string="Honorario")

    # atleta
    genero = fields.Selection([('1', 'Masculino'), ('2', 'Femenino')], string='Sexo', required=True)
    especialidad = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
    ficha = fields.Char(string="Ficha")
    categoria = fields.Char(string="Categoria")
    grupo_entreno = fields.Many2one('berp.grupo_entreno',string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno",string="visible",default=False)