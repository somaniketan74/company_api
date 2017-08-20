from company.views import companyView
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^company/$',companyView.as_view())
}

urlpatterns=format_suffix_patterns(urlpatterns)