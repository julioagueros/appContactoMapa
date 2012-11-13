from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from contactos.models import User


class UserView(object):
    model = User

    def get_template_names(self):
        """Nest templates within user directory."""
        tpl = super(UserView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'user'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class UserDateView(UserView):
    date_field = 'created_at'
    month_format = '%m'


class UserBaseListView(UserView):
    paginate_by = 10


class UserArchiveIndexView(
    UserDateView, UserBaseListView, ArchiveIndexView):
    pass


class UserCreateView(UserView, CreateView):
    pass


class UserDateDetailView(UserDateView, DateDetailView):
    pass


class UserDayArchiveView(
    UserDateView, UserBaseListView, DayArchiveView):
    pass


class UserDeleteView(UserView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('contactos_user_list')


class UserDetailView(UserView, DetailView):
    pass


class UserListView(UserBaseListView, ListView):
    pass


class UserMonthArchiveView(
    UserDateView, UserBaseListView, MonthArchiveView):
    pass


class UserTodayArchiveView(
    UserDateView, UserBaseListView, TodayArchiveView):
    pass


class UserUpdateView(UserView, UpdateView):
    pass


class UserWeekArchiveView(
    UserDateView, UserBaseListView, WeekArchiveView):
    pass


class UserYearArchiveView(
    UserDateView, UserBaseListView, YearArchiveView):
    make_object_list = True



