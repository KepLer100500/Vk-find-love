from .extAdminPanel import *
from .models import *


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateGroups)
admin.site.register(Search)
