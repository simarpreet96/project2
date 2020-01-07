from django.contrib import admin, messages
from .models import Article, Details, Country, City
from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin
from inline_actions.actions import DefaultActionsMixin, ViewAction
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

class UnPublishActionsMixin(object):
    def get_inline_actions(self, request, obj=None):
        actions= super(UnPublishActionsMixin, self).get_inline_actions(request, obj)
        if obj:
            if obj.status==Article.DRAFT:
                actions.append('publish')
            elif obj.status==Article.PUBLISHED:
                actions.append('unpublish')
            return actions

    def publish(self, request, obj, parent_obj=None):
        obj.status=Article.PUBLISHED
        obj.save()
        messages.info(request,_("Article published."))
    publish.short_description=_("publish")

    def unpublish(self, request, obj, parent_obj=None):
        obj.status=Article.DRAFT
        obj.save()
        messages.info(request,_("Article unpublished."))
    unpublish.short_description=_("Unpublish")


@admin.register(Article)
class ArticleAdmin(UnPublishActionsMixin, 
                    ViewAction, InlineActionsModelAdminMixin,
                    admin.ModelAdmin):           
    list_display=('title','status','author')

class DetailsAdmin(admin.ModelAdmin):
    list_display = ['name','email']

admin.site.register(Details,DetailsAdmin)

admin.site.register(Country)

admin.site.register(City)
