#!/bin/bash

function _quit(){
	echo 'Press Enter to exit'
	while true
	do
		read quitkey
		if [ quitkey=='' ]
		then
			exit
		fi
	done
}

_quit