from django.urls import re_path, include
from django.contrib import admin

import nexus

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^nexus/', include(nexus.site.urls)),
]
