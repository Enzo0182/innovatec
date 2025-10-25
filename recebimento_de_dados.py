import serial
import threading as th
from collections import deque

class LerSerial:
    def __init__(self, port, baud=115200 , timeout=1.0):
        self.thread = None
        self.ser = serial.Serial(port=port, baudrate=baud, timeout=timeout)
        self.lock = th.Lock()
        self.running = False
        self.buffer = []

    def _read_loop(self):
        while self.running:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if not line:
                    continue
                with self.lock:
                    self.buffer.append(line)
            except Exception as e:
                print(f"O erro serial é {e}")

    def start(self):
        self.running = True
        self.thread = th.Thread(target=self._read_loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
        self.ser.close()

    def get_lines(self):
        with self.lock:
            lines = self.buffer.copy()
            self.buffer.clear()
        return lines


class WindowBuffer:
    def __init__(self, window_size, num_channels, stride=None):
        self.window_size = window_size
        self.num_channels = num_channels
        self.stride = stride if stride is not None else window_size
        self.buffer = deque(maxlen=window_size)
        self.counter = 0

    def add_sample(self, sample):
        self.buffer.append(sample)
        self.counter += 1

