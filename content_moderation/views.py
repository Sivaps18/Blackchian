from rest_framework import viewsets
from .models import ContentModerationAction
from .serializers import ContentModerationActionSerializer

class ContentModerationActionViewSet(viewsets.ModelViewSet):
    queryset = ContentModerationAction.objects.all()
    serializer_class = ContentModerationActionSerializer

    # Example: Add automated flagging or review methods here
