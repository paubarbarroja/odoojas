# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools
import logging
from odoo.modules import get_module_resource
import base64
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"
    _order = "apellido1, apellido2, name asc"

    @api.multi
    @api.depends('apellido1', 'apellido1', 'name')
    def name_get(self):
        result = []
        for item in self:
            s = ""
            if item.apellido1:
                s += item.apellido1
            if item.apellido2:
                s += " " + item.apellido2
            if item.name:
                s += ", " + item.name
            result.append((item.id, s))
        return result

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


    @api.depends('apellido1', 'apellido2', 'name')
    def _get_name(self):
        for item in self:
            s = ""
            if item.name:
                s += " " + item.name
            if item.apellido1:
                s += item.apellido1
            if item.apellido2:
                s += " " + item.apellido2
            item.usuario_name = s

    @api.depends('apellido1', 'apellido2', 'name')
    def _get_name_tree(self):
        for item in self:
            s = ""
            if item.apellido1:
                s += item.apellido1
            if item.apellido2:
                s += " " + item.apellido2
            if item.name:
                s += ", " + item.name
            item.usuario_name_tree = s

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



    #************************************************** -- --  COLUMNAS  -- -- **************************************************
    # USUARIO
    image = fields.Binary("Image", attachment=True, default=lambda self:self._get_default_image('a','b','c'))
    name = fields.Char(string="Nombre")
    apellido1 = fields.Char(string="Apellido 1")
    apellido2 = fields.Char(string="Apellido 2")
    usuario_name = fields.Char(compute="_get_name", string="Nombre Completo",store=True)
    usuario_name_tree = fields.Char(compute="_get_name_tree", string="Nombre Completo",store=True)
    user_id = fields.Many2one('res.users', string='Usuario', help='The internal user in charge of this contact.', domain="[('active', '=', True)]",)
    fecha_nac = fields.Date(string="Fecha de Nacimiento")
    dni = fields.Char(string="DNI")
    is_socio = fields.Boolean(string="Socio")
    is_atleta = fields.Boolean(string="Atleta")
    cuenta_bancaria = fields.Many2one("res.partner.bank",string="Cuenta Bancaria")
    notas = fields.Text(string="Notas")

    # SOCIO
    num_socio = fields.Integer(string="Numero de Socio")
    fecha_alta = fields.Date(string="Fecha de Alta", required=True, default=fields.Date.context_today)
    fecha_baja = fields.Date(string="Fecha de Baja")
    socio_honorario = fields.Boolean(string="Honorario")

    # ATLETA
    genero = fields.Selection([('1', 'Masculino'), ('2', 'Femenino')], string='Sexo')
    especialidad = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
    ficha = fields.Char(string="N.º Licencia")
    categoria = fields.Char(string="Categoria")
    grupo_entreno = fields.Many2one('berp.grupo_entreno',string="Grupo Entreno")
    visible = fields.Boolean(compute="_comprobar_grupo_entreno",string="visible",default=False)
    tipo_ficha = fields.Selection([('esp', 'Ficha Española'), ('cat', 'Ficha Catalana'), ('fondo', 'Ficha Fondo y Ruta')], string='Tipo de Ficha')