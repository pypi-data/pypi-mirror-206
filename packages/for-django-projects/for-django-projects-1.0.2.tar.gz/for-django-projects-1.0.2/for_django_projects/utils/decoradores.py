import re
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from utils.funciones import redirectAfterPostGet


def custom_atomic_request(func):
    from utils.custom_models import FormError
    from utils.funciones_adicionales import salva_logs_request
    import sys
    def validate_request(*args, **kwargs):
        res_json = []
        request = args[0]
        has_except = False
        error_message = ""
        if request.method == "POST":
            action = request.POST.get("action")
            try:
                with transaction.atomic():
                    val_func = func(*args, **kwargs)
            except ValueError as ex:
                res_json.append({'error': True,
                                 "message": str(ex)
                                 })
                val_func = JsonResponse(res_json, safe=False)
                has_except = True
                error_message = str(ex)
            except FormError as ex:
                res_json.append(ex.dict_error)
                val_func = JsonResponse(res_json, safe=False)
                has_except = True
                error_message = "Formulario no válido"
            except IntegrityError as ex:
                has_except = True
                msg = str(ex)
                error_message = "Integrity Error"
                for key in settings.CONSTRAINT_MSG_KEYS:
                    if re.search(f"\\b{key}\\b", msg):
                        error_message = settings.CONSTRAINT_MSG[key]
                res_json.append(
                    {
                        'error': has_except,
                        "message": error_message
                    }
                )
                val_func = JsonResponse(res_json, safe=False)
            except Exception as ex:
                salva_logs_request(request, __file__, request.method,
                                   action, type(ex).__name__,
                                   'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), ex)
                res_json.append({'error': True,
                                 "message": "Intente Nuevamente"
                                 })
                val_func = JsonResponse(res_json, safe=False)
                has_except = True
                error_message = "Intente Nuevamente"
        elif request.method == "GET":
            val_func = func(*args, **kwargs)
        if has_except and not request.is_ajax:
            messages.error(request, error_message)
            val_func = redirect(redirectAfterPostGet(request))
        return val_func

    return validate_request


def public_login_required(func):
    def f(*args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated:
            return redirect("/login/")
        return func(*args, **kwargs)

    return f


def sync_to_async_function(f):
    import threading
    def threading_func(*a, **kw):
        t = threading.Thread(target=f, args=a, kwargs=kw)
        t.start()
        # t.join()

    return threading_func
