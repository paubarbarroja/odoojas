# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    @api.onchange('fecha_nac')
    def get_categoria(self):
        for record in self:
            if record.fecha_nac:
                categoria = ""
                hoy = date.today()
                fecha_hoy = hoy.strftime('%Y-%m-%d').split('-')
                fecha = "31-12-" + fecha_hoy[0]
                date_object = datetime.strptime(fecha, '%d-%m-%Y').date()
                diferencia = date_object - record.fecha_nac
                edad_final_temporada = str(int(diferencia.days / 365))
                edad = int(edad_final_temporada)

                if edad > 34:
                    record.categoria = "Master"
                else:
                    if edad > 22:
                        record.categoria = "Senior"
                    else:
                        if edad > 19:
                            record.categoria = "Sub 23"
                        else:
                            if edad > 17:
                                record.categoria = "Sub 20"
                            else:
                                if edad > 15:
                                    record.categoria = "Sub 18"
                                else:
                                    if edad > 13:
                                        record.categoria = "Sub 16"





    #************************************************** -- --  COLUMNAS  -- -- **************************************************
    # USUARIO

    user_id = fields.Many2one('res.users', string='Usuario', help='The internal user in charge of this contact.', domain="[('active', '=', True)]",)
    fecha_nac = fields.Date(string="Fecha de Nacimiento")
    dni = fields.Char(string="DNI")
    is_socio = fields.Boolean(string="Socio")
    is_atleta = fields.Boolean(string="Atleta")

    # SOCIO
    num_socio = fields.Integer(string="Numero de Socio")
    fecha_alta = fields.Date(string="Fecha de Alta", required=True, default=fields.Date.context_today)
    fecha_baja = fields.Date(string="Fecha de Baja")
    socio_honorario = fields.Boolean(string="Honorario")

    # ATLETA
    genero = fields.Selection([('1', 'Masculino'), ('2', 'Femenino')], string='Sexo')
    especialidad = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
    ficha = fields.Char(string="Ficha")
    categoria = fields.Char(string="Categoria")
    grupo_entreno = fields.Many2one('berp.grupo_entreno',string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno",string="visible",default=False)