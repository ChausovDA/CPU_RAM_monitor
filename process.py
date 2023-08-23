"""Модуль замеряет показатели работы CPU и RAM, используя psutil"""
import psutil as pt


class UsageBar:
    """Класс считывает показатели загрузки CPU и RAM"""

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_usage(self):
        """Возвращает загрузку ядер"""
        return pt.cpu_percent(percpu=True)

    def ram_usage(self):
        """Возвращает загрузку RAM"""
        return pt.virtual_memory()
