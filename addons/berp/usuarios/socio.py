# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


# todo HERENCIAR CLASE Y VISTA DE RES_USER PARA PONER CAMPO MANY2ONE A BERP.SOCIO.

class berp_socio(models.Model):
    _name = "berp.socio"
    _rec_name = "nombre"

    @api.multi
    def _comprobar_grupo_entreno(self):
        for record in self:
            if record.user == self.env.uid:
                for atletas in record.grupo_entreno.atletas:
                    atletas.visible = True

    @api.model
    def create(self, values):
        categoria = ""
        nacimiento = datetime.strptime(values['fecha_nac'], '%Y-%m-%d').date()
        hoy = date.today()
        fecha_hoy = hoy.strftime('%Y-%m-%d').split('-')
        fecha = "31-12-" + fecha_hoy[0]
        date_object = datetime.strptime(fecha, '%d-%m-%Y').date()
        diferencia = date_object - nacimiento
        edad_final_temporada = str(int(diferencia.days / 365))
        edad = int(edad_final_temporada)

        if edad > 34:
            categoria = "Master"
        else:
            if edad > 22:
                categoria = "Senior"
            else:
                if edad > 19:
                    categoria = "Sub 23"
                else:
                    if edad > 17:
                        categoria = "Sub 20"
                    else:
                        if edad > 15:
                            categoria = "Sub 18"
                        else:
                            if edad > 13:
                                categoria = "Sub 16"

        values.update({'categoria': categoria})
        res = super(berp_socio, self).create(values)
        return res

    nombre = fields.Char(string="Nombre", required=True)
    correo = fields.Char(string="Correo-e", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    nacionalidad = fields.Many2one('res.country', string="Nacionalidad", default=68, required=True)
    dni = fields.Char(string="DNI", required=True)
    genero = fields.Selection([('1', 'Masculino'), ('2', 'Femenino')], string='Sexo', required=True)
    fecha_nac = fields.Date(string="Fecha de Nacimiento", required=True)
    fecha_alta = fields.Date(string="Fecha de Alta", required=True, default=fields.Date.context_today)
    fecha_baja = fields.Date(string="Fecha de Baja")
    direccion = fields.Char(string="Dirección")
    titular_cc = fields.Char(string="Titular Cuenta Bancaria")
    cuenta_banc = fields.Char(string="Cuenta Bancaria", required=True)
    nombre_cont = fields.Char(string="Contacto de Emergencia")
    telef_cont = fields.Char(string="Teléfono de Emergencia")
    imagen = fields.Binary('Imagen')
    grupo_entreno = fields.Many2one('berp.grupo_entreno', string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno", string="visible", default=False)
    user = fields.Many2one('res.users', string="Usuario")
    especialidad = fields.Selection(
        [('1', 'Velocidad'), ('2', 'Fondo'), ('3', 'Medio Fondo'), ('4', 'Lanzamientos'), ('5', 'Saltos'),
         ('6', 'Marcha Atlética')], string='Especialidad')
    ficha = fields.Char(string="Ficha")
    categoria = fields.Char(string="Categoria")
    grupo_entreno = fields.Many2one('berp.grupo_entreno', string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno", string="visible", default=False)

#todo crear nueva clase para clubes que puede ser res.company hay que mirarselo


