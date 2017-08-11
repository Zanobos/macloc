#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>

#include <curl/curl.h> // For HTTP

#define DIM_BUFF 256
#define SERVER_URL "http://macloc-165115.appspot.com/rest/forcesService/upload"
#define SYMBOLS "!@#$%"

// I'll use threads to send the data to the internet
void *send_data(void *void_ptr)
{

	char *data = (char *)void_ptr;
	printf(data);
	printf("\n");

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
	printf("%s\n",body);
	
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
	unsigned char rx_buffer[DIM_BUFF] = "@#!45.677/3566/130";
	pthread_t send_data_thread;

	if(pthread_create(&send_data_thread, NULL, send_data, rx_buffer)) {
		fprintf(stderr, "Error creating thread\n");
		exit(3);
	}
	
	if(pthread_join(send_data_thread, NULL)) {
		fprintf(stderr, "Error joining thread\n");
		exit(3);
	}
	
	printf("FINISHED\n");
	
}
