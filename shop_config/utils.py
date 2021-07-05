from django.views.defaults import page_not_found


def shop_404(request, exception):
    template_name = "404.html"
    if request.path.startswith("/shop"):
        template_name = "shop/404.html"
    return page_not_found(request, exception, template_name=template_name)
