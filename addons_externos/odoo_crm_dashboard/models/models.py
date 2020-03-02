from odoo import models, fields, api
from odoo.http import request
import datetime


class CRMDashboard(models.Model):
    _name = 'crm.dashboard'
    _description = 'CRM Dashboard'

    name = fields.Char("")

    @api.model
    def get_crm_info(self):    
        uid = request.session.uid
        cr = self.env.cr 
        user_id=self.env['res.users'].browse(uid)
        today_date = datetime.datetime.now().date()
        my_pipeline = self.env['crm.lead'].sudo().search_count([('user_id', '=', uid)])
        tot_overdue_opportunities = self.env['crm.lead'].sudo().search_count([('type', '=', 'opportunity'),('date_deadline', '<', today_date), ('date_closed', '=', False)])
        tot_open_opportunities = self.env['crm.lead'].sudo().search_count([('type', '=', 'opportunity'),('probability', '<', 100)])
        
        tot_won= self.env['crm.lead'].sudo().search_count([('active', '=', True),('probability', '=', 100)])
        tot_lost= self.env['crm.lead'].sudo().search_count([('active', '=', False),('probability', '=', 0)])   
        crm_details = self.env['crm.lead'].sudo().search_read([('user_id', '=', uid)], limit=1)          
        # crm_details = self.env['hr.employee'].sudo().search_read([('user_id', '=', uid)], limit=1)
        
        crm_search_view_id = self.env.ref('crm.view_crm_case_opportunities_filter')
        # timesheet_search_view_id = self.env.ref('hr_timesheet.hr_timesheet_line_search')
        # job_search_view_id = self.env.ref('hr_recruitment.view_crm_case_jobs_filter')
        # attendance_search_view_id = self.env.ref('hr_attendance.hr_attendance_view_filter')
        # expense_search_view_id = self.env.ref('hr_expense.view_hr_expense_sheet_filter')

        # leaves_to_approve = self.env['hr.leave'].sudo().search_count([('state', 'in', ['confirm', 'validate1'])])
        # leaves_alloc_to_approve = self.env['hr.leave.allocation'].sudo().search_count([('state', 'in', ['confirm', 'validate1'])])
        # timesheets = self.env['account.analytic.line'].sudo().search_count(
        #     [('project_id', '!=', False), ])
        # timesheets_self = self.env['account.analytic.line'].sudo().search_count(
        #     [('project_id', '!=', False), ('user_id', '=', uid)])
        # job_applications = self.env['hr.applicant'].sudo().search_count([])
        # attendance_today = self.env['hr.attendance'].sudo().search_count([('check_in', '>=',
        #                     str(datetime.datetime.now().replace(hour=0, minute=0, second=0))),
        #                     ('check_in', '<=', str(datetime.datetime.now().replace(hour=23, minute=59, second=59)))])
        # expenses_to_approve = self.env['hr.expense.sheet'].sudo().search_count([('state', 'in', ['submit'])])


        obj_opr=self.env['crm.lead'].sudo().search([])
        expected_revenue=0
        for lead in obj_opr:
            expected_revenue=round(expected_revenue + (lead.planned_revenue or 0.0) * (lead.probability or 0) / 100.0, 2)
            #payroll Datas for Bar chart
        query = """
           select * from (
                select  to_char(now(), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expected_revenue,1 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '0 month') and ((date_trunc('month', now()) + interval '1 month')- interval '1 day')
                union
                select  to_char((date_trunc('month', now()) + interval '1 month'), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expecte_revenue, 2 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '1 month') and ((date_trunc('month', now()) + interval '2 month')- interval '1 day')
                union
                select  to_char((date_trunc('month', now()) + interval '2 month'), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expected_revenue,3 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '2 month') and ((date_trunc('month', now()) + interval '3 month')- interval '1 day')
                union
                select  to_char((date_trunc('month', now()) + interval '3 month'), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expected_revenue,4 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '3 month') and ((date_trunc('month', now()) + interval '4 month')- interval '1 day')
                union
                select  to_char((date_trunc('month', now()) + interval '4 month'), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expected_revenue,5 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '4 month') and ((date_trunc('month', now()) + interval '5 month')- interval '1 day')
                union
                select  to_char((date_trunc('month', now()) + interval '5 month'), 'MON-YYYY') as Month ,sum((planned_revenue*probability)/100) as expected_revenue,6 as sorting
                from crm_lead where date_deadline 
                between (date_trunc('month', now()) + interval '5 month') and ((date_trunc('month', now()) + interval '6 month')- interval '1 day')
                ) as t order by sorting
        """
        cr.execute(query)
        graph_exp_revenue_data = cr.dictfetchall()
        graph_exp_revenue_label = []
        graph_exp_revenue_dataset = []
        for data in graph_exp_revenue_data:
            graph_exp_revenue_label.append(data['month'])
            graph_exp_revenue_dataset.append(data['expected_revenue'])

       
      
        crm_details=[{}]
        if crm_details:
            #categories = self.env['hr.employee.category'].sudo().search([('id', 'in', crm_details[0]['category_ids'])])
            data = {
                'my_pipe_line': my_pipeline,
                'tot_open_opportunities': tot_open_opportunities,
                'tot_overdue_opportunities': tot_overdue_opportunities,                
                'tot_won': tot_won,
                'tot_lost': tot_lost,
                'expected_revenue':expected_revenue,
                'user_id':user_id.id,
                'graph_exp_revenue_label': graph_exp_revenue_label,
                'graph_exp_revenue_dataset': graph_exp_revenue_dataset,
            }

            crm_details[0].update(data)

            print ("CRM________________",crm_details)
        return crm_details
