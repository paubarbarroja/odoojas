from odoo import http


class berp_website_inici(http.Controller):

    @http.route('/inicio', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200627_2046_website",{})
        

class berp_website_formulari_soci(http.Controller):

    @http.route('/formulari_soci', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20191103_1522_website",{})
        

class berp_website_informacio_soci(http.Controller):

    @http.route('/informacio_soci', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200625_1449_website",{})


class berp_website_escola_atletisme(http.Controller):
    @http.route('/escola_atletisme', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1414_website",{})


class berp_website_grups_entrenament(http.Controller):
    @http.route('/grups_entrenament', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1623_website",{})


class berp_website_butlleti(http.Controller):
    @http.route('/butlleti', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1624_website",{})


class berp_website_ranquing_records(http.Controller):
    @http.route('/ranquing_records', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1625_website",{})


class berp_website_historia(http.Controller):
    @http.route('/historia', auth='user', website=True)
    def index(self, **kw):
        return http.request.render("berp_website.berp_20200524_1626_website",{})