# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_models_ext import BaseModelMixin


class OnerrorReportInfo(BaseModelMixin):
    lineNo = models.IntegerField(_(u'lineNo'), default=0, help_text=u'异常行号')
    columnNo = models.IntegerField(_(u'columnNo'), default=0, help_text=u'异常列号')
    scriptURI = models.CharField(_(u'scriptURI'), max_length=255, blank=True, null=True, help_text=u'异常文件路径')
    errorMessage = models.CharField(_(u'errorMessage'), max_length=255, blank=True, null=True, help_text=u'异常信息')
    stack = models.TextField(_(u'stack'), blank=True, null=True, help_text=u'异常堆栈信息')

    class Meta:
        verbose_name = _(u'onerrorreportinfo')
        verbose_name_plural = _(u'onerrorreportinfo')

    def __unicode__(self):
        return unicode(self.pk)
