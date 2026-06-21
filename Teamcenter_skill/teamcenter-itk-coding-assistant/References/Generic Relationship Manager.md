#  Generic Relationship Manager (grm.h)
## Detailed Description
The GRM module supports the concept of explicit relationships. A dataset can be directly and explicitly related to an Item Revision with, as an example, a specification relationship. With GRM, you can define and enforce specific rules pertaining to relationships, as well as separate the maintenance of relationships from the data itself.
Common Return Values

| Return Value | Description |
| ------------ | ----------- |
| CXPOM_invalid_tag |	Invalid tag supplied.
| GRM_duplicate_relation_type |	The type you propose to create already exists in the system. |
| GRM_internal_error |	The GRM module has detected an internal inconsistency and therefore should not be used. |
| GRM_invalid_primary_object |	Specified tag for the primary_object is not valid. |
| GRM_invalid_relation_type |	Specified tag for relation_type is not valid. |
| GRM_invalid_secondary_object |	Specified tag for the secondary_object is not valid. |
| GRM_invalid_user_data |	Specified tag for user_data is not valid. |
| GRM_not_initialized |	The GRM module was not initialized. |
| GRM_relation_already_exists |	The relation being saved already exists. |
| GRM_relation_does_not_exist |	Relation does not exist. |
| GRM_undefined_relation_type |	The type you propose to delete does not exist. |

## Returned Tag Structure

Several GRM list functions return a list of tag quadruplets defined by the structure GRM_relation_t. The tag structure includes the tags of the primary_object, secondary_object, relation_type, and the user_data. The tag of a specific element of the structure can be referenced as follows:

| structure_name.primary | To reference the primary object. | 
| ---------------------- | -------------------------------- |
| structure_name.secondary | 	To reference the secondary object.| 
| structure_name.relation_type | 	To reference the relation type.| 
| structure_name.user_data | 	To reference the user data.| 

## Constraint Handler Registration and Execution

User-written constraint handlers should be registered in the USER_register_handlers user exit. This user exit is called during initialization for both interactive and ITK modes. This ensures that constraint handling is enforced in a consistent manner.

If constraint handlers are also registered in your ITK program (as well as in USER_register_handlers), then both sets of constraint handlers are called in the order they were registered. Since USER_register_handlers is called before your main ITK program, any handler you register in your ITK program is executed after the handlers registered using USER_register_handlers.

Additionally, it is possible that an internal Teamcenter handler is also registered for a give relation type and action combination. Such a handler is normally registered by a Teamcenter module or application to enforce certain rules before the user exit USER_register_handlers is called. Internal handlers are always executed before any user-written handler.

## Multi-Level Handlers

Several levels of constraint handlers can exist for a particular relation type and action combination. There are internal handlers which a Teamcenter developer may have registered. For example, a new module in Teamcenter (i.e., MYITEM) may register a set of internal handlers for creating a relation of type reference to ensure that the primary object is either an item or an item revision.

The System Administrator of an installation could also register handlers using the user exit USER_register_handlers to enforce the rule that the user must be the owner of the item or item revision to allow the creation of such a relation. Additionally, an ITK program can register another set of handlers to enforce the rule that the secondary object cannot be another item or item revision.

For multi-level handlers, the order of execution is as follows:

- internal pre-condition handler
- user exit pre-condition handler
- ITK program pre-condition handler
- internal pre-action handler
- user exit pre-action handler
- ITK program pre-action handler
- base action (the main operation performed by Teamcenter)
- internal post-action handler
- user exit post-action handler
- ITK program post-action handler
If a handler that executes first returns an error condition, then the other registered handlers will not execute. For example, if the internal pre-condition handler returns an error, none of the other handlers will execute; this includes the base action.

## Modules
- GRM Errors
- GRM Messages
- GRM Type
- Data Structures
- struct GRM_relation_s

## Defines
## define GRM_class_name_c   "ImanRelation"
## define GRM_relationtype_name_size_c   32

## Typedefs
typedef struct GRM_relation_s GRM_relation_t
typedef struct GRM_relation_s * GRM_relation_p_t
## Functions
- TCCORE_API int GRM_create_relation (tag_t primary_object, tag_t secondary_object, tag_t relation_type, tag_t user_data, tag_t *relation)
- TCCORE_API int GRM_save_relation (tag_t relation)
- TCCORE_API int GRM_delete_relation (tag_t relation)
- TCCORE_API int GRM_find_relation (tag_t primary_object, tag_t secondary_object, tag_t relation_type, tag_t *relation)
- TCCORE_API int GRM_list_relations (tag_t primary_object, tag_t secondary_object, tag_t relation_type, tag_t user_data, int *count, tag_t **relation_list)
- TCCORE_API int GRM_list_secondary_objects (tag_t primary_object, tag_t relation_type, int *count, GRM_relation_t **secondary_list)
- TCCORE_API int GRM_list_secondary_objects_only (tag_t primary_object, tag_t relation_type, int *count, tag_t **secondary_objects)
- TCCORE_API int GRM_list_primary_objects (tag_t secondary_object, tag_t relation_type, int *count, GRM_relation_t **primary_list)
- TCCORE_API int GRM_list_primary_objects_only (tag_t secondary_object, tag_t relation_type, int *count, tag_t **primary_objects)
- TCCORE_API int GRM_list_all_related_objects (tag_t match_object, int *count, GRM_relation_t **related_object_list)
- TCCORE_API int GRM_list_all_related_objects_only (tag_t match_object, int *count, tag_t **related_objects)
- TCCORE_API int GRM_ask_primary (tag_t relation, tag_t *primary_object)
- TCCORE_API int GRM_ask_secondary (tag_t relation, tag_t *secondary_object)
- TCCORE_API int GRM_ask_relation_type (tag_t relation, tag_t *relation_type)
- TCCORE_API int GRM_ask_user_data (tag_t relation, tag_t *user_data)
- TCCORE_API int GRM_set_user_data (tag_t relation, tag_t new_user_data)
- TCCORE_API int GRM_list_relation_types (int *count, tag_t **relation_type_list)
- TCCORE_API int GRM_find_relation_type (const char *relation_type_name, tag_t *relation_type)
- TCCORE_API int GRM_create_relation_type (const char *relation_type_name, tag_t *relation_type)
- TCCORE_API int GRM_delete_relation_type (tag_t relation_type)

## Define Documentation
## define GRM_class_name_c   "ImanRelation"

Definition at line 115 of file grm.h.


## define GRM_relationtype_name_size_c   32

Definition at line 116 of file grm.h.

### Examples:

1. TCCORE_API int GRM_ask_primary	(	tag_t 	relation,
tag_t * 	primary_object	 
)			
Returns the primary object tag of the specified relation.

Parameters:
- relation 	(I) Tag of the relation
- primary_object 	(O) Tag of the primary object in the specified relation

2. TCCORE_API int GRM_ask_relation_type	(	tag_t 	relation,
tag_t * 	relation_type	 
)			
Returns the relation type of the specified relation.

Parameters:
- relation 	(I) Tag of the relation
- relation_type 	(O) Tag of the relation type in the specified relation
