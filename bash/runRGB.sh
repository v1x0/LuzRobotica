#Encabezado de licencia
#!/bin/sh

#llama los GPIO a usar
$(bash GPIO1.sh 29 2>> error3.log || salir) &
$(bash GPIO2.sh 31 2>> error3.log || salir) &
$(bash GPIO3.sh 33 2>> error3.log || salir) &
