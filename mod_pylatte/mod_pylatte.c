/* 
**  mod_pylatte.c -- Apache sample pylatte module
**  [Autogenerated via ``apxs -n pylatte -g'']
**
**  To play with this sample module first compile it into a
**  DSO file and install it into Apache's modules directory 
**  by running:
**
**    $ apxs -c -i mod_pylatte.c
**
**  Then activate it in Apache's apache2.conf file for instance
**  for the URL /pylatte in as follows:
**
**    #   apache2.conf
**    LoadModule pylatte_module modules/mod_pylatte.so
**    <Location /pylatte>
**    SetHandler pylatte
**    </Location>
**
**  Then after restarting Apache via
**
**    $ apachectl restart
**
**  you immediately can request the URL /pylatte and watch for the
**  output of this module. This can be achieved for instance via:
**
**    $ lynx -mime_header http://localhost/pylatte 
**
**  The output should be similar to the following one:
**
**    HTTP/1.1 200 OK
**    Date: Tue, 31 Mar 1998 14:42:22 GMT
**    Server: Apache/1.3.4 (Unix)
**    Connection: close
**    Content-Type: text/html
**  
**    The sample page from mod_pylatte.c
*/ 

#include "httpd.h"
#include "http_config.h"
#include "http_protocol.h"
#include "ap_config.h"


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <curl/curl.h>
#include <curl/types.h>
#include <curl/easy.h>


typedef struct
{
    size_t done_size;
    size_t max_size;
    char *ptr;
} MEMORY_STRUCT_S;

size_t write_data(void *ptr, size_t size, size_t nmemb, void *out)
{
    int copy_size               = 0;
    int actual_size             = size*nmemb;
    MEMORY_STRUCT_S *pst_mem    = (MEMORY_STRUCT_S*)out;

/* Copy Size */
    if (actual_size + pst_mem->done_size > pst_mem->max_size)
    {
        copy_size = pst_mem->max_size - pst_mem->done_size;
    }
    else
    {
        copy_size = actual_size;
    }

/* Memory copy */
    memcpy(pst_mem->ptr+pst_mem->done_size, ptr, copy_size);
    pst_mem->done_size += copy_size;
    return actual_size;
}


int http_get_body(
    char *url,              /**< "http://www.aaa.com/aaa.html?bbb=ccc" */
    char *buffer,           /**< Buffer */
    int size                /**< Buffer Size */
)
{
    CURL *curl_handle;
    MEMORY_STRUCT_S st_body;

    /* Set values */
    st_body.done_size = 0;
    st_body.max_size = size;
    st_body.ptr = buffer;

    /* Initialize */
    curl_global_init(CURL_GLOBAL_ALL);

    /* init the curl session */
    curl_handle = curl_easy_init();

    /* set URL to get */
    curl_easy_setopt(curl_handle, CURLOPT_URL, url);

    /* no progress meter please */
    curl_easy_setopt(curl_handle, CURLOPT_NOPROGRESS, 1);

    /* send all data to this function  */
    curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, write_data);

    /* we want the headers to this file handle */
//  curl_easy_setopt(curl_handle,   CURLOPT_WRITEHEADER ,&st_header);
    curl_easy_setopt(curl_handle,   CURLOPT_WRITEDATA ,&st_body);

    /* get it! */
    curl_easy_perform(curl_handle);

    /* cleanup curl stuff */
    curl_easy_cleanup(curl_handle);

    return 0;
}



/* The sample content handler */
static int pylatte_handler(request_rec *r)
{
	int i=0;

	char *ext;
	int extFlag = 0;
	int extDot = 0;
	char buffer[40960];
	char latteUrl[300]="http://127.0.0.1:8000";
		
	if (strcmp(r->handler, "pylatte")) {
                return DECLINED;
        }
	
	//find extension
	extFlag = 0;
	extDot = 0;
	for (i=0;i<strlen(r->uri);i++)
	{
		if(extFlag==0)
		{
			if(r->uri[i]=='.')
			{
				ext = (char *)malloc(sizeof(char)*(strlen(r->uri)-i));
				extFlag=1;
				extDot=i;
				ext[0]='.';
			}
		}
		else
		{
			//ap_rputc(r->uri[i],r);
			ext[i-extDot]=r->uri[i];
		}
	}
	ext[i-extDot]='\0';
	
	//ap_rputs("</br>",r);	
	
	//ap_rputs(ext,r);
	if (strcmp(ext,".pyl"))
	{
		return DECLINED;
	}  	
  	
    	r->content_type = "text/html";      

	//ap_rputs("</br>",r);
	if (!r->header_only) {
		
		strcat(latteUrl,r->uri);
		//ap_rputs(latteUrl,r);
		//ap_rputs("</br>",r);

		http_get_body(latteUrl,buffer,40960);
		
		ap_rputs(buffer,r);
		//ap_rputs(r->uri,r);
		if(r->args!=NULL)
			ap_rputs(r->args,r);
		//ap_rputs("</br>",r);
		//ap_rputs("The sample page from mod_pylatte.c\n", r);
		
		apr_table_addn(r->headers_out,"Module","mod_pylatte / v0.1 - http://www.pylatte.org");
    	}
	return OK;
}

static void pylatte_register_hooks(apr_pool_t *p)
{
    ap_hook_handler(pylatte_handler, NULL, NULL, APR_HOOK_MIDDLE);
}

/* Dispatch list for API hooks */
module AP_MODULE_DECLARE_DATA pylatte_module = {
    STANDARD20_MODULE_STUFF, 
    NULL,                  /* create per-dir    config structures */
    NULL,                  /* merge  per-dir    config structures */
    NULL,                  /* create per-server config structures */
    NULL,                  /* merge  per-server config structures */
    NULL,                  /* table of config file commands       */
    pylatte_register_hooks  /* register hooks                      */
};

