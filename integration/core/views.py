from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def save(request):
	sid = transaction.savepoint()
	return JsonResponse({"sid": sid})


@csrf_exempt
def rollback(request):
	sid = request.POST.get("sid")
	transaction.savepoint_rollback(sid)
	return JsonResponse({"status": "success"})