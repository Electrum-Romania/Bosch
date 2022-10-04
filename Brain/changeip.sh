#!/bin/bash

IPPATTERN='[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?.[0-9][0-9]?[0-9]?'
IP="$1"

grep -Eq "$IPPATTERN" <<<"$IP" || {
	echo 'not an ip'
	exit
}

gawk -i inplace '/self.serverIp[ \t]*=/ { sub(/'"$IPPATTERN"'/, "'"$IP"'") } { print }' \
	src/utils/camerastreamer/CameraStreamerProcess.py                               \
	src/utils/remotecontrol/RemoteControlTransmitterProcess.py
