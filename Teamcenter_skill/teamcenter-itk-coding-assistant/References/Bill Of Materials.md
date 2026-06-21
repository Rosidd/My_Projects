# Bill of Materials
## Detailed Description
The Bill of Material (BOM) module is intended to give a consistent interface to the separate elements that make up a line in a BOM. The design assumes that you have a BOM window (this can be a printed report or a screen window) showing a BOM made up of BOM lines. Each BOM line shows attributes derived from Items, Item Revision, occurrences, and so on along with some attributes belonging to the BOM line itself and not any of the individual objects the line represents (i.e., is_packed).
The names of these attributes give a clue as to which object they have been derived from. The programmer using them can ignore this and treat them all as BOM line attributes. Although some attributes are standard (and listed in bom_attr.h) others are defined at run time (i.e., the note types on occurrences) and have to be found by inquiry.
 
 Since the BOM module keeps all of its windows synchronized, it is possible for changes to structure in one window to cause a BOM line in some other window to disappear. Therefore, be careful about storing BOM line tags when using multiple windows onto the same structure if that structure is open to editing.
 
## Common Return Values

| Return Value | Description |
| ------------ | ----------- |
| BOM_compare_invalid_dest	| The output parameter is set to an illegal value. |
| BOM_compare_invalid_mode |	The mode parameter is not set to one of the legal values. |
| BOM_compare_nested_roots |	The specified BOM lines are nested (i.e., one is an ancestor of the other). |
| BOM_compare_no_report |	No report output was generated because a report was not requested by BOM_compare. |
| VRULE_invalid_rule |	The supplied variant rule is not valid. |
  
## Modules
- BOM Attributes
- BOM Errors
- BOM Tokens
- BOM OVE Errors
- BOM Writer
## BOM Setup Functions
- BOM_API int BOM_init_module (void)
## BOM Window Functions
- BOM_API int BOM_create_window (tag_t *window)
- BOM_API int BOM_close_window (tag_t window)
- BOM_API int BOM_refresh_window (tag_t window)
- BOM_API int BOM_ask_window_config_rule (tag_t window, tag_t *config_rule)
- BOM_API int BOM_set_window_config_rule (tag_t window, tag_t config_rule)
- BOM_API int BOM_set_window_pack_all (tag_t window, logical pack_all)
- BOM_API int BOM_window_ask_state_logical (tag_t window, int state, logical *answer)
- BOM_API int BOM_set_window_top_line (tag_t window, tag_t item, tag_t item_revision, tag_t bv, tag_t *top_bom_line)
- BOM_API int BOM_set_window_top_line_using_occgrp (tag_t window, tag_t occGrp, tag_t *top_bom_line)
- BOM_API int BOM_set_window_top_line_using_proxy (tag_t window, tag_t proxy, tag_t *top_bom_line)
- BOM_API int BOM_set_window_top_line_bvr (tag_t window, tag_t bvr, tag_t *top_bom_line)
- BOM_API int BOM_ask_window_top_line (tag_t window, tag_t *top_bom_line)
- BOM_API int BOM_ask_window_ignore_ove_errors_on_expand (tag_t bom_window, logical *ignore)
- BOM_API int BOM_set_window_ignore_ove_errors_on_expand (tag_t bom_window, logical ignore)
- BOM_API int BOM_ask_window_ove_message_error_level (tag_t bom_window, int *level)
- BOM_API int BOM_set_window_ove_message_error_level (tag_t bom_window, int level)
- BOM_API int BOM_ask_window_active_arrangement (tag_t bom_window, tag_t *arrangement)
- BOM_API int BOM_set_window_active_arrangement (tag_t bom_window, tag_t arrangement)
- BOM_API int BOM_set_window_ignore_arrangements (tag_t bom_window, logical ignore)
- BOM_API int BOM_line_ask_used_arrangement (tag_t bomline, tag_t *arrangement)
- BOM_API int BOM_window_ask_effectivity_grprevs (tag_t window, int *count, tag_t **effGrpRevList)
- BOM_API int BOM_window_set_effectivity_grprevs (tag_t window, int n_effrevs, tag_t *effGrpRevList)
- BOM_API int BOM_window_ask_is_modified (tag_t window, logical *is_modified)
- BOM_API int BOM_save_window (tag_t window)
- BOM_API int BOM_window_revert_all_pending_edits (tag_t window)
- BOM_API int BOM_line_revert_pending_edits (int bom_line_count, tag_t *bom_lines)
- BOM_API int BOM_set_window_sort_compare_fn (tag_t window, void *function, void *client_data)
## BOM Line Functions
- BOM_API int BOM_line_ask_child_lines (tag_t bom_line, int *count, tag_t **children)
- BOM_API int BOM_line_ask_all_child_lines (tag_t bom_line, int *count, tag_t **children)
- BOM_API int BOM_line_subset_child_lines_occs (tag_t bom_line, int n_occs, const tag_t *occs, int *n_child_lines, tag_t **children)
- BOM_API int BOM_line_subset_child_lines_occ_notes (tag_t bom_line, tag_t occ_note_type, int n_note_patterns, const char **notes_patterns, int *n_child_lines, tag_t **children)
- BOM_API int BOM_line_ask_remote_object (tag_t bom_line, tag_t *remote_object)
- BOM_API int BOM_line_get_remote_children (tag_t bom_line, int *n_remote, tag_t **remote_children)
- BOM_API int BOM_line_cut (tag_t bom_line)
- BOM_API int BOM_line_move_to (tag_t new_parent, int count, tag_t *bom_lines)
- BOM_API int BOM_line_remove_level (int count, tag_t *bom_lines)
- BOM_API int BOM_line_split_occurrence (const char *quantity, tag_t bom_line)
- BOM_API int BOM_line_replace_in_context (tag_t bom_line, tag_t item_rev)
- BOM_API int BOM_line_insert_level (int count, tag_t *bom_lines, tag_t item, tag_t view_type)
- BOM_API int BOM_line_copy (tag_t new_parent, tag_t to_be_copied, tag_t view_type, tag_t *new_line)
- BOM_API int BOM_line_fix_broken_links (int count, const tag_t *broken_links, const tag_t *candidate_lines)
- BOM_API int BOM_line_find_broken_links (tag_t bom_line, logical quick_search, int *count, tag_t **broken_links)
- BOM_API int BOM_line_resequence (tag_t bom_line, int start_number, int incre_number, logical recursive)
- BOM_API int BOM_line_unload_below (tag_t line)
- BOM_API int BOM_line_add (tag_t bom_line, tag_t item_folder, tag_t item_revision_folder, tag_t bv, tag_t *new_line)
- BOM_API int BOM_line_add_with_occ_type (tag_t bom_line, tag_t item_folder, tag_t item_revision_folder, tag_t bv, char *occType, tag_t *new_line)
- BOM_API int BOM_line_add_gde (tag_t bomline, tag_t childGDE, char *occType, tag_t *newLine)
## BOM Occurrence Sequencing
- BOM_API int BOM_line_add_predecessor (tag_t bom_line, tag_t predline)
- BOM_API int BOM_line_remove_predecessor (tag_t bom_line, tag_t predline)
- BOM_API int BOM_line_replace (tag_t bom_line, tag_t item_folder, tag_t item_revision_folder, tag_t bv)
- BOM_API int BOM_line_change_to_replace (tag_t deletedBOMLine, tag_t addedBOMLine)
- BOM_API int BOM_line_is_replaceable (tag_t bom_line, logical *verdict)
- BOM_API int BOM_line_set_precise (tag_t bom_line, logical precise)
- BOM_API int BOM_line_pack (tag_t bom_line)
- BOM_API int BOM_line_unpack (tag_t bom_line)
- BOM_API int BOM_line_is_packed (tag_t bom_line, logical *verdict)
- BOM_API int BOM_line_replace_gde (tag_t gde_line, tag_t new_gde)
## BOM Attribute Functions
- Used to ask about attributes of a BOM line, and update some of them. After updating the attribute, BOM_save_window must be called to commit the change.
- BOM_API int BOM_line_list_attributes (int *count, int **attributes)
- BOM_API int BOM_line_look_up_attribute (const char *attribute_name, int *attribute)
- BOM_API int BOM_line_look_up_inherited_attr (const char *class_name, const char *attribute_name, int *attribute)
- BOM_API int BOM_line_ask_attribute_name (int attribute, char **attribute_name)
- BOM_API int BOM_line_ask_attribute_uname (int attribute, char **attribute_user_name)
- BOM_API int BOM_line_ask_attribute_mode (int attribute, int *attribute_mode)
- BOM_API int BOM_line_ask_attribute_ro (int attribute, logical *attribute_is_read_only)
- BOM_API int BOM_line_set_attribute_int (tag_t bom_line, int attribute, int value)
- BOM_API int BOM_line_ask_attribute_int (tag_t bom_line, int attribute, int *value)
- BOM_API int BOM_line_set_attribute_logical (tag_t bom_line, int attribute, logical value)
- BOM_API int BOM_line_ask_attribute_logical (tag_t bom_line, int attribute, logical *value)
- BOM_API int BOM_line_set_attribute_tag (tag_t bom_line, int attribute, tag_t value)
- BOM_API int BOM_line_ask_attribute_tag (tag_t bom_line, int attribute, tag_t *value)
- BOM_API int BOM_line_set_attribute_string (tag_t bom_line, int attribute, const char *value)
- BOM_API int BOM_line_ask_attribute_string (tag_t bom_line, int attribute, char **value)
- BOM_API int BOM_line_set_attribute_double (tag_t bom_line, int attribute, double value)
- BOM_API int BOM_line_ask_attribute_double (tag_t bom_line, int attribute, double *value)
## BOM Substitute Functions
- BOM_API int BOM_line_ask_has_substitutes (tag_t bom_line, logical *has_substitutes)
- BOM_API int BOM_line_ask_is_substitute (tag_t bom_line, logical *is_substitute)
- BOM_API int BOM_line_show_substitutes (tag_t bom_line)
- BOM_API int BOM_line_hide_substitutes (tag_t bom_line)
- BOM_API int BOM_line_list_substitutes (tag_t bom_line, int *n_substitutes, tag_t **substitute_lines)
- BOM_API int BOM_line_add_substitute (tag_t bom_line, tag_t item, tag_t item_revision, tag_t bom_view, tag_t *new_line)
- BOM_API int BOM_line_prefer_substitute (tag_t bom_line, logical *is_temporary)
- BOM_API int BOM_window_show_substitutes (tag_t bom_window)
- BOM_API int BOM_window_hide_substitutes (tag_t bom_window)
## BOM Window Variation Functions
- Common Return Values
- BOM_variant_error_condition - The new variant data triggered a variant rule check in one (or more) of the BOM windows being updated.
 
- BOM_API int BOM_window_ask_vrule (tag_t bom_window, tag_t *vrule, logical *modified)
- BOM_API int BOM_window_apply_full_vrule (tag_t bom_window, tag_t vrule)
- BOM_API int BOM_window_apply_partial_vrule (tag_t bom_window, tag_t vrule)
- BOM_API int BOM_window_show_variants (tag_t bom_window)
- BOM_API int BOM_window_hide_variants (tag_t bom_window)
## BOM Variant Data Functions
- BOM_API int BOM_new_variant_expression (tag_t v1, int opcode, tag_t v2, const char *str, tag_t *expr)
- BOM_API int BOM_set_variant_expression (tag_t expr, tag_t v1, int opcode, tag_t v2, const char *str)
- BOM_API int BOM_ask_variant_expression (tag_t expr, tag_t *v1, int *opcode, tag_t *v2, char **str)
- BOM_API int BOM_variant_expression_as_text (tag_t expr, char **str)
- BOM_API int BOM_new_variant_e_block (tag_t *block)
- BOM_API int BOM_ask_variant_e_block (tag_t block, int *n, tag_t **exprs)
- BOM_API int BOM_set_variant_e_block (tag_t block, int n, const tag_t *exprs)
- BOM_API int BOM_line_ask_variant_e_block (tag_t line, tag_t *block)
- BOM_API int BOM_line_set_variant_e_block (tag_t line, tag_t block)
- BOM_API int BOM_variant_e_block_add (tag_t veb, tag_t ve)
- BOM_API int BOM_variant_e_block_remove (tag_t veb, tag_t ve)
- BOM_API int BOM_variant_e_block_replace (tag_t veb, tag_t veOut, tag_t veIn)

## BOM Variant Rule Functions
- BOM_API int BOM_window_ask_variant_rule (tag_t window, tag_t *bomvariantlist)
- BOM_API int BOM_variant_rule_copy (tag_t src_bomvariantlist, tag_t dst_window, tag_t *dst_bomvariantlist)
- BOM_API int BOM_variant_rule_set_copy_action (int action)
- BOM_API int BOM_variant_rule_ask_copy_action (int *action)
- BOM_API int BOM_variant_rule_apply (tag_t bomvariantlist)
- BOM_API int BOM_variant_rule_apply_to (tag_t src_bomvariantlist, tag_t dst_bomvariantlist)
- BOM_API int BOM_variant_rule_delete (tag_t bomvariantlist)
- BOM_API int BOM_variant_rule_apply_full_vrule (tag_t bomvariantlist, tag_t vrule, logical *list_changed)
- BOM_API int BOM_variant_rule_apply_partial_vrule (tag_t bomvariantlist, tag_t vrule, logical *list_changed)
- BOM_API int BOM_variant_rule_ask_vrule (tag_t bomvariantlist, tag_t *vrule, logical *modified)
- BOM_API int BOM_variant_rule_find_option (tag_t bomvariantlist, tag_t item, const char *name, tag_t *option, tag_t *option_rev)
- BOM_API int BOM_variant_rule_find_options (tag_t bomvariantlist, tag_t item, const char *name, int *n_options, tag_t **options)
- BOM_API int BOM_variant_rule_ask_option_rev (tag_t bomvariantlist, tag_t option, tag_t *option_rev)
- BOM_API int BOM_variant_rule_ask_options (tag_t bomvariantlist, int *n, tag_t **options, tag_t **option_revs)
- BOM_API int BOM_variant_rule_set_option_value (tag_t bomvariantlist, tag_t option, int value)
- BOM_API int BOM_variant_rule_ask_option_value (tag_t bomvariantlist, tag_t option, tag_t *option_rev, int *value, int *how_set, char **where_set)
- BOM_API int BOM_variant_rule_unset_option_value (tag_t bomvariantlist, tag_t option)
- BOM_API int BOM_variant_rule_unset_option_values (tag_t bomvariantlist, int n_options, tag_t *options)
- BOM_API int BOM_variant_rule_clear_option_values (tag_t bomvariantlist)
- BOM_API int BOM_variant_rule_evaluate (tag_t bomvariantlist)
 
## BOM Variant Clause List Functions
- Common Return Values
- BOM_variant_invalid_cond_clause - The specified clause position is not valid.
- BOM_variant_invalid_operation - This operation cannot be performed on the given list of clauses.
- 
- BOM_API int BOM_variant_new_clause_list (tag_t bom_window, tag_t *clause_list)
- BOM_API int BOM_variant_condition_to_clause_list (tag_t bom_window, tag_t condition_ve, tag_t *clause_list)
- BOM_API int BOM_variant_join_clause_list (tag_t clause_list, tag_t *conditon_ve)
- BOM_API int BOM_variant_delete_clause_list (tag_t clause_list)
- BOM_API int BOM_variant_clause_append (tag_t clause_list, int join, tag_t option, int op, const char *value)
- BOM_API int BOM_variant_clause_insert (tag_t clause_list, int pos, int join, tag_t option, int op, const char *value)
- BOM_API int BOM_variant_clause_replace (tag_t clause_list, int pos, int join, tag_t option, int op, const char *value)
- BOM_API int BOM_variant_clause_delete (tag_t clause_list, int n_clauses, int pos[])
- BOM_API int BOM_variant_clause_move_up (tag_t clause_list, int n_clauses, int pos[])
- BOM_API int BOM_variant_clause_move_down (tag_t clause_list, int n_clauses, int pos[])
- BOM_API int BOM_variant_clause_toggle_brackets (tag_t clause_list, int n_clauses, int pos[])
- BOM_API int BOM_variant_clause_list_size (tag_t clause_list, int *n_clauses)
- BOM_API int BOM_variant_clause_list_text (tag_t clause_list, int *n_clauses, char ***text)
- BOM_API int BOM_variant_clause_text (tag_t clause_list, int pos, char **text)
- BOM_API int BOM_variant_clause_details (tag_t clause_list, int pos, int *join, tag_t *option, int *op, char **value)
- BOM_API int BOM_variant_clause_valid_ops (tag_t clause_list, int n_clauses, int pos[], int *op_flags)
- BOM_API int BOM_variant_clause_validate_ops (tag_t clause_list, logical auto_validate)

## BOM Modular Variants Functions
- Configuration
- This is the set of ITK functions required to configure a structure.
 
- BOM_line_ask_sos
- BOM_line_clear_sos
- BOM_sos_apply
- BOM_sos_apply_list
- BOM_sos_free
- BOM_window_ask_ove_messages
- BOM_line_ove_validate
- BOM_sos_ask_entries
- BOM_sos_ask_entry_<type>
- BOM_sos_set_entry_<type>
- BOM_sos_unset_entry
- BOM_option_ask_allowed_ints
- BOM_option_ask_allowed_reals
- BOM_option_ask_allowed_strings
 
## Authoring ITK
 
The following ITKs deal with the creation and editing of Modular Variants. It essentially provides a way to getting and setting MVL. MVL has 2 distinct areas - the option declaration statements and the language expressions. These are dealt with via separate functions in the ITK.
- BOM_line_ask_mvl_condition
- BOM_line_set_mvl_condition
- BOM_line_ask_mvl
- BOM_line_set_mvl
- BOM_module_list_options
- BOM_module_ask_option_text
- BOM_line_delete_option
- BOM_line_define_option

## Additional ITK

- BOM_option_where_declared
- BOM_option_where_used

- BOM_API int BOM_line_ask_sos (tag_t bom_line, tag_t *sos)
- BOM_API int BOM_line_clear_sos (tag_t bom_line, logical doUpdates)
- BOM_API int BOM_sos_apply (tag_t sos, logical doUpdates)
- BOM_API int BOM_sos_apply_list (int count, tag_t *sos, logical doUpdates)
- BOM_API int BOM_sos_free (tag_t sos)
- BOM_API int BOM_window_ask_ove_messages (tag_t bom_window, int *count, int **severities, char ***messages, tag_t **lines)
- BOM_API int BOM_line_ove_validate (tag_t line, logical recurse, int *count, int **error_types, tag_t **lines, int **options)
- BOM_API int BOM_decompose_ove_path (const char *path, int *count, char ***pathElements)
- BOM_API int BOM_sos_ask_entries (tag_t sos, int *count, int **options, char ***paths)
- BOM_API int BOM_sos_ask_entry_int (tag_t sos, int option, const char *path, int *value, int *how_set)
- BOM_API int BOM_sos_ask_entry_double (tag_t sos, int option, const char *path, double *value, int *how_set)
- BOM_API int BOM_sos_ask_entry_logical (tag_t sos, int option, const char *path, logical *value, int *how_set)
- BOM_API int BOM_sos_ask_entry_display (tag_t sos, int option, const char *path, char **value, int *how_set)
- BOM_API int BOM_sos_set_entry_int (tag_t sos, int option, const char *path, int value, int how_set)
- BOM_API int BOM_sos_set_entry_double (tag_t sos, int option, const char *path, double value, int how_set)
- BOM_API int BOM_sos_set_entry_logical (tag_t sos, int option, const char *path, logical value, int how_set)
- BOM_API int BOM_sos_set_entry_string (tag_t sos, int option, const char *path, const char *value, int how_set)
- BOM_API int BOM_sos_unset_entry (tag_t sos, int option, const char *path)
- BOM_API int BOM_option_describe (int option, char **item, char **option_name, char **desc, int *visibility, int *option_type, int *value_type, int *based_on, logical *has_default)
- BOM_API int BOM_ask_option_path (int option, char **path)
- BOM_API int BOM_option_ask_allowed_strings (int option, int *count, char ***values, char **default_value)
- BOM_API int BOM_option_ask_allowed_ints (int option, int *count, int **mins, int **maxs, int **range_types, int *default_value)
- BOM_API int BOM_option_ask_allowed_reals (int option, int *count, double **mins, double **maxs, int **range_types, double *default_value)
- BOM_API int BOM_option_ask_logical_default (int option, logical *default_value)
- BOM_API int BOM_line_ask_mvl_condition (tag_t line, char **condition)
- BOM_API int BOM_line_set_mvl_condition (tag_t line, const char *condition)
- BOM_API int BOM_line_ask_mvl (tag_t line, char **mvl)
- BOM_API int BOM_line_set_mvl (tag_t line, const char *mvl)
- BOM_API int BOM_module_list_options (tag_t window, const char *module_id, int *count, int **options)
- BOM_API int BOM_module_ask_option_text (int option, char **text)
- BOM_API int BOM_module_ask_option_handle (tag_t window, const char *module_id, const char *name, int *option)
- BOM_API int BOM_line_define_option (tag_t line, const char *text)
- BOM_API int BOM_line_delete_option (tag_t line, int option)
- BOM_API int BOM_line_modify_option (tag_t line, int option, const char *text)
## SOS Storage and Retrieval
- BOM_API int BOM_sos_db_read (tag_t db_sos, tag_t config)
- BOM_API int BOM_sos_db_create (const char *db_sos_name, tag_t config, tag_t *db_sos)
- BOM_API int BOM_sos_db_set (tag_t db_sos, tag_t config)
- BOM_API int BOM_sos_db_create_partial (const char *db_sos_name, tag_t config, int count, tag_t *items, char **options, logical *isModular, tag_t *db_sos)
- BOM_API int BOM_sos_db_set_partial (tag_t db_sos, tag_t config, int count, tag_t *items, char **options, logical *isModular)
- BOM_API int BOM_sos_db_contents (tag_t db_sos, int *count, tag_t **items, char ***options, int **optionTypes, int **valueTypes, int **howSet, char ***values)
- BOM_API int BOM_sos_db_option_query (int n, tag_t *items, char **options, int *n_matches, tag_t **matches)
- BOM_API int BOM_sos_db_query (int n, tag_t *items, char **options, int *ops, int *valueTypes, char **lowValues, char **highValues, int *n_matches, tag_t **matches)
## BOM Variant configuration functions
- BOM_API int BOM_create_variant_config (tag_t bom_vrule, int count, tag_t *bomsoslist, tag_t *bom_variant_config)
- BOM_API int BOM_create_window_variant_config (tag_t bom_window, int mode, tag_t *bom_variant_config)
- BOM_API int BOM_create_bomline_variant_config (tag_t bom_line, int mode, tag_t *bom_variant_config)
- BOM_API int BOM_delete_variant_config (tag_t bom_variant_config)
- BOM_API int BOM_variant_config_apply (tag_t bom_variant_config)
- BOM_API int BOM_variant_config_clear (tag_t bom_variant_config)
- BOM_API int BOM_variant_config_evaluate (tag_t bom_variant_config)
- BOM_API int BOM_variant_config_copy (tag_t source_config, logical deepCopy, tag_t *new_config)
- BOM_API int BOM_set_variant_config_bomvrule (tag_t bom_variant_config, tag_t bom_vrule, int mode)
- BOM_API int BOM_set_variant_config_bomsos (tag_t bom_variant_config, tag_t bom_line, tag_t bom_sos, int mode)
- BOM_API int BOM_ask_variant_config (tag_t bom_variant_config, tag_t *bom_vrule, int *count, tag_t **bomsoslist)
- BOM_API int BOM_ask_variant_config_context (tag_t bom_variant_config, tag_t *bom_window, tag_t *root_bom_line)
## BOM Compare Functions
Common Return Values
- BOM_no_current_compare - The BOMCompare has not yet been supplied to BOM_compare_execute (or BOM_compare, for the standard internal compare), or an error occurred during the last such call that invalidated the comparison.
- BOM_no_such_bom_compare_mode - No mode by that name yet registered.

- BOM_API int BOM_compare_create (tag_t *bomcompare)
- BOM_API int BOM_compare_delete (tag_t bomcompare)
- BOM_API int BOM_compare_ask_modes (logical visible_only, int *n_modes, char ***mode_names)
- BOM_API int BOM_compare_visit_engine (tag_t bomcompare, BOM_compare_engine_visitor_t *enter_engine, BOM_compare_engine_visitor_t *leave_engine, BOM_compare_set_visitor_t *visit_set, void *user_data)
- BOM_API int BOM_compare_ask_mode (tag_t bomcompare, char **mode_name)
- BOM_API int BOM_compare_ask_output_mode (tag_t bomcompare, int *output_mode)
- BOM_API int BOM_compare_ask_root_bomlines (tag_t bomcompare, tag_t *bomline1, tag_t *bomline2)
- BOM_API int BOM_compare_ask_engine_root_bomlines (tag_t bomcompareengine, tag_t *bomline1, tag_t *bomline2)
- BOM_API int BOM_compare_define_mode (const char *mode_name, int traversal_mode, tag_t compare_desc, logical visible, logical autopack, logical virtualunpack)
- BOM_API int BOM_compare_ask_mode_info (const char *mode_name, int *traversal_mode, tag_t *compare_desc, logical *visible, logical *autopack, logical *virtualunpack)
- BOM_API int BOM_compare_set_visibility (const char *mode_name, logical visible)
- BOM_API int BOM_compare_reports_unchanged (const char *mode_name, logical *reports_unchanged)
- BOM_API int BOM_compare_set_rpt_unchanged (const char *mode_name, logical report_unchanged)
- BOM_API int BOM_compare (tag_t line1, tag_t line2, int mode, int output)
- BOM_API int BOM_compare_execute (tag_t bomcompare, tag_t bomline1, tag_t bomline2, const char *mode_name, int output_to)
- BOM_API int BOM_compare_clear (tag_t compare_context)
- BOM_API int BOM_compare_suppress (tag_t compare_context, int output)
- BOM_API int BOM_compare_list_bomlines (tag_t cmp_item, int *count1, tag_t **bomline_list1, int *count2, tag_t **bomline_list2)
- BOM_API int BOM_compare_ask_difference (tag_t cmp_item, int *diff_flags)
- BOM_API int BOM_compare_ask_qty (tag_t cmp_item, double *qty1, double *qty2)
- BOM_API int BOM_compare_ask_rev (tag_t cmp_item, char **rev1, char **rev2)
- BOM_API int BOM_compare_ask_seqno (tag_t cmp_item, char **seqno)
- BOM_API int BOM_compare_list_diffs (tag_t line, int *diff_count, tag_t **diff_lines, int **diff_flags)
- BOM_API int BOM_compare_list_diffs_context (tag_t line, tag_t context, int *diff_count, tag_t **diff_lines, int **diff_flags)
- BOM_API int BOM_compare_report (tag_t compare_context, int *report_length, char ***report_lines, tag_t **report_items)
- BOM_API int BOM_compare_report_size (tag_t compare_context, int *report_width, int *column_spacer, int *column_count, int **column_width)
- BOM Snapshot Folder creation functions
- BOM_API int BOM_create_snapshot (tag_t bom_window, const char *name, const char *desc, tag_t *snapshot_folder)
## BOM Baseline Functions
- BOM_API int BOM_create_baseline (tag_t bom_window, const char *name, const char *desc, const char *rel_proc_name, const char *jobName, const char *jobDescription, tag_t *baseline_rev)
- BOM_API int BOM_create_baseline_with_baseline_label (tag_t bom_window, const char *name, const char *desc, const char *rel_proc_name, const char *jobName, const char *baseline_label_name, const char *jobDescription, tag_t *baseline_rev)
- BOM_API int BOM_dryrun_baseline (tag_t bom_window, const char *rel_proc_name, char **logFileName, char **fullLogFileName, logical *error_registered)
- BOM Post-Configuration functions
- BOM_API int BOM_line_force_config (tag_t bomline, logical force_parents_too, int override_status)
- BOM_API int BOM_window_clear_all_forced_configs (tag_t bomwindow)
- BOM_API int BOM_start_forced_config (tag_t *transaction)
- BOM_API int BOM_end_forced_config (tag_t transaction)
## BOM Publish Functions
- BOM_API int BOM_create_publish_link (const char *name, const char *type, tag_t source_line, int target_count, const tag_t *target_lines, tag_t *publishLink)
- BOM_API int BOM_publishlink_add_targets (tag_t source_line, int target_count, const tag_t *target_lines, tag_t *publishLink)
- BOM_API int BOM_publishlink_delete_targets (tag_t source_line, int target_count, const tag_t *target_lines, tag_t *publishLink)
- BOM_API int BOM_publishlink_find_targets_in_window (tag_t source_line, tag_t target_bom_window, int *targets_count, tag_t **target_lines)
- BOM_API int BOM_publish_data (tag_t source_line, int target_count, const tag_t *target_lines, const int data_flags, const char *publishLinkName, const char *publishLinkTypeName, tag_t *publishLink)
- BOM_API int BOM_delete_publishlink_for_source (tag_t source_line)
- BOM_API int BOM_publishlink_find_source_in_window (tag_t target_line, tag_t source_bom_window, tag_t *source_line)
- BOM_API int BOM_publishlink_delete_target (tag_t target_line, tag_t *publishLink)
- BOM_API int BOM_publishlink_ask_source_context_bv (tag_t target_line, tag_t *source_bom_view)
- BOM_API int BOM_ask_publishlink_for_source (tag_t source_line, tag_t *publish_link)
- BOM_API int BOM_ask_publishlink_for_target (tag_t target_line, tag_t *publish_link)

## Functions
- BOM_API int BOM_exit_module (void)
- BOM_API int BOM_set_pack_compare (void *function)
- BOM_API int BOM_line_ask_packed_lines (tag_t bom_line, int *count, tag_t **packed)
- BOM_API int BOM_line_list_predecessors (tag_t bom_line, int *count, tag_t **pred)
- BOM_API int BOM_line_ask_window (tag_t bom_line, tag_t *window)
- BOM_API int BOM_line_ask_load_state (tag_t bom_line, int *load_state)
- BOM_API int BOM_update_pse (tag_t bvr)
- BOM_API int BOM_modified_bvr (tag_t line)
- BOM_API int BOM_create_option (tag_t owning_item, const char *name, const char *description, int mode, tag_t *option, tag_t *option_rev)
- BOM_API int BOM_new_option (tag_t itemrev, const char *optname, const char *optdesc, int mode, tag_t *option, tag_t *optionrev, tag_t *ve, tag_t *veb)
- BOM_API int BOM_declare_option (tag_t itemrev, tag_t optionrev, tag_t *ve, tag_t *veb)
- BOM_API int BOM_ask_option_data (tag_t option, tag_t *owning_item, char **name, char **description)
- BOM_API int BOM_option_where_declared (const char *item, const char *option, int *count, tag_t **item_revs)
- BOM_API int BOM_option_where_used (const char *item, const char *option, int *count, tag_t **objs)
- BOM_API int BOM_set_option_data (tag_t option, const char *name, const char *description)
- BOM_API int BOM_revise_option (tag_t revision_in, tag_t *new_revision)
- BOM_API int BOM_ask_option_rev_mode (tag_t option_rev, int *mode)
- BOM_API int BOM_ask_option_of_rev (tag_t option_rev, tag_t *option)
- BOM_API int BOM_list_option_rev_values (tag_t option_rev, int *n_values, int **indexes)
- BOM_API int BOM_ask_option_rev_value (tag_t option_rev, int an_index, char **value)
- BOM_API int BOM_set_option_rev_value (tag_t option_rev, int an_index, const char *value)
- BOM_API int BOM_add_option_rev_value (tag_t option_rev, const char *value, int *an_index)
- BOM_API int BOM_remove_option_rev_value (tag_t option_rev, int an_index)
- BOM_API int BOM_ask_index_of_opt_rev_value (tag_t option_rev, const char *value, int *an_index)
- BOM_API int BOM_window_ask_options (tag_t window, int *n_options, tag_t **options, tag_t **option_revisions)
- BOM_API int BOM_window_set_option_value (tag_t window, tag_t option, int value)
- BOM_API int BOM_window_unset_option_value (tag_t window, tag_t option)
- BOM_API int BOM_window_ask_option_value (tag_t window, tag_t option, tag_t *option_rev, int *value, int *how_set, char **where_set)
- BOM_API int BOM_window_find_option (tag_t window, tag_t item, const char *option_name, tag_t *option, tag_t *option_rev)
- BOM_API int BOM_update_for_variants_on_occ (tag_t parent_bvr, tag_t occurrence)
- BOM_API int BOM_update_for_variants_on_itemrev (tag_t item_rev)
- BOM_API int BOM_update_for_variants_on_bomline (tag_t bomline)
- BOM_API int BOM_variant_expr_load_if (tag_t cond_ve, tag_t *load_if_ve)
- BOM_API int BOM_variant_expr_error_if (tag_t cond_ve, const char *warning_text, tag_t *error_if_ve)
- BOM_API int BOM_variant_expr_set_if (tag_t cond_ve, tag_t option, int value, tag_t *set_if_ve, tag_t *assign_ve)
- BOM_API int BOM_variant_expr_default (tag_t option, int value, tag_t *default_ve)
- BOM_API int BOM_variant_expr_split_load_if (tag_t load_if_ve, tag_t *cond_ve)
- BOM_API int BOM_variant_expr_split_error_if (tag_t error_if_ve, char **warning_text, tag_t *cond_ve)
- BOM_API int BOM_variant_expr_split_set_if (tag_t set_if_ve, tag_t *option, int *value, tag_t *cond_ve)
- BOM_API int BOM_variant_expr_split_default (tag_t default_ve, tag_t *option, int *value)
- BOM_API int BOM_line_create_vi (tag_t line, logical is_linked_to_generic_component, const char *item_id, const char *item_name, const char *type_name, const char *rev_id, tag_t *new_item, tag_t *new_rev)
- BOM_API int BOM_line_configure_in_vi (tag_t line, tag_t variant_item)
- BOM_API int BOM_window_ask_generic_components (tag_t window, int *generic_component_count, tag_t **generic_component_lines)
- BOM_API int BOM_line_ask_can_search_for_vi_from_parent (tag_t line, logical *reuseIdIsPossible)
- BOM_API int BOM_line_map_vi_requirements_from_parent (tag_t line, int n, tag_t *items, char **options, int *ops, int *valueTypes, char **lowValues, char **highValues, int *n_out, tag_t **items_out, char ***options_out, int **ops_out, int **valueTypes_out, char ***lowValues_out, char ***highValues_out)
- BOM_API int BOM_line_is_stopped (tag_t line, logical *is_stopped)
- BOM_API int BOM_line_set_stop (tag_t line)
- BOM_API int BOM_line_clear_stop (tag_t line)
- BOM_API int BOM_line_clear_all_stops (tag_t line)
- BOM_API int BOM_line_assign_child_line (tag_t line, tag_t sourceLine, char *occType, tag_t *newChildLine)
- BOM_API int BOM_window_shows_unconfigured (tag_t window, logical *shows_unconfigured)
- BOM_API int BOM_window_show_unconfigured (tag_t window)
- BOM_API int BOM_window_hide_unconfigured (tag_t window)
- BOM_API int BOM_window_filter_unconfigured_classic_variants (tag_t window)
- BOM_API int BOM_window_filters_unconfigured_classic_variants (tag_t window, logical *filter_unconfigured)
- BOM_API int BOM_window_set_closure_rule (tag_t window, tag_t closure_rule, int n_variables, char **variable_names, char **variable_values)
- BOM_API int BOM_window_shows_gcs_cps (tag_t window, logical *shows_gcs_cp)
- BOM_API int BOM_window_show_gcs_cps (tag_t window)
- BOM_API int BOM_window_hide_gcs_cps (tag_t window)
- BOM_API int BOM_window_shows_suppressed (tag_t window, logical *shows_suppressed)
- BOM_API int BOM_window_show_suppressed (tag_t window)
- BOM_API int BOM_window_hide_suppressed (tag_t window)
- BOM_API int BOM_create_window_from_snapshot (tag_t snapshot_folder, tag_t *bom_window)
- BOM_API int BOM_line_ask_attribute_external (int attribute, logical *attribute_is_external)
- BOM_API int BOM_writer_new_output_file (BOM_writer_output **p)
- BOM_API int BOM_writer_new_output_smstring (BOM_writer_output **p)
- BOM_API int BOM_writer_new_format_empty (BOM_writer_format **p)
- BOM_API int BOM_writer_new_format_ajt (BOM_writer_format **p)
- BOM_API int BOM_writer_new_format_plmxml (BOM_writer_format **p)
- BOM_API int BOM_writer_new_format_flatten (BOM_writer_format **p)
- BOM_API int BOM_writer_new_traversal (BOM_writer_traversal **p)
- BOM_API int BOM_writer_write_bomwindow (tag_t bom_window, BOM_writer_output *output_p, BOM_writer_format *format_p, BOM_writer_traversal *traversal_p)
- BOM_API int BOM_writer_get_plmxml_builders (int *count, char ***names, char ***descriptions)
- BOM_API int BOM_writer_delete (void *block)
- BOM_API int BOM_window_show_incremental_changes (tag_t bom_window)
- BOM_API int BOM_window_hide_incremental_changes (tag_t bom_window)
- BOM_API int BOM_set_window_config_context (tag_t window, tag_t config_context)
- BOM_API int BOM_window_get_bomline_from_apprPathNode (tag_t window, tag_t pathNode, tag_t intermediateParentLine, tag_t *pathNodeBomLine)
- BOM_API int BOM_line_create_add_ice (tag_t line, tag_t *new_ice)
- BOM_API int BOM_line_create_remove_ice (tag_t line, tag_t *new_ice)
- BOM_API int BOM_line_remove_incremental_changes (tag_t line, int n, tag_t *ices)
- BOM_API int BOM_line_list_related_substitutes (tag_t bom_line, int *n_items, tag_t **related_occs, tag_t **related_items)
- BOM_API int BOM_line_remove_related_substitutes (int n_lines, tag_t *lines)
- BOM_API int BOM_line_relate_substitutes (int num_of_lines, tag_t *bom_lines, tag_t *substitute_set)
- BOM_API int BOM_line_add_optional_item (tag_t bom_line, tag_t item, tag_t rev, tag_t bomview)
- BOM_API int BOM_line_remove_optional_item (tag_t bom_line, tag_t item, tag_t rev, tag_t bomview)
- BOM_API int BOM_line_ask_optional_items (tag_t bom_line, int *count, tag_t **opt_items, tag_t **opt_views)
- BOM_API int BOM_window_show_occ_type_filter (tag_t window_tag)
- BOM_API int BOM_window_hide_occ_type_filter (tag_t window_tag)
- BOM_API int BOM_window_set_occ_type_filter (tag_t window_tag, int count, char **typeList)
- BOM_API int BOM_window_get_occ_type_filter (tag_t window_tag, int *count, char ***typeList)
- BOM_API int BOM_line_create_vi_structures (tag_t line, logical is_linked_to_generic_component, tag_t *new_item, tag_t *new_rev)
- BOM_API int BOM_ok_to_modify_obj_in_ic (tag_t window_tag, tag_t object_tag, logical *modifiable)
- BOM_API int BOM_world_newIrfWhereConfigured (tag_t rev)
- BOM_API int BOM_line_find_candidates_with_fix_option (int n_broken_links, tag_t *broken_links, int n_scope, tag_t *scope, int n_properties, char **properties, int n_operators, char **operators, tag_t revision_rule, logical quick_search, logical auto_fix, int **n_candidates, tag_t **candidates)
- BOM_API int BOM_line_create_rollup_report (tag_t bomline, tag_t rollup_template, tag_t folder, const char *name, const char *description, tag_t *report_dataset)
- BOM_API int BOM_verify_part_structure (tag_t line, int *cntCompleteLines, tag_t **completeLinesTags, int *cntIncompleteLines, tag_t **incompleteLinesTags, int *cntSkippedLines, tag_t **skippedLinesTags)
- BOM_API int BOM_export_configured_nx_assembly (tag_t bomLine, const char *namingFormat, int noOfValidExcludes, const tag_t *excludedTags, char **zipFileTicket, char **logFileTicket)
- BOM_API int BOM_line_get_child_bomlines_from_clone_stable_uid (tag_t bom_line, int countin, char **clone_stable_uids, int *count, tag_t **children)
- BOM_API int BOM_line_find_preferred_JT_refset (tag_t bom_line, tag_t item_revision, logical ignore_overrides, tag_t *jtfile, char **refset_name, logical *jt_override)
- BOM_API int BOM_line_remove_absocc_property (tag_t bomLine, char *propertyName, tag_t contextBomLine)
- BOM_API int BOM_line_remove_absocc_relation (tag_t lineTag, tag_t sourceApn, tag_t relation)
- BOM_API int BOM_line_ask_absocc_relation (tag_t lineTag, tag_t sourceApn, char *relName, logical configuredOnly, int *relCount, tag_t **relations)
- BOM_API int BOM_line_replace_absocc_relation (tag_t lineTag, tag_t sourceApn, tag_t relation, tag_t newSecondary, tag_t *newRelation)
- BOM_API int BOM_line_add_absocc_relation (tag_t lineTag, tag_t relType, tag_t secObject, tag_t *newRelation)
- BOM_API int BOM_window_ask_absocc_context (tag_t window, tag_t *rootLine)
- BOM_API int BOM_window_set_absocc_context (tag_t window, tag_t rootLine)
- BOM_API int BOM_window_ask_absocc_edit_mode (tag_t window, logical *absOccEditMode)
- BOM_API int BOM_window_set_absocc_edit_mode (tag_t window, logical absOccEditMode)
- BOM_API int BOM_line_ask_unit_occurrence_effectivity (tag_t bomline, logical intersectWithConfigurationEff, logical *occEffExists, logical *isAlwaysEffective, int *effyInfoCount, WSOM_effectivity_info_t ***effectivityInfo)
- BOM_API int BOM_create_bomsetlines_for_input_lines (BOM_bomset_create_criteria_t bomset_create_criteria, tag_t *input_lines, int input_lines_count, int *bomset_count, BOM_bomset_input_info_t **bomset_input_info)
- BOM_API int BOM_expand_bomset_lines (BOM_bomset_input_info_t bomset_input_info, BOM_bomset_output_info_t *bomset_output_info)
- BOM_API int BOM_item_module_list_options (tag_t window, tag_t item, int *count, int **options)
- Gets the list of option names on the item corresponding to the bom line.
- BOM_API int BOM_item_ask_option_handle (tag_t window, const tag_t item, const char *name, int *option)
- Returns the Option id for the given item and Option name.
- BOM_API int BOM_option_describe2 (int option, tag_t *item, char **option_name, char **desc, int *visibility, int *option_type, int *value_type, int *based_on, logical *has_default)
- Returns the details for an Option defined on item.
- BOM_API int BOM_option_where_declared2 (const tag_t item, const char *option, int *count, tag_t **item_revs)
- For the given Item returns the item revision on which Option is declared.
- BOM_API int BOM_option_where_used2 (const tag_t item, const char *option, int *count, tag_t **objs)
- For the given Item returns the item revision on which Option is Used.
