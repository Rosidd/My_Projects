# Application Encapsulation

## Dataset (dataset.h)
[Application Encapsulation]
Detailed Description
A complete list of named references defined for a tool may not necessarily exist in all instances of datasets created by that tool or datasets that can be read by that tool.

Warning:
Do not pass the const char reference_name[AE_reference_size_c + 1] argument to AE_add_dataset_named_ref or AE_remove_dataset_named_ref by handing to them a character pointer which points to a reference name and which is returned by another Teamcenter Engineering routine (like a pointer returned by AE_ask_dataset_named_ref or by other ITK routines). Unpredictable results can happen this way which can be difficult to trace down. We strongly recommend that you always make a copy of the reference name into a local character array before passing it to these two ITK functions as follows:
    your_ITK_routine()
    {
        char my_local_copy_refname[AE_reference_size_c + 1];
        char my_other_refname[AE_reference_size_c + 1];

        tag_t my_dataset;
        tag_t my_other_dataset;

        AE_reference_type_t my_ref_type;
        AE_reference_type_t my_other_ref_type;

        tag_t my_ref_object;
        tag_t my_other_ref_object;

        .... other stuff ...

        strcpy(my_local_copy_refname, "UGPART");
        AE_add_dataset_named_ref(my_dataset, my_local_copy_refname, myref_type, my_ref_object);

        strcpy(my_local_copy_refname, "CLS");
        AE_add_dataset_named_ref(my_dataset, my_local_copy_refname, my_other_ref_type, my_other_ref_object);

        .... other stuff ...

        strcpy(my_other_refname, "EXPERT");
        AE_ask_dataset_named_ref(my_other_dataset, my_other_refname, & my_other_ref_type, & my_other_ref_object);

        strcpy(my_local_copy_refname, my_other_refname);
        AE_add_dataset_named_ref(my_dataset, my_local_copy_refname, my_other_ref_type, my_other_ref_object);

        .... other stuff ...

        strcpy(my_local_copy_refname, "UGPART");
        AE_remove_dataset_named_ref(my_dataset, my_local_copy_refname);

        .... other stuff ...

    }
AE_reference_type_t can be either AE_ASSOCIATION or AE_PART_OF.


### Modules
Dataset Messages
Revision Anchor
- AE_API int AE_replace_dataset_named_ref (tag_t dataset, tag_t old_referenced_object, const char reference_name[AE_reference_size_c+1], AE_reference_type_t reference_type, tag_t previously_saved_object)
- AE_API int AE_replace_dataset_named_ref2 (tag_t dataset, tag_t old_referenced_object, const char *reference_name, AE_reference_type_t reference_type, tag_t previously_saved_object)
- AE_API int AE_insert_dataset_named_ref (tag_t dataset, int index, const char reference_name[AE_reference_size_c+1], AE_reference_type_t reference_type, tag_t previously_saved_object)
- AE_API int AE_insert_dataset_named_ref2 (tag_t dataset, int index, const char *reference_name, AE_reference_type_t reference_type, tag_t previously_saved_object)
#### Dataset Identification
- AE_API int AE_ask_dataset_id_rev (tag_t aDataset, char **aDatasetId, char **aDatasetRev)
- AE_API int AE_set_dataset_id_rev (tag_t aDataset, const char *aDatasetId, const char *aDatasetRev)
- AE_API int AE_find_dataset_by_id_rev (tag_t aDatasetType, const char *aDatasetId, const char *aDatasetRev, tag_t *aDataset)
- AE_API int AE_find_all_datasets_by_id (tag_t aDatasetType, const char *aDatasetId, int *nFound, tag_t **aDataset)
- AE_API int AE_create_dataset_with_id (tag_t aDatasetType, const char *aDatasetName, const char *aDatasetDescription, const char *aDatasetId, const char *aDatasetRev, tag_t *aNewDataset)
- AE_API int AE_initialize_dataset_with_id (tag_t aDataset, tag_t dsTypeTag, const char *dsName, const char *dsDesc, const char *dsId, const char *dsRev)
- AE_API int AE_copy_dataset_with_id (tag_t aDataset, const char *nameOfNewDataset, const char *dsId, const char *dsRev, tag_t *aNewDataset)

#### Typedefs
typedef enum AE_reference_type_e AE_reference_type_t
Enumerations
enum AE_reference_type_e { AE_BAD_REF_TYPE = 0, AE_ASSOCIATION, AE_PART_OF }

#### Functions:

- AE_API int AE_dataset_extent (int *n_instances, tag_t **instances)
- AE_API int AE_create_dataset (tag_t dataset_type, const char dataset_name[WSO_name_size_c+1], const char dataset_description[WSO_desc_size_c+1], tag_t *new_dataset)
- AE_API int AE_create_dataset_with_revanchor (tag_t aDatasetType, const char *aDatasetName, const char *aDatasetDescription, const char *aDatasetId, const char *aDatasetRev, tag_t rev_anchor_tag, tag_t *aNewDataset)
- AE_API int AE_find_dataset (const char dataset_name[WSO_name_size_c+1], tag_t *dataset)
- AE_API int AE_find_dataset2 (const char *dataset_name, tag_t *dataset)
- AE_API int AE_find_all_datasets (const char dataset_name[WSO_name_size_c+1], int *nFound, tag_t **dataset)
- AE_API int AE_find_all_datasets2 (const char *dataset_name, int *nFound, tag_t **dataset)
- AE_API int AE_ask_dataset_def_rev_limit (int *default_rev_limit)
- AE_API int AE_initialize_dataset (tag_t dataset, tag_t dataset_type, const char dataset_name[WSO_name_size_c+1], const char dataset_description[WSO_desc_size_c+1])
- AE_API int AE_copy_dataset (tag_t dataset, const char name_of_new_dataset[WSO_name_size_c+1], tag_t *new_dataset)
- AE_API int AE_ask_dataset_tool (tag_t dataset, tag_t *tool)
- AE_API int AE_ask_dataset_format (tag_t dataset, char format_name[AE_io_format_size_c+1])
- AE_API int AE_ask_dataset_format2 (tag_t dataset, char **format_name)
- AE_API int AE_ask_dataset_siteclass (tag_t dataset, char site_classification[AE_siteclass_size_c+1])
- AE_API int AE_ask_dataset_siteclass2 (tag_t dataset, char **site_classification)
- AE_API int AE_ask_dataset_datasettype (tag_t dataset, tag_t *datasettype)
- AE_API int AE_set_dataset_tool (tag_t dataset, tag_t tool)
- AE_API int AE_set_dataset_format (tag_t dataset, const char format_name[AE_io_format_size_c+1])
- AE_API int AE_set_dataset_format2 (tag_t dataset, const char *format_name)
- AE_API int AE_set_dataset_siteclass (tag_t dataset, const char site_classification[AE_siteclass_size_c+1])
- AE_API int AE_set_dataset_siteclass2 (tag_t dataset, const char *site_classification)
- AE_API int AE_set_dataset_datasettype (tag_t dataset, tag_t datasettype)
- AE_API int AE_save_myself (tag_t dataset)
- AE_API int AE_add_dataset_named_ref (tag_t dataset, const char reference_name[AE_reference_size_c+1], AE_reference_type_t reference_type, tag_t previously_saved_object)
- AE_API int AE_add_dataset_named_ref2 (tag_t dataset, const char *reference_name, AE_reference_type_t reference_type, tag_t previously_saved_object)
- AE_API int AE_find_dataset_named_ref (tag_t dataset, int instance, char reference_name[AE_reference_size_c+1], AE_reference_type_t *reference_type, tag_t *referenced_object)
- AE_API int AE_find_dataset_named_ref2 (tag_t dataset, int instance, char **reference_name, AE_reference_type_t *reference_type, tag_t *referenced_object)
- AE_API int AE_ask_dataset_ref_count (tag_t dataset, int *reference_count)
- AE_API int AE_ask_dataset_named_ref (tag_t dataset, const char reference_name[AE_reference_size_c+1], AE_reference_type_t *reference_type, tag_t *referenced_object)
- AE_API int AE_ask_dataset_named_ref2 (tag_t dataset, const char *reference_name, AE_reference_type_t *reference_type, tag_t *referenced_object)
- AE_API int AE_ask_all_dataset_named_refs (tag_t dataset, const char reference_name[AE_reference_size_c+1], int *nFound, tag_t **referenced_object)
- AE_API int AE_ask_all_dataset_named_refs2 (tag_t dataset, const char *reference_name, int *nFound, tag_t **referenced_object)
- AE_API int AE_remove_dataset_named_ref (tag_t dataset, const char reference_name[AE_reference_size_c+1])
- AE_API int AE_remove_dataset_named_ref2 (tag_t dataset, const char *reference_name)
- AE_API int AE_remove_dataset_named_ref_by_tag (tag_t dataset, const char reference_name[AE_reference_size_c+1], tag_t referenced_object)
- AE_API int AE_remove_dataset_named_ref_by_tag2 (tag_t dataset, const char *reference_name, tag_t referenced_object)
- AE_API int AE_is_dataset_unique (const char dataset_name[WSO_name_size_c+1], logical *result)
- AE_API int AE_is_dataset_unique2 (const char *dataset_name, logical *result)
- AE_API int AE_ask_dataset_num_revs (tag_t dataset, int *count)
- AE_API int AE_purge_dataset_revs (tag_t dataset)
- AE_API int AE_delete_all_dataset_revs (tag_t dataset)
- AE_API int AE_ask_dataset_anchor (tag_t dataset, tag_t *revision_anchor)
- AE_API int AE_ask_dataset_at (tag_t dataset, int index_name, tag_t *outDataset)
- AE_API int AE_ask_dataset_latest_rev (tag_t dataset, tag_t *latestDataset)
- AE_API int AE_ask_dataset_first_rev (tag_t dataset, tag_t *firstDataset)
- AE_API int AE_ask_dataset (tag_t dataset, tag_t *lastDataset)
- AE_API int AE_ask_dataset_next_rev (tag_t dataset, tag_t *nextDataset)
- AE_API int AE_ask_dataset_prev_rev (tag_t dataset, tag_t *prevDataset)
- AE_API int AE_ask_dataset_named_refs (tag_t dataset, int *nFound, tag_t **refObject)
- AE_API int AE_import_named_ref (tag_t dataset_tag, const char *reference_name, const char *os_full_path_name, const char *new_file_name, int file_type_flag)
- AE_API int AE_export_named_ref (tag_t datasetTag, const char *referenceName, const char *destPathName)
- AE_API int AE_set_bounding_boxes (tag_t dataset, tag_t file, int numBoundingBoxes, const double *boundingBoxes)
- AE_API int AE_set_absOcc_bounding_boxes (tag_t absOccData, tag_t dataset, tag_t file, int numBoundingBoxes, const double *boundingBoxes)
- AE_API int AE_get_bounding_boxes (tag_t dataset, int *numBoundingBoxes, double **boundingBoxes)
- AE_API int AE_delete_bounding_boxes (tag_t dataset)
