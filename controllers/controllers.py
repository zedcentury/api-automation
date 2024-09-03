# -*- coding: utf-8 -*-
import ast

from odoo import http
from odoo.api import call_kw


class APIAutomation(http.Controller):
    @http.route('/api-automation/v1', auth='public', methods=['POST', 'OPTIONS'], type='json', csrf=False, cors='*')
    def api_automation_v1(self, **post):
        try:
            user = http.request.env["token.authentication"].get_user() or http.request.env.user
        except Exception as e:
            print(e)
            user = http.request.env.user

        model = post.get('model')
        method = post.get('method')
        args = post.get('args', [])
        kwargs = post.get('kwargs', {})

        return call_kw(http.request.env[model].with_user(user=user), method, args, kwargs)

    @http.route('/api-automation/v2', auth='public', methods=['POST', 'OPTIONS'], type='json', csrf=False, cors='*')
    def api_automation_v2(self, **post):
        try:
            user = http.request.env["token.authentication"].get_user() or http.request.env.user
        except Exception as e:
            print(e)
            user = http.request.env.user

        path = post.get('path')
        if not path:
            return {"error": "Path not provided"}

        api_automation = http.request.env["api.endpoint"].sudo().search([("path", "=", path)], limit=1)
        if not api_automation:
            return {"error": "API endpoint not found"}

        model = api_automation.model
        method = api_automation.method
        args = ast.literal_eval(api_automation.args)
        kwargs = ast.literal_eval(api_automation.kwargs)

        return call_kw(http.request.env[model].with_user(user=user), method, args, kwargs)
