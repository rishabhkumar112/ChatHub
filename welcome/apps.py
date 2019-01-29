# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class WelcomeConfig(AppConfig):
    name = 'welcome'

    def ready(self):
        import users.signals
