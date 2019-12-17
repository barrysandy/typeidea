from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm

from config.custom_site import custom_site
from config.base_admin import BaseOwnerAdmin


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'create_time')
    fields = ('name', 'status', 'is_nav')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'create_time')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户的分类"""

    title = '分类过滤器'
    parameter_name = 'owner_category'   # 查询时URL参数的名字

    """lookups：返回要展示的内容和查询用的id（就是上面Query用的）"""
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    """queryset：根据URL Query的内容返回列表数据"""
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


# @admin.register(Post)
@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    exclude = ('owner', )
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     # 'tag',
    # )

    fieldsets = (
        ('基础配置', {
           'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            # 'classes': ('collapse', ),
            # 'classes': ('wide', ),
            'fields': (
                'desc',
                'content',
            ),
        })
        # ,
        # ('额外信息', {
        #     'classes': ('collapse', ),
        #     'fields': ('content', ),
        # })
    )

    list_display = [
        'title', 'desc', 'category', 'status', 'owner',
        'create_time', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    list_filter = [CategoryOwnerFilter]

    search_fields = ['title', 'category__name']

    actions_on_top = True
    # actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # def operator(self, obj):
    #     return format_html(
    #         '<a href="{}">编辑</a>',
    #         reverse('admin:blog_post_change', args=(obj.id, ))
    #     )
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id, ))
        )
    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    # 自定义静态资源引入
    # class Media:
    #     css = {
    #         'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta/css/bootstrap.min.css', ),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user',
                    'change_message']

