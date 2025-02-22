from django.contrib import messages

class ClearMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Clear previous messages
        storage = messages.get_messages(request)
        storage.used = True

        response = self.get_response(request)
        return response