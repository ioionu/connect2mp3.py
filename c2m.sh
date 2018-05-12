#!/usr/bin/env bash
set -o errexit
set -o pipefail

function _get_the_video() {
  local url=$1
  local destination=$2
  local duration=$3
  
  xvfb-run --listen-tcp --server-num 44 --auth-file /tmp/xvfb.auth -s "-ac -screen 0 1200x768x24" google-chrome --no-gpu --disable-sandbox "${url}" &
  sleep 10
  echo "derp"
  ffmpeg -video_size 1200x768 -r 12 -f x11grab -i :44 -f pulse -ac 2 -i default -codec:v libx264 -t "${duration}" "${destination}" -y 2> /tmp/ff.log
  echo "exiting"
  killall chrome
}

_get_the_video "$@"
exit 0
