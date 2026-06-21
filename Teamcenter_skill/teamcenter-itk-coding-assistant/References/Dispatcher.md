# Dispatcher/dispatcher_itk.h File Reference
## Detailed Description
This file contains the different ITK methods available for the Dispatcher Management application for Teamcenter.
Definition in file dispatcher_itk.h.

### include <dispatcher/libdispatcher_exports.h>
### include <dispatcher/dispatcher_errors.h>
### include <time.h>
### include <dispatcher/libdispatcher_undef.h>

- Go to the source code of this file.
## Defines
### define DISPATCHER_UPDATE_EXISTING   "ETSUpdOvr"
### define DISPATCHER_PREF_SUCCESSFUL_STATES   "TS_successful_states";
### define DISPATCHER_PREF_UNSUCCESSFUL_STATES   "TS_unsuccessful_states";
### define DISPATCHER_PREF_INPROCESS_STATES   "TS_inprocess_states";
### define ETS_translation_arg_size_c   255
### define ETS_TRANSLATION_ARG_NV_SEP   "="
### define ETS_TRANSLATION_ARG_MIN_SIZE   3
### define ETS_TRANSLATION_ARG_NAME_TRIGGER   "ETSTrigger"
### define ETS_TRANSLATION_ARG_NAME_UPDATE_OVR   "ETSUpdOvr"
### define ETS_TRANSLATION_ARG_VALUE_TRUE   "true"
### define ETS_TRANSLATION_ARG_VALUE_FALSE   "false"

## Functions
- int DISPATCHER_API DISPATCHER_create_request (const char *provider_name, const char *service_name, const int priority, const time_t start_time, const time_t end_time, const int interval, const int num_objs, const tag_t *primary_objs, const tag_t *secondary_objs, const int num_args, const char **request_args, const char *type, const int num_datafiles, const char **data_file_keys, const char **datafiles, tag_t *request)
- int DISPATCHER_API DISPATCHER_query_requests (const int num_providers, const char **providers, const int num_services, const char **services, const int num_states, const char **states, const int num_priorities, const int *priorities, const int num_users, const char **owning_users, const int num_taskids, const char **task_ids, int *num_requests, tag_t **queried_requests)
- int DISPATCHER_API DISPATCHER_wait_for_request (tag_t request, int interval, int time_to_wait, logical *is_final)
- int DISPATCHER_API DISPATCHER_delete_request (tag_t requestToDelete, int ignoreState)
- int DISPATCHER_API DISPATCHER_add_files_to_request (const tag_t request, const int numFiles, const char **fileKeys, const char **files)
- int DISPATCHER_API DISPATCHER_get_files_from_request (const tag_t request, const int numKeys, const char **keys, const char *path)
- int DISPATCHER_API DISPATCHER_find_request_by_tag (const tag_t requestTag, char **task_id, char **providerName, char **serviceName, int *priority, char **currentState, char **type, int *numObjs, tag_t **primaryObjs, tag_t **secondaryObjs, int *numArgs, char ***argKeys, char ***argData)
- int DISPATCHER_API DISPATCHER_is_final_state (const tag_t request, int *isFinalState)
- int DISPATCHER_API ETS_create_request (const int num_objs, const tag_t *primary_objs, const tag_t *secondary_objs, const int sched_priority, const char *provider_name, const char *translator_name, const char *trigger, tag_t *request)
- int DISPATCHER_API ETS_create_request2 (const int num_objs, const tag_t *primary_objs, const tag_t *secondary_objs, const int priority, const char *provider_name, const char *translator_name, const char *trigger, const int num_translation_args, const char **translation_args, tag_t *request)
- int DISPATCHER_API ETS_query_requests (const char *translationRequestState, int *numTranslationRequests, tag_t **translationRequests)
- int DISPATCHER_API ETS_find_request_by_tag (const tag_t requestTag, char **task_id, char **state, int *num_objs, tag_t **primary_objs, tag_t **secondary_objs, int *priority, char **provider_name, char **translator_name, int *num_trans_args, char ***translation_args)
- int DISPATCHER_API ETS_is_final_state (const tag_t request, int *isFinalState)

## Define Documentation
### define DISPATCHER_PREF_INPROCESS_STATES   "TS_inprocess_states";
 
- Definition at line 40 of file dispatcher_itk.h.
 
### define DISPATCHER_PREF_SUCCESSFUL_STATES   "TS_successful_states"; 
- Definition at line 38 of file dispatcher_itk.h.

### define DISPATCHER_PREF_UNSUCCESSFUL_STATES   "TS_unsuccessful_states";

- Definition at line 39 of file dispatcher_itk.h.

### define DISPATCHER_UPDATE_EXISTING   "ETSUpdOvr"
 
- Definition at line 35 of file dispatcher_itk.h.
  
### define ETS_TRANSLATION_ARG_MIN_SIZE   3

- Definition at line 53 of file dispatcher_itk.h.
 
### define ETS_TRANSLATION_ARG_NAME_TRIGGER   "ETSTrigger"
 
- Definition at line 56 of file dispatcher_itk.h.
 
### define ETS_TRANSLATION_ARG_NAME_UPDATE_OVR   "ETSUpdOvr"
 
- Definition at line 62 of file dispatcher_itk.h.
 
### define ETS_TRANSLATION_ARG_NV_SEP   "="
 
- Definition at line 52 of file dispatcher_itk.h.
 
### define ETS_translation_arg_size_c   255
 
- Definition at line 51 of file dispatcher_itk.h.
 
### define ETS_TRANSLATION_ARG_VALUE_FALSE   "false"

- Definition at line 68 of file dispatcher_itk.h.

### define ETS_TRANSLATION_ARG_VALUE_TRUE   "true"
 
- Definition at line 67 of file dispatcher_itk.h.
 
### Example:

- int DISPATCHER_API DISPATCHER_add_files_to_request	(	const tag_t 	request,
 const int 	numFiles,
 const char ** 	fileKeys,
 const char ** 	files	 
 )			

Parameters:
- request 	(I) tag of the request
- numFiles 	(I) number of files to upload
- fileKeys 	(I) file keys to associate to files
- files 	(I) ABSOLUTE paths to file to upload
 
