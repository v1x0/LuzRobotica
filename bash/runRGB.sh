#!/bin/sh

#llama los GPIO a usar
$(bash GPIO1.sh 5 2>> error3.log || salir) &
$(bash GPIO2.sh 6 2>> error3.log || salir) &
$(bash GPIO3.sh 13 2>> error3.log || salir) &
