# __init__.py
from .module import greet  # относительный импорт, для упрощения импорта
from .utils import add

__version__ = '1.0.0.'
__doc__ = 'Это пакет, который содержит ...'
__author__ = 'Иван'
__all__ = ['greet', 'add']



