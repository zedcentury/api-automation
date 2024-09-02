# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.api import call_kw


class APIAutomation(http.Controller):
    @http.route('/api-automation', auth='public', methods=['POST', 'OPTIONS'], type='json', csrf=False, cors='*')
    def api_automation(self, **post):
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

    @http.route('/api-automation/<string:api_endpoint>', auth='public', methods=['GET', 'OPTIONS'], type='json')
    def api_endpoint(self, api_endpoint, **post):
        try:
            user = http.request.env["token.authentication"].get_user() or http.request.env.user
        except Exception as e:
            print(e)
            user = http.request.env.user

        api_automation = http.request.env["api.automation"].sudo().search([("api_endpoint", "=", api_endpoint)], limit=1)
        if not api_automation:
            return {"error": "API endpoint not found"}

        model = api_automation.model_id.model
        method = api_automation.method
        args = json.loads(api_automation.args)
        kwargs = json.loads(api_automation.kwargs)

        return call_kw(http.request.env[model].with_user(user=user), method, args, kwargs)
