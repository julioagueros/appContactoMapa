from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from contactos.models import Friend


class FriendView(object):
    model = Friend

    def get_template_names(self):
        """Nest templates within friend directory."""
        tpl = super(FriendView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'friend'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class FriendDateView(FriendView):
    date_field = 'created_at'
    month_format = '%m'


class FriendBaseListView(FriendView):
    paginate_by = 10


class FriendArchiveIndexView(
    FriendDateView, FriendBaseListView, ArchiveIndexView):
    pass


class FriendCreateView(FriendView, CreateView):
    pass


class FriendDateDetailView(FriendDateView, DateDetailView):
    pass


class FriendDayArchiveView(
    FriendDateView, FriendBaseListView, DayArchiveView):
    pass


class FriendDeleteView(FriendView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('contactos_friend_list')


class FriendDetailView(FriendView, DetailView):
    pass


class FriendListView(FriendBaseListView, ListView):
    pass


class FriendMonthArchiveView(
    FriendDateView, FriendBaseListView, MonthArchiveView):
    pass


class FriendTodayArchiveView(
    FriendDateView, FriendBaseListView, TodayArchiveView):
    pass


class FriendUpdateView(FriendView, UpdateView):
    pass


class FriendWeekArchiveView(
    FriendDateView, FriendBaseListView, WeekArchiveView):
    pass


class FriendYearArchiveView(
    FriendDateView, FriendBaseListView, YearArchiveView):
    make_object_list = True



