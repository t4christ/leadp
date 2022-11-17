# from django.utils.timezone import now

# class SetLastVisitMiddleware(object):
#     def process_response(self, request, response):
#         if request.user.is_authenticated():
#             # Update last visit time after request finished processing.
#             User.objects.filter(pk=request.user.pk).update(last_visit=now())
#         return response