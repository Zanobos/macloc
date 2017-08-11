#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>			//Used for UART
#include <fcntl.h>			//Used for UART
#ifdef PI
	#include <termios.h>		//Used for UART
#endif /* PI */

#include <curl/curl.h> // For HTTP

#define DIM_BUFF 256
#define SERVER_URL "http://macloc-165115.appspot.com/rest/forcesService/upload"
#define SYMBOLS "!@#$%"

// I'll use threads to send the data to the internet
void *send_data(void *void_ptr)
{

	char *data = (char *)void_ptr;

	/*
	 * Formatting the data
	 */
	char holdId[30];
	double xaxis, yaxis, zaxis;
	
	//ID + xaxis
	char* first_token = strtok(data,"/");
	char cp_first_token[100];
	char last_symbol;
	strcpy(cp_first_token,first_token);
	int trimmed = 0;
	while(!trimmed)
	{
		char c = cp_first_token[0];
		if (strchr(SYMBOLS, c) != NULL) {
			last_symbol = c;
			strncpy(cp_first_token, cp_first_token+1, strlen(cp_first_token)); //remove char seen
		} else {
			trimmed = 1;
		}
	}
	if(last_symbol=='!'){ //TODO
		strcpy(holdId,"hold1");
	}
	xaxis = atof(cp_first_token);
	
	//yaxis
	char* second_token = strtok(NULL,"/");
	yaxis = atof(second_token);
	
	//zaxis
	char* third_token = strtok(NULL,"/");
	zaxis = atof(third_token);
	
	char body[DIM_BUFF];
	sprintf(body,"{\"wallId\":\"%s\",\"holdId\":\"%s\",\"xaxis\":\"%f\",\"yaxis\":\"%f\",\"zaxis\":\"%f\"}","wall1",holdId,xaxis,yaxis,zaxis);
	
	CURL * curl = curl_easy_init();
  	CURLcode res;
	
	if(curl) {
		
		struct curl_slist *chunk = NULL;
		chunk = curl_slist_append(chunk, "Content-Type: application/json");
		
		curl_easy_setopt(curl, CURLOPT_URL, SERVER_URL);
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, chunk);
		curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body);
		//Perform the request, res will get the return code
		res = curl_easy_perform(curl);
		//Check for errors 
		if(res != CURLE_OK)
		  fprintf(stderr, "curl_easy_perform() failed: %s\n",
				  curl_easy_strerror(res));

		//always cleanup 
		curl_easy_cleanup(curl);
	}
	/* the function must return something - NULL will do */
	return NULL;

}

int main(int argc, char **argv)
{
	int uart0_filestream = -1;
	
	//OPEN THE UART
	//The flags (defined in fcntl.h):
	//	Access modes (use 1 of these):
	//		O_RDONLY - Open for reading only.
	//		O_RDWR - Open for reading and writing.
	//		O_WRONLY - Open for writing only.
	//
	//	O_NDELAY / O_NONBLOCK (same function) - Enables nonblocking mode. When set read requests on the file can return immediately with a failure status
	//											if there is no input immediately available (instead of blocking). Likewise, write requests can also return
	//											immediately with a failure status if the output can't be written immediately.
	//
	//	O_NOCTTY - When set and path identifies a terminal device, open() shall not cause the terminal device to become the controlling terminal for the process.
	uart0_filestream = open("/dev/ttyS0", O_RDONLY /*| O_NOCTTY*/ );		//Open in blocking read mode
	if (uart0_filestream == -1)
	{
		//ERROR - CAN'T OPEN SERIAL PORT
		printf("Error - Unable to open UART.  Ensure it is not in use by another application\n");
		exit(2);
	}
	
	//CONFIGURE THE UART
	//The flags (defined in /usr/include/termios.h - see http://pubs.opengroup.org/onlinepubs/007908799/xsh/termios.h.html):
	//	Baud rate:- B1200, B2400, B4800, B9600, B19200, B38400, B57600, B115200, B230400, B460800, B500000, B576000, B921600, B1000000, B1152000, B1500000, B2000000, B2500000, B3000000, B3500000, B4000000
	//	CSIZE:- CS5, CS6, CS7, CS8
	//	CLOCAL - Ignore modem status lines
	//	CREAD - Enable receiver
	//	IGNPAR = Ignore characters with parity errors
	//	ICRNL - Map CR to NL on input (Use for ASCII comms where you want to auto correct end of line characters - don't use for bianry comms!)
	//	PARENB - Parity enable
	//	PARODD - Odd parity (else even)
	#ifdef PI
		struct termios options;
		tcgetattr(uart0_filestream, &options);
		options.c_cflag = B4800 | CS8 | CLOCAL | CREAD;		//<Set baud rate
		options.c_iflag = IGNPAR;
		options.c_oflag = 0;
		options.c_lflag = 0;
		tcflush(uart0_filestream, TCIFLUSH);
		tcsetattr(uart0_filestream, TCSANOW, &options);
	#endif /* PI */
	
	//main loop, listening for new requests
	while(1)
	{
		//These variables are local of the function, because if they are shared, I can go messy with threads
		unsigned char rx_buffer[DIM_BUFF];
		int rx_length = read(uart0_filestream, rx_buffer, DIM_BUFF -1);		//Filestream, buffer to store in, number of bytes to read (max)
		
		if (rx_length < 0)
		{
			//ERROR 
			printf("Error - Unable to read from UART.\n");
			continue;
		}
		else
		{
			rx_buffer[rx_length] = '\0';
			pthread_t send_data_thread;

			if(pthread_create(&send_data_thread, NULL, send_data, rx_buffer)) {
				fprintf(stderr, "Error creating thread\n");
				exit(3);
			}
			
		}
	}
}
