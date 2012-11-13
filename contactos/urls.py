from django.conf.urls import patterns, url



from contactos.views.contact_views import *
urlpatterns = patterns('',
    url(
        regex=r'^contact/archive/$',
        view=ContactArchiveIndexView.as_view(),
        name='contactos_contact_archive_index'
    ),
    url(
        regex=r'^contact/create/$',
        view=ContactCreateView.as_view(),
        name='contactos_contact_create'
    ),
    url(
        regex=r'^contact/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=ContactDateDetailView.as_view(),
        name='contactos_contact_date_detail'
    ),
    url(
        regex=r'^contact/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=ContactDayArchiveView.as_view(),
        name='contactos_contact_day_archive'
    ),
    url(
        regex=r'^contact/(?P<pk>\d+?)/delete/$',
        view=ContactDeleteView.as_view(),
        name='contactos_contact_delete'
    ),
    url(
        regex=r'^contact/(?P<pk>\d+?)/$',
        view=ContactDetailView.as_view(),
        name='contactos_contact_detail'
    ),
    url(
        regex=r'^contact/$',
        view=ContactListView.as_view(),
        name='contactos_contact_list'
    ),
    url(
        regex=r'^contact/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=ContactMonthArchiveView.as_view(),
        name='contactos_contact_month_archive'
    ),
    url(
        regex=r'^contact/today/$',
        view=ContactTodayArchiveView.as_view(),
        name='contactos_contact_today_archive'
    ),
    url(
        regex=r'^contact/(?P<pk>\d+?)/update/$',
        view=ContactUpdateView.as_view(),
        name='contactos_contact_update'
    ),
    url(
        regex=r'^contact/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=ContactWeekArchiveView.as_view(),
        name='contactos_contact_week_archive'
    ),
    url(
        regex=r'^contact/archive/(?P<year>\d{4})/$',
        view=ContactYearArchiveView.as_view(),
        name='contactos_contact_year_archive'
    ),
)


from contactos.views.user_views import *
urlpatterns += patterns('',
    url(
        regex=r'^user/archive/$',
        view=UserArchiveIndexView.as_view(),
        name='contactos_user_archive_index'
    ),
    url(
        regex=r'^user/create/$',
        view=UserCreateView.as_view(),
        name='contactos_user_create'
    ),
    url(
        regex=r'^user/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=UserDateDetailView.as_view(),
        name='contactos_user_date_detail'
    ),
    url(
        regex=r'^user/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=UserDayArchiveView.as_view(),
        name='contactos_user_day_archive'
    ),
    url(
        regex=r'^user/(?P<pk>\d+?)/delete/$',
        view=UserDeleteView.as_view(),
        name='contactos_user_delete'
    ),
    url(
        regex=r'^user/(?P<pk>\d+?)/$',
        view=UserDetailView.as_view(),
        name='contactos_user_detail'
    ),
    url(
        regex=r'^user/$',
        view=UserListView.as_view(),
        name='contactos_user_list'
    ),
    url(
        regex=r'^user/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=UserMonthArchiveView.as_view(),
        name='contactos_user_month_archive'
    ),
    url(
        regex=r'^user/today/$',
        view=UserTodayArchiveView.as_view(),
        name='contactos_user_today_archive'
    ),
    url(
        regex=r'^user/(?P<pk>\d+?)/update/$',
        view=UserUpdateView.as_view(),
        name='contactos_user_update'
    ),
    url(
        regex=r'^user/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=UserWeekArchiveView.as_view(),
        name='contactos_user_week_archive'
    ),
    url(
        regex=r'^user/archive/(?P<year>\d{4})/$',
        view=UserYearArchiveView.as_view(),
        name='contactos_user_year_archive'
    ),
)


from contactos.views.friend_views import *
urlpatterns += patterns('',
    url(
        regex=r'^friend/archive/$',
        view=FriendArchiveIndexView.as_view(),
        name='contactos_friend_archive_index'
    ),
    url(
        regex=r'^friend/create/$',
        view=FriendCreateView.as_view(),
        name='contactos_friend_create'
    ),
    url(
        regex=r'^friend/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=FriendDateDetailView.as_view(),
        name='contactos_friend_date_detail'
    ),
    url(
        regex=r'^friend/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=FriendDayArchiveView.as_view(),
        name='contactos_friend_day_archive'
    ),
    url(
        regex=r'^friend/(?P<pk>\d+?)/delete/$',
        view=FriendDeleteView.as_view(),
        name='contactos_friend_delete'
    ),
    url(
        regex=r'^friend/(?P<pk>\d+?)/$',
        view=FriendDetailView.as_view(),
        name='contactos_friend_detail'
    ),
    url(
        regex=r'^friend/$',
        view=FriendListView.as_view(),
        name='contactos_friend_list'
    ),
    url(
        regex=r'^friend/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=FriendMonthArchiveView.as_view(),
        name='contactos_friend_month_archive'
    ),
    url(
        regex=r'^friend/today/$',
        view=FriendTodayArchiveView.as_view(),
        name='contactos_friend_today_archive'
    ),
    url(
        regex=r'^friend/(?P<pk>\d+?)/update/$',
        view=FriendUpdateView.as_view(),
        name='contactos_friend_update'
    ),
    url(
        regex=r'^friend/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=FriendWeekArchiveView.as_view(),
        name='contactos_friend_week_archive'
    ),
    url(
        regex=r'^friend/archive/(?P<year>\d{4})/$',
        view=FriendYearArchiveView.as_view(),
        name='contactos_friend_year_archive'
    ),
)
