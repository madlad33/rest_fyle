from .models import Branches, Banks
from rest_framework import viewsets, mixins, status
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .serializers import BranchSerializer, BankSerialzier
from rest_framework import filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class LargeResultsSetPagination(PageNumberPagination):
    """Pagination Controls"""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class BranchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, LimitOffsetPagination):
    """Main view for searching and to get respective branches by 'autocomplete' query parameter"""
    serializer_class = BranchSerializer
    queryset = Branches.objects.all()
    http_method_names = ['get']
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'district', 'state', 'ifsc', 'address']
    renderer_classes = [JSONRenderer]

    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.query_params.get('autocomplete'):
            branch = self.request.query_params.get('autocomplete', None)
            self.limit_query_param = 'limit'
            self.offset_query_param = 'offset'
            return Branches.objects.filter(branch__iexact=branch).order_by('ifsc')
        else:
            self.limit_query_param = 'limit'
            self.offset_query_param = 'offset'
            return Branches.objects.all()


class BankBranchView(APIView,LimitOffsetPagination):
    """View to fetch data for our frontend table"""
    renderer_classes = [JSONRenderer]
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        branches = Branches.objects.select_related("bank_id").values("ifsc", "bank_id__name",
                                                                     "branch", "address",
                                                                     "city", "district",
                                                                     "state", "bank_id")
        if not branches:
            raise NotFound('No branch found for provided Bank and City.')

        data = [{
            "ifsc": branch["ifsc"],
            "bank": branch["bank_id__name"],
            "branch": branch["branch"],
            "address": branch["address"],
            "city": branch["city"],
            "district": branch["district"],
            "state": branch["state"],
            "bank_id": branch["bank_id"]
        } for branch in branches]

        return Response(data)
