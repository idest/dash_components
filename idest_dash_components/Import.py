# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Import(Component):
    """A Import component.
Import serves for the only purpose to force Dash to load idest-dash-components.
This is useful when you want to use grasia components that are going to be
added dynamically to the Dash app layout.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- src (string; optional): local or external source of the javascript to import

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, src=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'src']
        self._type = 'Import'
        self._namespace = 'idest_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'src']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Import, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Import(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Import(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
