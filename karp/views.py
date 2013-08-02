# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.views.generic import TemplateView
import importlib
from django.conf import settings

__author__ = 'tchen'
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'karp/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tools'] = []
        for item in settings.TOOL_SET_APPS:
            m = importlib.import_module("%s" % item)
            context['tools'].append(m.__info__)
        return context

