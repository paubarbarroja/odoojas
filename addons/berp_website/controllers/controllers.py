from odoo import http


class berp_website_formulari_escola(http.Controller):
    @http.route('/formulari_escola', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200716_1254_website",{})


class berp_website_formulari_soci(http.Controller):
    @http.route('/formulari_soci', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20191103_1522_website",{})
        

class berp_website_informacio_soci(http.Controller):
    @http.route('/informacio_soci', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200625_1449_website",{})


class berp_website_escola_atletisme(http.Controller):
    @http.route('/escola_atletisme', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1414_website",{})


class berp_website_grups_entrenament(http.Controller):
    @http.route('/grups_entrenament', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1623_website",{})


class berp_website_butlleti(http.Controller):
    @http.route('/butlleti', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1624_website",{})


class berp_website_ranquing_records(http.Controller):
    @http.route('/ranquing_records', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1625_website",{})


class berp_website_historia(http.Controller):
    @http.route('/historia', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1626_website",{})


class berp_website_politica_privacidad(http.Controller):
    @http.route('/politica_privacidad', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200527_2205_website",{})


class berp_website_aviso_legal(http.Controller):
    @http.route('/aviso_legal', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200527_2212_website",{})


class berp_website_cookies(http.Controller):
    @http.route('/politica_cookies', auth='public', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200527_2230_website",{})