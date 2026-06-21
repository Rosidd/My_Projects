# Workspace Object (workspaceobject.h)

## Detailed Description

This module implements the methods of the abstract class called WorkspaceObject from which several other classes descend. The methods of these classes are presented as the functional interface described in this reference section.
The system employs an object-oriented design and these functions implement the methods found at the top of the hierarchy. The hierarchy starts with POM objects at the top. This means all descendant objects may use POM functions.

Each of these modules introduces a specialized interface to the objects. Therefore, the super class interface (e.g., POM) may no longer be applicable and/or allowed.


Note:
To use these functions, include workspaceobject.h.
Data Structure Descriptions
These constants specify the size of variables returned in the get_info entries. Do not write more than this number of bytes into the buffers.

- WSO_name_size_c
- WSO_desc_size_c
- WSO_date_size_c
- WSO_revision_size_c

## Search Criteria

The following structure allows you to specify a query:

WSO_search_criteria_t

## Status

The following structure is used for returning status information for a workspace object from WSOM_ask_status:

WSO_status_t

Basic Information

The following structure contains basic information about a workspace object:

## WSO_description_t

The values in square brackets indicate the amount of memory allocated for the storage of the value of the corresponding attribute. For those that can be changed care must be taken not to overwrite the limits.

#### Dates are returned as: yyyy-mm-dd hh:mm:ss
---
## Common Return Values

- CXPOM_invalid_tag:	Function specified a tag that is either no longer existent or is not a tag_t.
- CXPOM_wrong_class:	Tag supplied is not a valid WorkspaceObject.
- WSO_wr_invalid_depth	Invalid depth (zero or negative).
- WSOM_invalid_eff	Effectivity tag being queried does not exist.
- WSOM_bad_effectivity_text_format	This error is returned when difficulty is encountered parsing a string into a set of start-end range values. The problem might be one or more of the following:
- Incorrect format for date effectivities.
- Text representation of 'to' not being equal to corresponding internationalized values.
- Text representations of 'open-ended' and 'stock-out' not being equal to internationalized values.
- Go to WSOM_eff_set_range for additional information.
- WSOM_range_overlap	A correctly formatted discontinuous range must contain values that are in ascending order, otherwise this error will result. Go to WSOM_eff_set_range for additional information.
- WSOM_eff_with_end_item_in_rs	The WSOM_eff_with_end_item_in_rs error code is deprecated and will be removed from Teamcenter 11.
- WSOM_cannot_edit_protected	A protected effectivity cannot be edited. To make the effectivity editable, it must first be unlocked. This can only be done by a user with the correct permissions.
- WSOM_no_mixed_range_types	The range text contains both date and unit values; effectivities can have either a date range or a unit range, but not both.
- WSOM_closed_status_open_range	A range being set with an array has an odd number of values, suggesting an open-ended range, but the WSOM_open_ended_status_t parameter is set to EFFECTIVITY_closed.
- WSOM_open_status_closed_range	A range being set with an array has an even number of values, suggesting a closed range, but the WSOM_open_ended_status_t parameter is set to EFFECTIVITY_open_ended or EFFECTIVITY_stock_out.
- WSOM_cant_save_eff_with_no_rs	An effectivity must be attached to a release status before it can be saved. This error results if an ITK program is still working with an effectivity that has been removed from its release status.
- WSOM_init_module WSOM_exit_module	WSOM_init/exit_module are the standard wrappers round any module; they are called by Teamcenter startup / TC_stop so the normal ITK programmer can ignore them. Repeated calls to WSOM_init_module are harmless.
- WSOM_extent	WSOM_extent returns all the workspace objects in the database (an unlikely event for any real site - but potentially useful on a test database).
- WSOM_cannot_destroy_eff	An attempt is being made to destroy an effectivity attached to a release status. This should be done by removing the effectivity from the release status.


---

## Modules
- WSO Errors
- WSO Messages
## Data Structures
- struct WSO_description_s
- struct WSO_search_criteria_s
- struct WSO_get_info_entry_s
- struct WSO_descriptor_s
- struct WSO_status_s
- struct WSOM_effectivity_info_s
## Release Status ITK
TCCORE_API int WSOM_ask_release_status_list (tag_t workspace_object, int *status_count, tag_t **status_list)
TCCORE_API int WSOM_status_ask_date_released (tag_t release_status, date_t *release_date)
## Effectivity ITK
All functions that add/edit/remove effectivity automatically lock the release status and effectivities. After such calls, the changes remain loaded in session until committed to the database by calling AOM_save( release_status ). There is never a need to save individual effectivity instances; they will be automatically saved when you save the owning release status.
- TCCORE_API int WSOM_effectivity_create (tag_t release_status, tag_t end_item, tag_t *effectivity)
- TCCORE_API int WSOM_effectivity_create_empty (tag_t release_status, tag_t *effectivity)
- TCCORE_API int WSOM_eff_create_with_date_text (tag_t release_status, tag_t end_item, const char *range_text, tag_t *effectivity)
- TCCORE_API int WSOM_eff_create_with_unit_text (tag_t release_status, tag_t end_item, const char *range_text, tag_t *effectivity)
- TCCORE_API int WSOM_effectivity_create_with_effectivitygroup (tag_t effectivitygroup_rev, tag_t end_item, const char *unit_text, tag_t *effectivity)
- TCCORE_API int WSOM_effectivity_create_with_text (tag_t release_status, tag_t end_item, const char *range_text, tag_t *effectivity)
- TCCORE_API int WSOM_effectivity_create_with_units (tag_t release_status, tag_t end_item, int n_units, int *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, tag_t *effectivity)
- TCCORE_API int WSOM_effectivity_create_with_dates (tag_t release_status, tag_t end_item, int n_dates, date_t *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, tag_t *effectivity)
- TCCORE_API int WSOM_status_ask_effectivities (tag_t release_status, int *n_effectivities, tag_t **effectivities)
- TCCORE_API int WSOM_status_remove_effectivity (tag_t release_status, tag_t effectivity)
- TCCORE_API int WSOM_status_clear_effectivities (tag_t release_status)
- TCCORE_API int WSOM_eff_set_range (tag_t release_status, tag_t effectivity, const char *range_text, logical append)
- TCCORE_API int WSOM_effectivity_set_range (tag_t effectivity, const char *range_text, logical append)
- TCCORE_API int WSOM_eff_set_unit_range (tag_t release_status, tag_t effectivity, const char *range_text, logical append)
- TCCORE_API int WSOM_eff_ask_unit_range (tag_t release_status, tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_effectivity_ask_unit_range (tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_eff_set_date_range (tag_t release_status, tag_t effectivity, const char *range_text, logical append)
- TCCORE_API int WSOM_eff_ask_date_range (tag_t release_status, tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_effectivity_ask_date_range (tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_eff_ask_range (tag_t release_status, tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_effectivity_ask_range (tag_t effectivity, char **range_text)
- TCCORE_API int WSOM_eff_set_units (tag_t release_status, tag_t effectivity, int n_units, int *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, logical append)
- TCCORE_API int WSOM_effectivity_set_units (tag_t effectivity, int n_units, int *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, logical append)
- TCCORE_API int WSOM_eff_set_dates (tag_t release_status, tag_t effectivity, int n_dates, date_t *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, logical append)
- TCCORE_API int WSOM_effectivity_set_dates (tag_t effectivity, int n_dates, date_t *start_end_values, WSOM_open_ended_status_t open_ended_or_stock_out, logical append)
- TCCORE_API int WSOM_eff_ask_units (tag_t release_status, tag_t effectivity, int *n_units, int **start_end_values, WSOM_open_ended_status_t *open_ended_or_stock_out)
- TCCORE_API int WSOM_effectivity_ask_units (tag_t effectivity, int *n_units, int **start_end_values, WSOM_open_ended_status_t *open_ended_or_stock_out)
- TCCORE_API int WSOM_eff_ask_dates (tag_t release_status, tag_t effectivity, int *n_dates, date_t **start_end_values, WSOM_open_ended_status_t *open_ended_or_stock_out)
- TCCORE_API int WSOM_effectivity_ask_dates (tag_t effectivity, int *n_dates, date_t **start_end_values, WSOM_open_ended_status_t *open_ended_or_stock_out)
- TCCORE_API int WSOM_eff_ask_ranges (tag_t release_status, tag_t effectivity, int *n_units, int *n_dates, int **units, date_t **dates, WSOM_open_ended_status_t *unit_open_ended_status, WSOM_open_ended_status_t *date_open_ended_status)
- TCCORE_API int WSOM_effectivity_ask_ranges (tag_t effectivity, int *n_units, int *n_dates, int **units, date_t **dates, WSOM_open_ended_status_t *unit_open_ended_status, WSOM_open_ended_status_t *date_open_ended_status)
- TCCORE_API int WSOM_eff_ask_range_type (tag_t release_status, tag_t effectivity, WSOM_range_type_t *range_type)
- TCCORE_API int WSOM_effectivity_ask_range_type (tag_t effectivity, WSOM_range_type_t *range_type)
- TCCORE_API int WSOM_eff_clear_ranges (tag_t release_status, tag_t effectivity)
- TCCORE_API int WSOM_eff_set_range_type (tag_t release_status, tag_t effectivity, WSOM_range_type_t range_type)
- TCCORE_API int WSOM_effectivity_set_range_type (tag_t effectivity, WSOM_range_type_t range_type)
- TCCORE_API int WSOM_eff_set_end_item_rev (tag_t release_status, tag_t effectivity, tag_t end_item_rev)
- TCCORE_API int WSOM_eff_set_end_item (tag_t release_status, tag_t effectivity, tag_t end_item)
- TCCORE_API int WSOM_effectivity_set_end_item (tag_t effectivity, tag_t end_item)
- TCCORE_API int WSOM_eff_ask_end_item_rev (tag_t release_status, tag_t effectivity, tag_t *end_item_rev)
- TCCORE_API int WSOM_eff_ask_end_item (tag_t release_status, tag_t effectivity, tag_t *end_item)
- TCCORE_API int WSOM_effectivity_ask_end_item (tag_t effectivity, tag_t *end_item)
- TCCORE_API int WSOM_eff_set_protection (tag_t release_status, tag_t effectivity, logical protection)
- TCCORE_API int WSOM_effectivity_set_protection (tag_t effectivity, logical protection)
- TCCORE_API int WSOM_eff_ask_is_protected (tag_t release_status, tag_t effectivity, logical *is_protected)
- TCCORE_API int WSOM_effectivity_is_protected (tag_t effectivity, logical *is_protected)
- TCCORE_API int WSOM_ask_effectivity_mode (logical *is_v7)
- TCCORE_API int WSOM_ask_ead_paragraph (tag_t aWSOTag, int *num, char ***paragraph)
## Defines
#define WSO_name_size_c   128
### define TC_LEGACY_ID_NAME_SIZE   32
#define WSO_desc_size_c   240
### define WSO_date_size_c   21
#define WSO_object_type_size_c   32
### define WSO_revision_size_c   15
#define WSO_release_status_size_c   128
### define WSO_ip_class_size_c   128
#define WSO_gov_class_size_c   128
#define WSO_where_ref_any_depth   -1
#define RLM_tasktype_name_size_c   32
#define RLM_tasktype_desc_size_c   32
#define RLM_followup_action_size_c   32
#define Describe_object_name   0x1
#define Describe_object_type   0x2
#define Describe_owner   0x4
#define Describe_application   0x8
#define Describe_date_created   0x10
#define Describe_date_modified   0x20
#define Describe_date_released   0x40
#define Describe_released_for   0x80
#define Describe_id_string   0x100
#define Describe_revision_number   0x200
#define Describe_revision_limit   0x400
#define Describe_owning_group   0x800
#define Describe_last_mod_user   0x1000
#define Describe_archive_date   0x2000
#define Describe_backup_date   0x4000
#define Describe_description   0x8000
#define Describe_is_frozen   0x10000
#define Describe_is_reserved   0x20000
#define Describe_revision_id   0x40000
#define Describe_owning_site   0x80000
#define WSO_search_HOR   0
#define WSO_search_Vault   1
### Typedefs
typedef struct WSO_description_s WSO_description_t
typedef struct WSO_description_s * WSO_description_p_t
typedef struct
WSO_search_criteria_s WSO_search_criteria_t
typedef struct
WSO_search_criteria_s * WSO_search_criteria_p_t
typedef struct WSO_get_info_entry_s WSO_get_info_entry_t
typedef struct
WSO_get_info_entry_s * WSO_get_info_entry_p_t
typedef struct WSO_descriptor_s WSO_descriptor_t
typedef struct WSO_descriptor_s * WSO_descriptor_p_t
typedef struct WSO_status_s WSO_status_t
typedef enum
WSOM_open_ended_status_e WSOM_open_ended_status_t
typedef enum WSOM_range_type_e WSOM_range_type_t
typedef struct
WSOM_effectivity_info_s WSOM_effectivity_info_t
## Enumerations
enum WSOM_open_ended_status_e { EFFECTIVITY_closed = 0, EFFECTIVITY_open_ended = 1, EFFECTIVITY_stock_out = 2 }
enum WSOM_range_type_e { EFFECTIVITY_range_not_defined = 0, EFFECTIVITY_range_unit = 1, EFFECTIVITY_range_date = 2, EFFECTIVITY_range_legacy_unit_and_date = 3 }
## Functions
- TCCORE_API int WSOM_init_module ()
- TCCORE_API int WSOM_exit_module ()
- TCCORE_API int WSOM_extent (int *n_instances, tag_t **instances)
- TCCORE_API int WSOM_initialize (tag_t a_WSO_tag, const char a_name[WSO_name_size_c+1], const char a_description[WSO_desc_size_c+1])
- TCCORE_API int WSOM_initialize2 (tag_t a_WSO_tag, const char *a_name, const char *a_description)
- TCCORE_API int WSOM_set_name (tag_t a_WSO_tag, const char new_name[WSO_name_size_c+1])
- TCCORE_API int WSOM_set_name2 (tag_t a_WSO_tag, const char *new_name)
- TCCORE_API int WSOM_ask_name (tag_t a_WSO_tag, char a_name[WSO_name_size_c+1])
- TCCORE_API int WSOM_ask_name2 (tag_t a_WSO_tag, char **a_name)
- TCCORE_API int WSOM_ask_id_string (tag_t a_WSO_tag, char **an_id)
- TCCORE_API int WSOM_ask_object_id_string (tag_t a_WSO_tag, char **object_id)
- TCCORE_API int WSOM_set_description (tag_t a_WSO_tag, const char new_description[WSO_desc_size_c+1])
- TCCORE_API int WSOM_set_description2 (tag_t a_WSO_tag, const char *new_description)
- TCCORE_API int WSOM_ask_description (tag_t a_WSO_tag, char a_description[WSO_desc_size_c+1])
- TCCORE_API int WSOM_ask_description2 (tag_t a_WSO_tag, char **a_description)
- TCCORE_API int WSOM_set_object_type (tag_t wso_tag, const char object_type[WSO_name_size_c+1])
- TCCORE_API int WSOM_set_object_type2 (tag_t wso_tag, const char *object_type)
- TCCORE_API int WSOM_ask_status (tag_t a_WSO_tag, int *status_count, WSO_status_t **status_structures)
- TCCORE_API int WSOM_set_ip_classification (tag_t aWSOsTag, const char newClassn[WSO_ip_class_size_c+1])
- TCCORE_API int WSOM_set_ip_classification2 (tag_t aWSOsTag, const char *newClassn)
- TCCORE_API int WSOM_ask_ip_classification (tag_t aWSOsTag, char aClassification[WSO_ip_class_size_c+1])
- TCCORE_API int WSOM_ask_ip_classification2 (tag_t aWSOsTag, char **aClassification)
- TCCORE_API int WSOM_has_ip_classification (tag_t aWSOsTag, logical *hasIPClassification)
- TCCORE_API int WSOM_set_gov_classification (tag_t aWSOsTag, const char classification[WSO_gov_class_size_c+1])
- TCCORE_API int WSOM_set_gov_classification2 (tag_t aWSOsTag, const char *classification)
- TCCORE_API int WSOM_ask_gov_classification (tag_t aWSOsTag, char classification[WSO_gov_class_size_c+1])
- TCCORE_API int WSOM_ask_gov_classification2 (tag_t aWSOsTag, char **classification)
- TCCORE_API int WSOM_has_gov_classification (tag_t aWSOsTag, logical *hasGovClassification)
- TCCORE_API int WSOM_ask_ip_logged (tag_t aWSOsTag, logical *logged)
- TCCORE_API int WSOM_ask_user_can_unmanage (tag_t aWSOsTag, logical *can_unmanage)
- TCCORE_API int WSOM_ask_licenses (tag_t aWSOTag, int *licenseCount, tag_t **licenses)
- TCCORE_API int WSOM_find (const char name[WSO_name_size_c+1], int *hits, tag_t **list)
- TCCORE_API int WSOM_find2 (const char *name, int *hits, tag_t **list)
- TCCORE_API int WSOM_clear_search_criteria (WSO_search_criteria_t *criteria)
- TCCORE_API int WSOM_search (WSO_search_criteria_t criteria, int *hits, tag_t **list)
- TCCORE_API int WSOM_get_info (tag_t a_WS0_tag, WSO_descriptor_t *info)
- TCCORE_API int WSOM_set_info (tag_t a_WS0_tag, WSO_descriptor_t *info)
- TCCORE_API int WSOM_free_info (tag_t a_WS0_tag, WSO_descriptor_t *info)
- TCCORE_API int WSOM_describe (tag_t a_WSO_tag, WSO_description_t *description)
- TCCORE_API int WSOM_copy (tag_t a_WSO_tag, const char *new_name, tag_t *copy_tag)
- TCCORE_API int WSOM_set_revision (tag_t a_WSO_tag, int rev_number)
- TCCORE_API int WSOM_ask_revision (tag_t a_WSO_tag, int *rev_number)
- TCCORE_API int WSOM_set_revision_limit (tag_t a_WSO_tag, int rev_limit)
- TCCORE_API int WSOM_ask_revision_limit (tag_t a_WSO_tag, int *rev_limit)
- TCCORE_API int WSOM_ask_object_type (tag_t a_WSO_tag, char object_type[WSO_name_size_c+1])
- TCCORE_API int WSOM_ask_object_type2 (tag_t a_WSO_tag, char **object_type)
- TCCORE_API int WSOM_ask_based_on (tag_t wso, tag_t *based_on_wso)
- TCCORE_API int WSOM_list_derived_wsos (tag_t wso, int *n_derived, tag_t **derived_wsos)
- TCCORE_API int WSOM_where_referenced (tag_t wso, int n_levels, int *n_referencers, int **levels, tag_t **referencers, char ***relations)
Define Documentation
### define Describe_application   0x8

Definition at line 176 of file workspaceobject.h.
