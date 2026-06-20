---
name: teamcenter-itk-coding-assistant
description: Teamcenter ITK (Integration Toolkit) is Siemens C/C++ based API used to customize and extend the Teamcenter PLM server.
---
# Teamcnter ITK Coding Instructions

## Teamcenter ITK Coding Standards

- All server side customizations should use Siemens C/C++ based API, never invent or hallucinate function names/API's.
- Always include standard ITK memory management. Ensure any memory allocated by ITK functions (e.g., using 'MEM_alloc') is freed using 'MEM_free' when no longer needed.
- Always check the return status of ITK function calls against 'ITK_ok'. 

## Standard ITK Function Syntax

- Teamcenter ITK functions strictly follow a structured, predictable naming standard:
- int MODULE_verb_class_modifier(...);

- Return Code: Almost all functions return an int status code (ifail). A value of 0 indicates success (ITK_ok).
- MODULE: The functional block (e.g., AOM, BOM, ITEM).
- Verb: The action being taken (e.g., ask, create, set, find).


## Core ITK Modules and Common Functions:

1. Session and Authentication (ITK)

Used to manage the life cycle of a server connection and authenticate system administration workflows.
-	ITK_init_module(char* user, char* pass, char* group): Logs into the Teamcenter environment with explicit credentials.
-	ITK_auto_login(): Automatically connects using operating system credentials.

2. Application Object Module (AOM)

Handles structural data, locks, and generic property interactions on runtime business objects.
-	AOM_ask_value_string(tag_t object, const char* prop_name, char** value): Retrieves a string property value.
-	AOM_set_value_string(tag_t object, const char* prop_name, const char* value): Assigns a string property value.
-	AOM_lock(tag_t object): Locks an object for editing.
-	AOM_save(tag_t object): Commits changes to the Teamcenter database.

3. Items and Revisions (ITEM)

Manages the creation, status, and life-cycle metadata of parts and items.
-	ITEM_find_item(const char* item_id, tag_t* item): Locates an Item by its unique ID.
-	ITEM_find_rev(const char* item_id, const char* rev_id, tag_t* item_rev): Retrieves a specific Revision of an Item.

4. Bill of Materials (BOM)

Facilitates product configuration, window loading, and tree traversals.
-	BOM_create_window(tag_t* window): Opens a fresh assembly viewing context window.
-	BOM_set_window_top_line(tag_t window, tag_t item, tag_t rev, tag_t rule, tag_t* top_line): Binds an item structure to the top of the window.
-	BOM_line_ask_child_lines(tag_t bom_line, int* count, tag_t** children): Returns child components of an assembly node.

5. Error Message Handling (EMH)

Provides diagnostic mapping for failed function returns.
-	EMH_ask_error_text(int error_code, char** error_text): Decodes an ifail integer into human-readable logs.

