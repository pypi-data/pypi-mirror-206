Usage
=====

Vanilla
-------

In its simplest form, Django UFilter usage revolves around :class:`.FilterSet`.
They can be used manually::

    from django import forms
    from django_ufilter.filters import Filter
    from django_ufilter.filtersets import FilterSet

    class ProfileFilterSet(FilterSet):
        lives_in_country = Filter(form_field=forms.CharField())

    class UserFilterSet(FilterSet):
        username = Filter(form_field=forms.CharField(), lookups=['exact'])
        email = Filter(form_field=forms.CharField())
        joined = Filter(form_field=forms.DateField())
        profile = ProfileFilterSet()

    query = QueryDict(
      'email__contains=gmail'
      '&joined__year=2015'
      '&profile__lives_in_country__iexact=us'
    )
    fs = UserFilterSet(data=query, queryset=User.objects.all())
    filtered_users = fs.filter()

Notable things to mention from above:

* :class:`.FilterSet` can be used as a :class:`.Filter` within another :class:`.FilterSet`
  hence allowing filtering by related models.
* ``form_field`` is used to validate the filter value.
  Each lookup however can overwrite validation. For example ``year``
  lookup will use ``IntegerField`` rather then ``DateField``.
* :class:`.Filter` can restrict allowed lookups for that field by
  using ``lookups`` parameter

Django
------

Instead of manually creating :class:`.FilterSet`, Django UFilter comes with
:class:`.ModelFilterSet` which greatly simplifies the task::


    from django import forms
    from django_ufilter.filtersets import ModelFilterSet

    class UserFilterSet(ModelFilterSet):
        class Meta(object):
            model = User
            fields = ['username', 'email', 'joined', 'profile']

Notable things:

* ``fields`` can actually be completely omitted. In that case
  :class:`.FilterSet` will use all fields available in the model, including
  related fields.
* filters can be manually overwritten when custom behavior is required::

    class UserFilterSet(ModelFilterSet):
        username = Filter(form_field=forms.CharField(max_length=15))

        class Meta(object):
            model = User
            fields = ['username', 'email', 'joined', 'profile']

Plain Filtering
---------------

In addition to supporting regular ORMs ``django-ufilter`` also allows to
filter plain Python lists of either objects or dictionaries. This feature
is primarily meant to filter data-sources without direct filtering support
such as lists of data in redis. For example::

    from django import forms
    from django_ufilter.backend.plain import PlainFilterBackend
    from django_ufilter.filtersets.plain import PlainModelFilterSet

    class UserFilterSet(PlainModelFilterSet):
        filter_backend_class = PlainFilterBackend

        class Meta(object):
            # the filterset will generate fields from the
            # primitive Python data-types
            model = {
                'username': 'foo',
                'password': bar,
                'joined': date(2015, 1, 2),
                'profile': {
                    'preferred_name': 'rainbow',
                }
            }

    fs = UserFilterSet(data=QueryDict(), queryset=[{...}, {...}, ...])
    fs.filter()

Integrations
------------

Django UFilters tries to be usage-agnostic and does not assume
how :class:`.FilterSet` is being used in the application. It does however
ship with some common integrations to simplify common workflows.

Django Class Based Views
++++++++++++++++++++++++

:class:`.FilterSet` or related classes can directly be used within Django class-based-views::

    class MyFilterSet(ModelFilterSet):
        class Meta(object):
            model = MyModel

    class MyListView(ListView):
        queryset = MyModel.objects.all()
        def get_queryset(self):
            qs = super(MyListView, self).get_queryset()
            return MyFilterSet(data=self.request.GET, queryset=qs).filter()

Django REST Framework
+++++++++++++++++++++

Django UFilter can rather easily be integrated with DRF.
For that, a DRF-specific filter backend :class:`DRFFilterBackend <django_ufilter.integrations.drf.DRFFilterBackend>`
is implemented and can be used in settings::

    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': [
            'django_ufilter.integrations.drf.DRFFilterBackend',
        ]
    }

or manually set in the viewset::

    class MyViewSet(ModelViewSet):
        queryset = MyModel.objects.all()
        serializer_class = MyModelSerializer
        filter_backends = [DRFFilterBackend]
        filter_fields = ['field1', 'field2']

Note in the example above, fields to be filtered on are explicitly
specified in the ``filter_fields`` attribute. Alternatively if more
control over :class:`.FilterSet` is required, it can be set explicitly::

    class MyFilterSet(FilterSet):
        pass

    class MyViewSet(ModelViewSet):
        queryset = MyModel.objects.all()
        serializer_class = MyModelSerializer
        filter_backends = [DRFFilterBackend]
        filter_class = MyFilterSet

For more available options, please refer to
:class:`DRFFilterBackend <django_ufilter.integrations.drf.DRFFilterBackend>` documentation.
