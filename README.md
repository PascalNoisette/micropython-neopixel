

## Requirements

```
import mip
mip.install("github:brainelectronics/micropython-esp-wifi-manager")

import webrepl_setup
```

## Install


```
git clone https://github.com/micropython/webrepl.git webrepl-client
cd webrepl-client
.\webrepl_cli.py ../boot.py 192.168.1.200:boot.py
.\webrepl_cli.py ../swagger.py 192.168.1.200:swagger.py
.\webrepl_cli.py ../swagger.html 192.168.1.200:swagger.html
.\webrepl_cli.py ../animation.py 192.168.1.200:animation.py
.\webrepl_cli.py ../ribbon.py 192.168.1.200:ribbon.py
.\webrepl_cli.py ../rainbowio.py 192.168.1.200:rainbowio.py
```

Do not copy stub `machine.py` and `neopixel.py`