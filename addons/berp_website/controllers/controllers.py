from odoo import http


class berp_website(http.Controller):
    @http.route('/inicio', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_02102019_2300_website",{})