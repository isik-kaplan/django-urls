import os
from glob import glob
from importlib import import_module

from django.urls import re_path as _re_path, path as _path


def _glob_init(name):
    name = name.replace(".", os.sep)
    path = os.sep + "**"
    modules = []
    for module in glob(name + path, recursive=True):
        importable = os.path.splitext(module)[0].replace(os.sep, ".").rstrip(".")
        if "__" in importable:
            continue
        module = import_module(importable)
        modules.append(module)
    return modules


class UrlManager:
    def __init__(self, views_root=None):
        self.views_root = views_root
        self._url_patterns = []

    def _path(self, route, kwargs=None, name=None, is_re=None, importance=0):
        importance = int(importance)
        func = _re_path if is_re else _path

        def decorator(view):
            _view = view  # keep the original view
            if isinstance(view, type):
                view = view.as_view()
            self._url_patterns.append(
               (func(route, view, kwargs=kwargs, name=name or view.__name__), importance)
            )
            return _view

        return decorator

    def path(self, route, kwargs=None, name=None, importance=0):
        return self._path(route, kwargs=kwargs, name=name, is_re=False, importance=importance)

    def re_path(self, route, kwargs=None, name=None, importance=0):
        return self._path(route, kwargs=kwargs, name=name, is_re=True, importance=importance)

    def extend(self, urlpatterns):
        self._url_patterns.extend(urlpatterns)
        return self._url_patterns

    @property
    def url_patterns(self):
        if self.views_root:
            if isinstance(self.views_root, str):
                _glob_init(self.views_root)
            else:
                for root in self.views_root:
                    _glob_init(root)
        return list(i[0] for i in sorted(self._url_patterns, key=lambda x: x[1]))
