# Naming Rule (nr.h) [Properties]
## Detailed Description
Naming Rules allow the site to provide naming pattern validation for various user input fields.
The set of ITK given here accesses NameRule, NameField and NameCounter classes, which can be used to validate and generate ids based on specific patterns.

| NameRule Class attributes | NameField Class attributes | NameCounter Class attributes |
| ------------------------- | -------------------------- | -----------------------------|
| rule_name |	type_name |	counter_name |
| patterns[] |	property_name |	no_of_chars |
| autogen |	field_case |	char_type |
| counter_tags |	rule_tag |	start_pos |
| | | init_value |
| | | max_value |
| | | next_id |


## Modules
- NR Errors
## Naming Rule Checker
The Naming Rule Checker enables the Assign buttons for Item IDs and Revisions and Dataset IDs and Revisions, to use the Naming rule patterns as templates. Also, the i-Man components for Name Rule and NameField will be created to allow Portal to access the Naming Rules.
- PROPERTY_API int NR_next_item_id (const char *type_name, char **next_id)
- PROPERTY_API int NR_next_rev_id (const char *type_name, tag_t item_tag, char **next_id)
- PROPERTY_API int NR_next_rev_id_from_alt_rule (const char *type_name, const char *rule_suffix, tag_t item_tag, const char *base_rev_id, char **next_id)
- PROPERTY_API int NR_next_alt_id (const char *preferred_type_name, const char *default_type_name, tag_t parent_tag, char **next_id)
- PROPERTY_API int NR_next_dataset_id (const char *ds_type, char **next_id)
- PROPERTY_API int NR_next_dataset_rev_id (const char *ds_type, const char *ds_id, char **next_id)
- PROPERTY_API int NR_validate_field (const char *type_name, const char *property_name, char *field_value)
- PROPERTY_API logical NR_match_revid_altrule (const char *type_name, const char *revid, const char *suffixrule)
- PROPERTY_API int NR_is_name_matching_pattern (const char *pattern, const char *string, logical *is_matched)
- PROPERTY_API int NR_next_value (const char *typeName, const char *propertyName, const tag_t itemTag, const char *dsId, const char *preferredTypeName, const char *defaultTypeName, const tag_t parentTag, const char *ruleSuffix, const char *baseRevId, char **nextId)
- PROPERTY_API int NR_next_values (const char *typeName, int quantity, const char *propertyName, const tag_t itemTag, const char *dsId, const char *preferredTypeName, const char *defaultTypeName, const tag_t parentTag, const char *ruleSuffix, const char *baseRevId, char ***nextId, logical *isNRWithoutAutogen)
- PROPERTY_API int NR_next_value2 (const char *typeName, const char *propertyName, const tag_t itemTag, const char *dsId, const char *preferredTypeName, const char *defaultTypeName, const tag_t parentTag, const char *ruleSuffix, const char *baseRevId, char **nextId, logical *isNRWithoutAutogen)
- PROPERTY_API int NR_pattern_next_value (const char *typeName, const char *propertyName, const tag_t itemTag, const char *dsId, const char *preferredTypeName, const char *defaultTypeName, const tag_t parentTag, const char *ruleSuffix, const char *baseRevId, const char *pattern, char **nextId)
- PROPERTY_API int NR_pattern_next_values (const char *typeName, int quantity, const char *propertyName, const tag_t itemTag, const char *dsId, const char *preferredTypeName, const char *defaultTypeName, const tag_t parentTag, const char *ruleSuffix, const char *baseRevId, const char *pattern, char ***nextIds)
- PROPERTY_API int NR_rule_desc_with_counters (tag_t rule_tag, char rule_name[WSO_name_size_c+1], int *n_patterns, char ***patterns, logical **autogen, int **n_counters, tag_t ***counter_tags)
- PROPERTY_API int NR_rule_desc_with_counters2 (tag_t rule_tag, char **rule_name, int *n_patterns, char ***patterns, logical **autogen, int **n_counters, tag_t ***counter_tags)
- PROPERTY_API int NR_ask_counter_details (tag_t counter_tag, char **counter_name, int *no_of_chars, int *start_pos, char **char_type, char **start_value, char **max_value)
- PROPERTY_API int NR_revision_naming_rule_desc (tag_t rule_tag, char rule_name[WSO_name_size_c+1], logical *exclude_skip_letters, int *init_rev_type, char **init_rev_start, char **init_rev_desc, int *sec_rev_type, char **sec_rev_start, char **sec_rev_desc, int *suppl_rev_format, char **suppl_rev_desc)
- PROPERTY_API int NR_revision_naming_rule_desc2 (tag_t rule_tag, char **rule_name, logical *exclude_skip_letters, int *init_rev_type, char **init_rev_start, char **init_rev_desc, int *sec_rev_type, char **sec_rev_start, char **sec_rev_desc, int *suppl_rev_format, char **suppl_rev_desc)
- PROPERTY_API int NR_revision_naming_rule_extent (int *n_tags, tag_t **rule_tags)
- PROPERTY_API int NR_find_revision_naming_rule (char *rule_name, tag_t *rule_tag)
- PROPERTY_API int NR_revision_naming_rule_attach_extent (int *n_tags, tag_t **field_tags)
- PROPERTY_API int NR_revision_name_rule_attach_desc (tag_t attach_tag, char **type_name, tag_t *rule_tag, int *field_case)
- PROPERTY_API int NR_ask_revision_naming_rule_and_case (char *type_name, tag_t *rule_tag, int *field_case)
- PROPERTY_API int NR_next_rev_options (char *item_type, tag_t item_rev, char **init_rev_option, char **sec_rev_option, char **suppl_rev_option)
- PROPERTY_API int NR_get_rev_rule_attach (const char *type_name, tag_t *revNameRuleAttachTag)
- PROPERTY_API int NR_validate_rev_id_field (const char *type_name, const char *property_name, char *field_value, const char *item_id)
- PROPERTY_API int NR_validate_rev_id_field2 (const char *type_name, const char *property_name, char *field_value, const tag_t item_tag)
## Defines

define NR_CASE_MIXED   0
define NR_CASE_LOWER   1
define NR_CASE_UPPER   2

## Functions

- PROPERTY_API int NR_rule_extent (int *n_tags, tag_t **rule_tags)
- PROPERTY_API int NR_find (char *rule_name, tag_t *rule_tag)
- PROPERTY_API int NR_field_extent (int *n_tags, tag_t **field_tags)
- PROPERTY_API int NR_rule_desc (tag_t rule_tag, char rule_name[WSO_name_size_c+1], int *n_patterns, char ***patterns, logical *autogen, int *n_counters, tag_t **counter_tags)
- PROPERTY_API int NR_rule_desc2 (tag_t rule_tag, char **rule_name, int *n_patterns, char ***patterns, logical *autogen, int *n_counters, tag_t **counter_tags)
- PROPERTY_API int NR_ask_counter_values (tag_t counter_tag, char **counter_name, int *no_of_chars, int *start_pos, char **char_type, char **start_value, char **max_value, char **next_id)
- PROPERTY_API int NR_field_desc (tag_t field_tag, char **type_name, char **property_name, tag_t *rule_tag, int *field_case)
- PROPERTY_API int NR_ask_rule_and_case (char *type_name, char *property_name, tag_t *rule_tag, int *field_case)

## Examples:
1. PROPERTY_API int NR_ask_counter_details	(	tag_t 	counter_tag,
char ** 	counter_name,
int * 	no_of_chars,
int * 	start_pos,
char ** 	char_type,
char ** 	start_value,
char ** 	max_value	 
)			
- Get all of the values of a NameCounter.

Parameters:
- counter_tag 	(I) The tag of the NameCounter to retrieve values from
- counter_name 	(OF) The name of the counter
- no_of_chars 	(O) The width of this counter
- start_pos 	(O) The starting position (offset) of this counter in its parent pattern
- char_type 	(OF) Type of counter
- start_value 	(OF) The initial value for this counter
- max_value 	(OF) The maximum value for this counter

2. PROPERTY_API int NR_ask_revision_naming_rule_and_case	(	char * 	type_name,
tag_t * 	rule_tag,
int * 	field_case	 
)			
- Get the field case and the corresponding rule tag of the attachment

Parameters:
- type_name 	(I) The Item Type that the rule applies to
- rule_tag 	(O) Tag of Revision Naming Rule object
- field_case 	(O) The case to automatically translate the property fields contents
- (NR_CASE_MIXED, NR_CASE_LOWER, NR_CASE_UPPER)
