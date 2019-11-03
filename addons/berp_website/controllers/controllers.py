from odoo import http


class berp_website(http.Controller):
    @http.route('/form_add_socio', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20191103_1522_website",{})