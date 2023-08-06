#!/usr/bin/env python
# coding: utf-8

# Copyright (c) zoubingwu.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, CallbackDispatcher
from traitlets import Unicode, List, Dict, validate

from ._frontend import module_name, module_version


class TableWidget(DOMWidget):
    """TODO: Add docstring here"""

    _model_name = Unicode("ExampleModel").tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode("ExampleView").tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # Your widget state goes here. Make sure to update the corresponding
    # JavaScript widget state (defaultModelProperties) in widget.ts
    value = Unicode("Jupyter").tag(sync=True)
    columns = List(Dict()).tag(sync=True)
    data = List(Dict()).tag(sync=True)

    def __init__(self, columns, data, **kwargs):
        self.columns = columns
        self.data = data
        super().__init__(**kwargs)
        self._cell_change_handlers = CallbackDispatcher()
        self.on_msg(self.__handle_custom_msg)

    @validate("columns")
    def _validate_columns(self, proposal):
        value = proposal["value"]
        if not all(
            isinstance(item, dict)
            and all(key in item for key in ["accessor", "header"])
            for item in value
        ):
            raise ValueError("columns should have `accessor` and `header` key")
        return value

    @validate("data")
    def _validate_columns(self, proposal):
        value = proposal["value"]
        return value

    def __handle_custom_msg(self, widget, content, buffers):
        if content["type"] == "cell-changed":
            self._cell_change_handlers(content["payload"])

    def on_cell_change(self, callback, remove=False):
        self._cell_change_handlers.register_callback(callback, remove=remove)

    def set_row_value(self, row):
        self._cell_change_handlers(row)
