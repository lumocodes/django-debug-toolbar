from django.contrib import admin
from django.contrib.auth.views import LoginView
try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path
try:
    from django.urls import include
except ImportError:
    from django.conf.urls import include

import debug_toolbar

from . import views
from .models import NonAsciiRepr

urlpatterns = [
    re_path(
        r"^resolving1/(.+)/(.+)/$", views.resolving_view, name="positional-resolving"
    ),
    re_path(r"^resolving2/(?P<arg1>.+)/(?P<arg2>.+)/$", views.resolving_view),
    re_path(r"^resolving3/(.+)/$", views.resolving_view, {"arg2": "default"}),
    re_path(r"^regular/(?P<title>.*)/$", views.regular_view),
    re_path(r"^template_response/(?P<title>.*)/$", views.template_response_view),
    re_path(r"^regular_jinja/(?P<title>.*)/$", views.regular_jinjia_view),
    re_path("^non_ascii_request/$", views.regular_view, {"title": NonAsciiRepr()}),
    re_path("^new_user/$", views.new_user),
    re_path("^execute_sql/$", views.execute_sql),
    re_path("^cached_view/$", views.cached_view),
    re_path("^json_view/$", views.json_view),
    re_path("^redirect/$", views.redirect_view),
    re_path("^login_without_redirect/$", LoginView.as_view(redirect_field_name=None)),
    re_path("^admin/", admin.site.urls),
    re_path("^__debug__/", include(debug_toolbar.urls)),
]
