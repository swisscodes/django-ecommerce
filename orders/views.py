from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.http import HttpResponse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

# import weasyprint


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:  # this works because of __iter__ in cart.py
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            order_created.delay(order.id)
            request.session["order_id"] = order.id
            context = {"order": order}
            return redirect(reverse("payment:process"))
            # return render(request, "orders/created.html", context)
    else:
        form = OrderCreateForm()
        context = {"cart": cart, "form": form}
        return render(request, "orders/create.html", context)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/detail.html", {"order": order})


# @staff_member_required
# def admin_order_pdf(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     html = render_to_string("orders/order/pdf.html", {"order": order})
#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = f"filename=order_{order.id}.pdf"
#     weasyprint.HTML(string=html).write_pdf(
#         response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "css/pdf.css")]
#     )
#     return response
