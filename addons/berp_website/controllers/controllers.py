from odoo import http


class berp_website_formulari_soci(http.Controller):

    @http.route('/formulari_soci', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20191103_1522_website",{})


class berp_website_escola_atletisme(http.Controller):
    @http.route('/escola_atletisme', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1414_website",{})