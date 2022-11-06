Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
fseconds = time.time() // 60
minute = fseconds % 60
hour = fseconds //60 &24
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hour = fseconds //60 &24
TypeError: unsupported operand type(s) for &: 'float' and 'int'
hour = fseconds //60 %24
print("현재 시간(영국 그리니치 시각):", int(hour), "시", int(minute), "분")
현재 시간(영국 그리니치 시각): 14 시 32 분
