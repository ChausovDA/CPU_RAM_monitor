"""Модуль строит графический интерфейс"""
import sys
import tkinter as tk
from tkinter import ttk

from process import UsageBar
from widgets_update import ConfigureWidgets


class Window(tk.Tk, ConfigureWidgets):
    """Главное окно"""

    def __init__(self):
        tk.Tk.__init__(self)
        ConfigureWidgets.__init__(self)
        self.progress_bar_frame = None
        self.btn_frame = None
        self.resizable(False, False)
        self.set_ui()
        self.cpu = UsageBar()
        self.make_bars_usage()
        self.configure_ram_bar()
        self.configure_cpu_bar()

    def set_ui(self):
        """Графический интерфейс"""
        exit_btn = ttk.Button(self, text="Выход", command=self.app_exit)
        exit_btn.pack(fill=tk.X, side="bottom")

        self.btn_frame = ttk.LabelFrame(self, text="Количество ядер и потоков:")
        self.btn_frame.pack(fill=tk.X)

        self.progress_bar_frame = ttk.LabelFrame(self, text="Загруженность:")
        self.progress_bar_frame.pack(fill=tk.BOTH)

    def make_bars_usage(self):
        """Виджеты прогресс-баров RAM и CPU"""
        ttk.Label(self.btn_frame, text=f"Ядер: {self.cpu.cpu_count}"
                                       f"\nПотоков: {self.cpu.cpu_count_logical}").pack(fill=tk.X)

        self.list_label = []
        self.list_prog_bar = []
        for _ in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.progress_bar_frame, anchor=tk.CENTER))
            self.list_prog_bar.append(ttk.Progressbar(self.progress_bar_frame, length=100))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_prog_bar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.progress_bar_frame, text="")
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.progress_bar_frame, length=100)
        self.ram_bar.pack(fill=tk.X)

    def app_exit(self):
        """Выход из приложения"""
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Window()
    root.mainloop()
