from rest_framework.views import APIView
from rest_framework.response import Response


class InviteUserList(APIView):
    def get(self, request, format=None):
        invite_users = request.user.main.prefetch_related('invite_user').all()
        data = {request.user.phone: [invite_obj.invite_user.phone for invite_obj in invite_users]}

        return Response(data)
