from pattern.web import time,Twitter

engine = Twitter(license=None, throttle=0.5, language=None)
s = engine.stream('#DMCLatam2013')
for tweet in range(10):
    time.sleep(1)
    s.update(bytes=1024)
    print s[-1].text if s else ''