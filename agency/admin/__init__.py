from django.contrib import admin

from agency.sites import customer_admin_site
from agency.models import Agency, Tag, Travel
from agency.admin.superuser import AgencyAdmin, TagAdmin, TravelAdmin
from agency.admin.customer import AgencyCustomerAdmin, TravelCustomerAdmin


customer_admin_site.register(Agency, AgencyCustomerAdmin)
customer_admin_site.register(Travel, TravelCustomerAdmin)

admin.site.register(Tag, TagAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Travel, TravelAdmin)
