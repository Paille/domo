import serial
import time
import sqlite3
con=sqlite3.connect('domo')
cursor=con.cursor()
cursor.execute('select * from domo;')
cursor.execute("INSERT INTO domo (device,state) VALUES ('hotte',1);")
cursor.execute("UPDATE domo SET device='plan',state=0 where device='hotte';")
devices={}
devices['']=[1,0,'' ]
devices['']=[2,0,'' ]
devices['']=[3,0,'' ]
devices['']=[4,0,'' ]
devices['']=[5,0,'' ]
devices['']=[6,0,'' ]
devices['']=[7,0,'' ]
devices['']=[8,0,'' ]
devices['']=[9,1,'' ]
devices['']=[10,1,'']
devices['']=[11,1,'']
devices['']=[12,1,'']
devices['']=[13,1,'']
devices['']=[14,1,'']
devices['']=[15,1,'']
devices['']=[16,1,'']



ser = serial.Serial(
port="/dev/ttyUSB0",
baudrate=19200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
ser.open()
count=1
line=""
code=""
lenline=10000
while True:
    for char in ser.read():
        code+=char
        line =':'.join(x.encode('hex') for x in code)
        #print(str(count) + str(': ') + line )
        #print line+'\n'
        if line.startswith('23'):
         if len(line)>=12 and lenline >100:
           lenline=int(line[9:11],16)
           #print str(lenline)+'\n'
         if len(line)==12+(lenline*3)-1:
          dump=open('dump.txt','a')
          print( line )
          dump.write( line +'\n')
          count = count+1
          dump.close()
          lenline=10000
          line=''
          code=''
        if line.endswith('23') and not(line.startswith('23')):
         line='23'
         code=code[-1]
          
