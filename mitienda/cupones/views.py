from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Cupon
from .forms import CouponApplyForm
# Create your views here.
@require_POST
def aplicar_cupon(request):
    ahora = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        codigo = form.cleaned_data['codigo']
        try:
            cupon = Cupon.objects.get(codigo=codigo, valido_desde__lte=ahora, valido_hasta__gte=ahora,activo = True)
            request.session['cupon_id'] = cupon.id
        except Cupon.DoesNotExist:
            request.session['cupon_id'] = None
    return redirect('carro:detalle_carro')
