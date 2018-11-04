# pytivo

A Python Library to control TiVo set top boxes



## Code Examples:

The following code will print out the current channel:
```
from pytivo import tivo_client

host = "xxx.xxx.xxx.xxx"
#The port is usually 31339, if it's something else for some reason change it.
port = 31339

tc = tivo_client.TivoClient(host, port)

print(tc.getStatus())
```

The following code will take an input and set the channel to that:
```
from pytivo import tivo_client

host = "xxx.xxx.xxx.xxx"
#The port is usually 31339, if it's something else for some reason change it.
port = 31339

tc = tivo_client.TivoClient(host, port)

channel_number = input("Enter a channel number: ")

print(tc.setChannel(channel_number))
```
