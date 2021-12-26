from rest_framework import generics
from rest_framework.response import Response


class MyView(generics.ListAPIView):
    """
    This View is a proof that the access token generated with drf-social-oauth2 works.
    Try firing a request to http:127.0.0.1:8000/read with and without the token.
    """
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.'
        }
        return Response(response, status=200)
