from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Category, Product


class LeafCategoryFilter(SimpleListFilter):
    """Filter to show only leaf categories."""
    title = 'Is Leaf'
    parameter_name = 'is_leaf'

    def lookups(self, _, __):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, _, queryset):
        if self.value() == 'yes':
            return queryset.filter(children__isnull=True)
        elif self.value() == 'no':
            return queryset.filter(children__isnull=False)
        return queryset


class RootCategoryFilter(SimpleListFilter):
    """Filter to show only root categories."""
    title = 'Is Root'
    parameter_name = 'is_root'

    def lookups(self, _, __):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, _, queryset):
        if self.value() == 'yes':
            return queryset.filter(parent__isnull=True)
        elif self.value() == 'no':
            return queryset.filter(parent__isnull=False)
        return queryset



admin.site.register([Product])



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_breadcrumb')
    list_filter = (LeafCategoryFilter, RootCategoryFilter)

