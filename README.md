connect2mp3.py
==============

Convert adobe connect to mp3

Simple and dodge little python script to convert adobe connect recordings to mp3.

Useful for listening to sloooow lectures a bit faster :)

Only really useful if there is more then one person talking in the lecture. If there is only one person talking you can just convert that track (from the zip file described below) to mp3 using something like "ffmpeg -i cameraVoip_0_3.flv cameraVoip_0_3.mp3"

Requires python, ffmpeg and sox.

Download zip file of recoding by following something like http://ronniediaz.com/2011/04/27/download-recordings-from-adobe-connect-pro/

Unzip and cd to resulting recordings directory.

Run connect2mp3.py

Recording will be in out.mp3

Now if you listen to the mp3 in something like VLC you can speed it up or slow it down.

Bugs

Crashes if only one track with audio.
