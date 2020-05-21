# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools, exceptions, _
import logging
from odoo.modules import get_module_resource
import base64
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"
    _order = "apellido1, apellido2, name asc"

    @api.model
    def _get_categoria(self, fecha_nac):
        if isinstance(fecha_nac,str):
            nacimiento = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
        else:
            nacimiento = fecha_nac
        hoy = date.today()
        fecha_hoy = hoy.strftime('%Y-%m-%d').split('-')
        fecha = "31-12-" + fecha_hoy[0]
        date_object = datetime.strptime(fecha, '%d-%m-%Y').date()
        diferencia = date_object - nacimiento
        edad_final_temporada = str(int(diferencia.days / 365))
        edad = int(edad_final_temporada)

        categoria = ""
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
                            else:
                                if edad > 11:
                                    categoria = "Sub 14"
                                else:
                                    if edad > 9:
                                        categoria = "Sub 12"
                                    else:
                                        if edad > 7:
                                            categoria = "Sub 10"
                                        else:
                                            categoria = "Sub 8"

        return categoria


    @api.model
    def create(self, values):
        res = False
        if values['is_socio'] and values['is_atleta']:
            if values['is_socio'] == False and values['is_atleta'] == False:
                raise exceptions.except_orm(_('Error!!'), _('Indica en el formulario si es atleta, socio o ambas'))
            else:
                if values['is_socio']:
                    values['num_socio'] = self.env['ir.sequence'].next_by_code('res_partner.num_socio')
                res = super(Partner, self).create(values)
                categoria = ""
                if 'fecha_nac' in values:
                    if not isinstance(values['fecha_nac'],bool):
                        categoria = self._get_categoria(values['fecha_nac'])
                res.categoria = categoria
        else:
            res = super(Partner, self).create(values)
        return res


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
                categoria = self._get_categoria(record.fecha_nac)
                record.categoria = categoria


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


    @api.multi
    def funcion_categoria_cron(self):
        items = self.search([])
        for item in items:
            if item.fecha_nac:
                categoria = self._get_categoria(item.fecha_nac)
                item.write({'categoria' : categoria})


    @api.multi
    def funcion_categoria(self):
        items = self.search([])
        for item in items:
            if item.ficha:
                item.write({'is_atleta': True})



    #************************************************** -- --  COLUMNAS  -- -- **************************************************
    not_jas                 = fields.Boolean('Not Jas')
    # USUARIO
    image                   = fields.Binary("Image", attachment=True, default=lambda self:self._get_default_image('a','b','c'))
    name                    = fields.Char(string="Nombre")
    apellido1               = fields.Char(string="Apellido 1")
    apellido2               = fields.Char(string="Apellido 2")
    usuario_name            = fields.Char(compute="_get_name", string="Nombre Completo",store=True)
    usuario_name_tree       = fields.Char(compute="_get_name_tree", string="Nombre Completo",store=True)
    user_id                 = fields.Many2one('res.users', string='Usuario', help='The internal user in charge of this contact.', domain="[('active', '=', True)]",)
    fecha_nac               = fields.Date(string="Fecha de Nacimiento")
    dni                     = fields.Char(string="DNI")
    is_socio                = fields.Boolean(string="Socio")
    is_atleta               = fields.Boolean(string="Atleta")
    cuenta_bancaria         = fields.Char(string="Cuenta Bancaria")
    notas                   = fields.Text(string="Notas")

    # SOCIO
    num_socio               = fields.Integer(string="Numero de Socio")
    fecha_alta              = fields.Date(string="Fecha de Alta", default=fields.Date.context_today)
    fecha_baja              = fields.Date(string="Fecha de Baja")
    socio_honorario         = fields.Boolean(string="Honorario")
    descuento               = fields.Selection([('25', '+25 años'),('50', '+50 años'),('3f', '+3 Familiar'),('bayunt', 'Beca Ayuntamiento'),('bclub', 'Beca Club')],string="Descuento")
    descuento_tipo          = fields.Char(string="Tipo descuento")
    socio_protector         = fields.Boolean(string="Socio Protector")
    dinero_socio            = fields.Float(string="¿ Cuanto paga el socio ?")

    # ATLETA
    genero                  = fields.Selection([('1', 'Masculino'), ('2', 'Femenino')], string='Sexo')
    especialidad            = fields.Selection([('1', 'Velocidad'),('2', 'Fondo'),('3', 'Medio Fondo'),('4', 'Lanzamientos'),('5', 'Saltos'),('6', 'Marcha Atlética')],string='Especialidad')
    ficha                   = fields.Char(string="N.º Licencia")
    categoria               = fields.Char(string="Categoria")
    grupo_entreno           = fields.Many2one('berp.grupo_entreno',string="Grupo Entreno")
    visible                 = fields.Boolean(compute="_comprobar_grupo_entreno",string="visible",default=False)
    tipo_ficha              = fields.Selection([('esp', 'Ficha Española'), ('cat', 'Ficha Catalana'), ('fondo', 'Ficha Fondo y Ruta')], string='Tipo de Ficha')
