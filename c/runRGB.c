//Añadir Licencia
/*
*Este programa se compila con la siguiente instruccion
*gcc prog.c -lpthread -lm
*/
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define BCM2708_PERI_BASE       0x3F000000
const unsigned int GPIO_BASE  = BCM2708_PERI_BASE + 0x200000; /* GPIO controller */

const unsigned short PAGE_SIZE = 4*1024;
const unsigned short BLOCK_SIZE = 4*1024;

const unsigned long REPEAT = 1000;
const unsigned long DELAY = 1000;

const unsigned long MARK = 1000;
const unsigned long SPACE = 5000;

int  mem_fd;
void *gpio_map;

volatile unsigned *gpio;

// GPIO setup macros. Always use INP_GPIO(x) before using OUT_GPIO(x) or SET_GPIO_ALT(x,y)
#define INP_GPIO(g) *(gpio+((g)/10)) &= ~(7<<(((g)%10)*3))
#define OUT_GPIO(g) *(gpio+((g)/10)) |=  (1<<(((g)%10)*3))
#define SET_GPIO_ALT(g,a) *(gpio+(((g)/10))) |= (((a)<=3?(a)+4:(a)==4?3:2)<<(((g)%10)*3))

#define GPIO_SET *(gpio+7)  // sets   bits which are 1 ignores bits which are 0
#define GPIO_CLR *(gpio+10) // clears bits which are 1 ignores bits which are 0

#define GET_GPIO(g) (*(gpio+13)&(1<<g)) // 0 if LOW, (1<<g) if HIGH

#define GPIO_PULL *(gpio+37) // Pull up/pull down
#define GPIO_PULLCLK0 *(gpio+38) // Pull up/pull down clock

#define HILOS 3 

//
// Set up a memory regions to access GPIO
//
void setup_io()
{
    if ((mem_fd = open("/dev/mem", O_RDWR|O_SYNC) ) < 0)
    {
	printf("can't open /dev/mem (sudo?)\n");
	exit(-1);
    }

    gpio_map = mmap(
		       NULL,             //Any adddress in our space will do
		       BLOCK_SIZE,       //Map length
		       PROT_READ|PROT_WRITE,// Enable reading & writting to mapped memory
		       MAP_SHARED,       //Shared with other processes
		       mem_fd,           //File to map
		       GPIO_BASE         //Offset to GPIO peripheral
		   );

    close(mem_fd); //No need to keep mem_fd open after mmap

    if (gpio_map == MAP_FAILED)
    {
	printf("mmap error %d\n", (int)gpio_map);//errno also set!
	exit(-1);
    }

    gpio = (volatile unsigned *)gpio_map;
}

//funcion que envia el tren de pulsos a GPIO
void doPWM(pin)
{
	
    int rep;
    pin;

    for (rep=0; rep<REPEAT; rep++)
    {
		printf ("OFF %d\n", pin);
		INP_GPIO(pin);
		usleep(DELAY);
	
		GPIO_SET = 1<<pin;
		printf ("HIGH %d\n", pin);
	
		OUT_GPIO(pin);
		usleep(DELAY);
	
		printf ("OFF %d\n", pin);
		INP_GPIO(pin);
		usleep(DELAY);
	
		GPIO_CLR = 1<<pin;
		printf ("LOW %d\n", pin);
	
		OUT_GPIO(pin);
		usleep(DELAY);
    }
	
	return 0;
}

//funcion que llama al ciclo para generar PWM por software
void *PWM(void *hilo)
{
	int nHilo;
	
	nHilo = *(int*)hilo;
	
	switch(nHilo)
	{
		case 0:
			doPWM(5);
		break;
		case 1:
			doPWM(6);
		break;
		case 2:
			doPWM(13);
		break;
	}
	
   //termina el hilo
   pthread_exit(hilo);
}

main(){
	// se definen las varibles para el programa
  pthread_t hilos[HILOS];
  int i,error;
  int h[HILOS];

  setup_io();
  //se lanzan los hilos
  for(i=0;i<HILOS;i++){
      h[i]=i;
      error=pthread_create(&hilos[i],NULL,PWM,&h[i]);
  }
} 
