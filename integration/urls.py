from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r"^cms/api/v1/", include("bulbs.api.urls")),  # noqa

    url(r"^save$", "integration.core.views.save"),
    url(r"^rollback$", "integration.core.views.save")
)
