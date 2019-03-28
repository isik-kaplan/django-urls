import os
from glob import glob
from importlib import import_module

from django.urls import re_path as _re_path, path as _path


def _glob_init(name):
    name = name.replace('.', os.sep)
    path = os.sep + '**'
    modules = []
    for module in glob(name + path, recursive=True):
        importable = os.path.splitext(module)[0].replace(os.sep, '.')
        if '__' in importable:
            continue
        try:
            module = import_module(importable)
        except ModuleNotFoundError:
            module = import_module(importable[:-1])
        modules.append(module)
    return modules


class UrlManager:
    def __init__(self, views_root):
        self.views_root = views_root
        self._url_patterns = []

    def _path(self, route, kwargs=None, name=None, is_re=None):
        func = _re_path if is_re else _path

        def decorator(view):
            if isinstance(view, type):
                view = view.as_view()
            self._url_patterns.append(
                func(route, view, kwargs=kwargs, name=name or view.__name__)
            )
            return view

        return decorator

    def path(self, route, kwargs=None, name=None):
        return self._path(route, kwargs=kwargs, name=name, is_re=False)

    def re_path(self, route, kwargs=None, name=None):
        return self._path(route, kwargs=kwargs, name=name, is_re=True)

    @property
    def url_patterns(self):
        if isinstance(self.views_root, str):
            _glob_init(self.views_root)
        else:
            for root in self.views_root:
                _glob_init(root)
        return self._url_patterns
