from django.shortcuts import render, get_object_or_404
from .models import Category, Faq_QA, User, IpModel
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import DetailView


def base(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_keywords_faq = Q(
            Q(translations__question_Title__icontains=q) |
            # Q(translations__question_Description__icontains=q) |
            Q(translations__SEO_Keywords__icontains=q)
        )
        search_key_faq = Faq_QA.objects.filter(multiple_keywords_faq).order_by('-id')
    else:
        category_filter = request.GET.get('categories')
        if category_filter:
            search_key_faq = Faq_QA.objects.filter(translations__category_Option=category_filter).order_by('-id')
        else:
            search_key_faq = Faq_QA.objects.all().order_by('-id').order_by('-id')
    paginator = Paginator(search_key_faq, 5)
    page_num = request.GET.get('page', 1)
    search_key_faq = paginator.page(page_num)

    # ip = get_ip(request)
    # u = User(user=ip)
    # result = User.objects.filter(Q(user__icontains=ip))
    # if len(result) == 1:
    #     pass
    # elif len(result) > 1:
    #     pass
    # else:
    #     u.save()
    # counts = Faq_QA.objects.all().count()
    # print("Total question Counts :", counts)
    context = {
        'search_data': search_key_faq,
        'category_data': Category.objects.all(),
        # 'view_counts': counts,
        'search_params': request.GET.get('q'),
        'category_params': request.GET.get('categories')
    }
    return render(request, 'Base.html', context)


# IP Address
def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
        print("IP Address :", ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print("IP Address :", ip)
    return ip


class faq_view(DetailView):
    model = Faq_QA
    pk_url_kwarg = 'pk'
    template_name = 'faq-detail.html'
    context_object_name = 'faqs'

    def __get__(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_ip(request)
        print("New Faq_Ip Address :", ip)
        if IpModel.objects.filter(ip=ip).exits():
            print("Already is there IP in DB")
            faq_id = request.GET.get('faq_viewer_id')
            print("The Page per Visits :", faq_id)
            faq = Faq_QA.objects.get(pk=faq_id)
            faq.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            faq_id = request.GET.get('faq_viewer_id')
            print("The Page per Visits :", faq_id)
            faq = Faq_QA.objects.get(pk=faq_id)
            faq.views.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)
