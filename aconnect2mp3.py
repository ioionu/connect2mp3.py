#!/usr/bin/env python

import pprint
import xml.etree.ElementTree as ET
import subprocess as sp
import os

class Track():

    def __init__(self, audio_file, audio_delay):
        self.afile = audio_file
        self.delay = audio_delay

    def getWav(self):
        cmd = [FFMPEG_BIN,
            '-y',
            '-loglevel', 'quiet',
            '-i', self.afile
            ]
        if int(self.delay) != 0:
            cmd = cmd + ['-af', 'adelay=' + self.delay]

        cmd = cmd + [self.afile + '.wav']
        print " ".join(cmd)
        po = sp.Popen(cmd)
        po.stdin = None
        po.wait()
        #print(self.afile + " returned: " + str(po.returncode))
        self.wav = self.afile + '.wav'
        return self.wav


FFMPEG_BIN = "ffmpeg" # on Linux

tree = ET.parse("indexstream.xml")
root = tree.getroot()

#find messages
messages = root.findall("Message")
#print messages

recording = []
for message in messages:
    method = message.find("Method")
    if method.text == 'playEvent':
        filename = message.findall("Array/Object/streamName")
        added = message.find("String")
        if len(filename) != 0 and added.text == 'streamAdded':
            fn = filename[0].text + ".flv"
            fn = fn[1:] #strip out slash
            dl = message.attrib['time']
            recording.append( Track(fn, dl ) )

for t in recording:
    t.getWav()

sox = ['sox','--norm','-m'] + [t.wav for t in recording] + ['out.wav']
print " ".join(sox)
po = sp.Popen(sox)
po.stdin = None
po.wait()

#compress wav
print("compress wav")
cmd = [FFMPEG_BIN,'-y','-loglevel', 'quiet','-i','out.wav','out.mp3']
print " ".join(cmd)
po = sp.Popen(cmd)
po.stdin = None
po.wait()

print("cleaning up")
for t in recording:
    os.remove(t.wav)
os.remove('out.wav')

print("end");
