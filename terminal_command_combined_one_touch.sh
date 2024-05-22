dd 'this will show what is running in localhost in port 11434 and 1234'
lsof -iTCP:11434 -sTCP:LISTEN -n -P; lsof -iTCP:1234 -sTCP:LISTEN -n -P
dd '#this will show hardware spec'
system_profiler SPHardwareDataType
