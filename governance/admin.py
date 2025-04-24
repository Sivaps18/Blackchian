from django.contrib import admin
from .models import GovernanceProposal

@admin.register(GovernanceProposal)
class GovernanceProposalAdmin(admin.ModelAdmin):
    list_display = ('proposal_id', 'submitter', 'proposal_type', 'proposal_status', 'timestamp')
    list_filter = ('proposal_status', 'proposal_type')
    search_fields = ('submitter__username', 'proposal_content')
