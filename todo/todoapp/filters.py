from django_filters import rest_framework as filters, DateFromToRangeFilter

from todoapp.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(filters.FilterSet):
    create = DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['project', 'create']
