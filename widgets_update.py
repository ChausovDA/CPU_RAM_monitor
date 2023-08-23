"""Модуль обновляет виджеты"""


class ConfigureWidgets:
    """Настройка и обновление виджетов"""
    def __init__(self):
        self.list_prog_bar = None
        self.list_label = None
        self.wheel = None
        self.ram_bar = None
        self.cpu = None
        self.ram_lab = None

    def configure_ram_bar(self):
        """Настройка прогресс-бара оперативной памяти"""
        ram = self.cpu.ram_usage()
        self.ram_lab.configure(text=f"RAM:"
                                    f"\nИспользуется {round(ram[3]/1048576)}Mb,"
                                    f"\nСвободно: {round(ram[1]/1048576)} Mb")
        self.ram_bar.configure(value=ram[2])
        self.wheel = self.after(1000, self.configure_ram_bar)

    def configure_cpu_bar(self):
        """Настройка прогресс-бара ядер процессора"""
        cpu_bar = self.cpu.cpu_usage()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f"Ядро {i + 1} загружено на: {cpu_bar[i]}%")
            self.list_prog_bar[i].configure(value=cpu_bar[i])
        self.wheel = self.after(1000, self.configure_cpu_bar)
