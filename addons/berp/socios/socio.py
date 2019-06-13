# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class berp_socio(models.Model):
    _name = "berp.socio"
    _rec_name = "nombre"

    @api.multi
    def _comprobar_grupo_entreno(self):
        for record in self:
            record.visible = True


    nombre = fields.Char(string="Nombre")
    tipo = fields.Many2many('berp.categoria',string="Tipo")
    correo = fields.Char(string="Correo-e")
    telefono = fields.Char(string="Teléfono")
    especialidad = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
    nacionalidad = fields.Many2one('res.country',string="Nacionalidad")
    dni = fields.Char(string="DNI")
    ficha = fields.Char(string="Ficha")
    genero = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='Sexo')
    fecha_nac = fields.Date(string="Fecha de Nacimiento")
    direccion = fields.Char(string="Dirección")
    cuenta_banc = fields.Char(string="Cuenta Bancaria")
    nombre_cont = fields.Char(string="Contacto de Emergencia")
    telef_cont = fields.Char(string="Teléfono de Emergencia")
    imagen = fields.Binary('Imagen')
    grupo_entreno = fields.Many2one('berp.grupo_entreno',string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno",string="visible",default=False)
    user = fields.Many2one('res.users',string="Usuario")

#todo poner pais por defecto españa y luego mas a delante crear nueva clase para clubes que puede ser res.company hay que mirarselo

# todo poner en el page de informacion del atleta en la vista poner un tree de sus mejores marcas y alguna cosa mas de información sobre el atleta... (mirar si es convincente)

# todo Mirar de poner la categoria en el socio ya que es informacion del atleta, ponerlo en la pagina del atleta y asi sera mas facil cojer la categoria del mismo.