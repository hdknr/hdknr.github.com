(tact)hdknr@wzy:~/ve/tact/src/logging$ sentry --config=sentry.conf.py start
Performing upgrade before service startup...
Syncing...
Creating tables ...
Creating table auth_permission
Creating table auth_group_permissions
Creating table auth_group
Creating table auth_user_groups
Creating table auth_user_user_permissions
Creating table auth_user
Creating table django_admin_log
Creating table django_content_type
Creating table django_session
Creating table django_site
Creating table south_migrationhistory

You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'hdknr'): admin
Email address: admin@admin.admin
Password:
Password (again):
Superuser created successfully.
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)
Migrating...
Running migrations for djcelery:
 - Migrating forwards to 0004_v30_changes.
 > djcelery:0001_initial
 > djcelery:0002_v25_changes
 > djcelery:0003_v26_changes
 > djcelery:0004_v30_changes
 - Loading initial data for djcelery.
Installed 0 object(s) from 0 fixture(s)
Running migrations for django:
 - Migrating forwards to 0001_initial.
 > django:0001_initial
 - Loading initial data for django.
Installed 0 object(s) from 0 fixture(s)
Running migrations for sentry:
 - Migrating forwards to 0105_auto__chg_field_projectcountbyminute_time_spent_total__chg_field_group.
 > sentry:0001_initial
 > sentry:0002_auto__del_field_groupedmessage_url__chg_field_groupedmessage_view__chg
 > sentry:0003_auto__add_field_message_group__del_field_groupedmessage_server_name
 > sentry:0004_auto__add_filtervalue__add_unique_filtervalue_key_value
 > sentry:0005_auto
 > sentry:0006_auto
 > sentry:0007_auto__add_field_message_site
 > sentry:0008_auto__chg_field_message_view__add_field_groupedmessage_data__chg_field
 > sentry:0009_auto__add_field_message_message_id
 > sentry:0010_auto__add_messageindex__add_unique_messageindex_column_value_object_id
 > sentry:0011_auto__add_field_groupedmessage_score
 > sentry:0012_auto
 > sentry:0013_auto__add_messagecountbyminute__add_unique_messagecountbyminute_group_
 > sentry:0014_auto
 > sentry:0014_auto__add_project__add_projectmember__add_unique_projectmember_project
 > sentry:0015_auto__add_field_message_project__add_field_messagecountbyminute_projec
 > sentry:0016_auto__add_field_projectmember_is_superuser
 > sentry:0017_auto__add_field_projectmember_api_key
 > sentry:0018_auto__chg_field_project_owner
 > sentry:0019_auto__del_field_projectmember_api_key__add_field_projectmember_public_
 > sentry:0020_auto__add_projectdomain__add_unique_projectdomain_project_domain
 > sentry:0021_auto__del_message__del_groupedmessage__del_unique_groupedmessage_proje
 > sentry:0022_auto__del_field_group_class_name__del_field_group_traceback__del_field
 > sentry:0023_auto__add_field_event_time_spent
 > sentry:0024_auto__add_field_group_time_spent_total__add_field_group_time_spent_cou
 > sentry:0025_auto__add_field_messagecountbyminute_time_spent_total__add_field_messa
 > sentry:0026_auto__add_field_project_status
 > sentry:0027_auto__chg_field_event_server_name
 > sentry:0028_auto__add_projectoptions__add_unique_projectoptions_project_key_value
 > sentry:0029_auto__del_field_projectmember_is_superuser__del_field_projectmember_pe
 > sentry:0030_auto__add_view__chg_field_event_group
 > sentry:0031_auto__add_field_view_verbose_name__add_field_view_verbose_name_plural_
 > sentry:0032_auto__add_eventmeta
 > sentry:0033_auto__add_option__add_unique_option_key_value
 > sentry:0034_auto__add_groupbookmark__add_unique_groupbookmark_project_user_group
 > sentry:0034_auto__add_unique_option_key__del_unique_option_value_key__del_unique_g
 > sentry:0036_auto__chg_field_option_value__chg_field_projectoption_value
 > sentry:0037_auto__add_unique_option_key__del_unique_option_value_key__del_unique_g
 > sentry:0038_auto__add_searchtoken__add_unique_searchtoken_document_field_token__ad
 > sentry:0039_auto__add_field_searchdocument_status
 > sentry:0040_auto__del_unique_event_event_id__add_unique_event_project_event_id
 > sentry:0041_auto__add_field_messagefiltervalue_last_seen__add_field_messagefilterv
 > sentry:0042_auto__add_projectcountbyminute__add_unique_projectcountbyminute_projec
 > sentry:0043_auto__chg_field_option_value__chg_field_projectoption_value
 > sentry:0044_auto__add_field_projectmember_is_active
 > sentry:0045_auto__add_pendingprojectmember__add_unique_pendingprojectmember_projec
 > sentry:0046_auto__add_teammember__add_unique_teammember_team_user__add_team__add_p
 > sentry:0047_migrate_project_slugs
 - Migration 'sentry:0047_migrate_project_slugs' is marked for no-dry-run.
 > sentry:0048_migrate_project_keys
 - Migration 'sentry:0048_migrate_project_keys' is marked for no-dry-run.
 > sentry:0049_create_default_project_keys
 - Migration 'sentry:0049_create_default_project_keys' is marked for no-dry-run.
 > sentry:0050_remove_project_keys_from_members
 > sentry:0051_auto__del_pendingprojectmember__del_unique_pendingprojectmember_projec
 > sentry:0052_migrate_project_members
 - Migration 'sentry:0052_migrate_project_members' is marked for no-dry-run.
 > sentry:0053_auto__del_projectmember__del_unique_projectmember_project_user
 > sentry:0054_fix_project_keys
 - Migration 'sentry:0054_fix_project_keys' is marked for no-dry-run.
 > sentry:0055_auto__del_projectdomain__del_unique_projectdomain_project_domain
 > sentry:0056_auto__add_field_group_resolved_at
 > sentry:0057_auto__add_field_group_active_at
 > sentry:0058_auto__add_useroption__add_unique_useroption_user_project_key
 > sentry:0059_auto__add_filterkey__add_unique_filterkey_project_key
 > sentry:0060_fill_filter_key
 - Migration 'sentry:0060_fill_filter_key' is marked for no-dry-run.
 > sentry:0061_auto__add_field_group_group_id__add_field_group_is_public
 > sentry:0062_correct_del_index_sentry_groupedmessage_logger__view__checksum
 > sentry:0063_auto
 > sentry:0064_index_checksum
 > sentry:0065_create_default_project_key
 - Migration 'sentry:0065_create_default_project_key' is marked for no-dry-run.
 > sentry:0066_auto__del_view
 > sentry:0067_auto__add_field_group_platform__add_field_event_platform
 > sentry:0068_auto__add_field_projectkey_user_added__add_field_projectkey_date_added
 > sentry:0069_auto__add_lostpasswordhash
 > sentry:0070_projectoption_key_length
 > sentry:0071_auto__add_field_group_users_seen
 > sentry:0072_auto__add_affecteduserbygroup__add_unique_affecteduserbygroup_project_
 > sentry:0073_auto__add_field_project_platform
 > sentry:0074_correct_filtervalue_index
 > sentry:0075_add_groupbookmark_index
 > sentry:0076_add_groupmeta_index
 > sentry:0077_auto__add_trackeduser__add_unique_trackeduser_project_ident
 > sentry:0078_auto__add_field_affecteduserbygroup_tuser
 > sentry:0079_auto__del_unique_affecteduserbygroup_project_ident_group__add_unique_a
 > sentry:0080_auto__chg_field_affecteduserbygroup_ident
 > sentry:0081_fill_trackeduser
 - Migration 'sentry:0081_fill_trackeduser' is marked for no-dry-run.
 > sentry:0082_auto__add_activity__add_field_group_num_comments__add_field_event_num_
 > sentry:0083_migrate_dupe_groups
 - Migration 'sentry:0083_migrate_dupe_groups' is marked for no-dry-run.
 > sentry:0084_auto__del_unique_group_project_checksum_logger_culprit__add_unique_gro
 > sentry:0085_auto__del_unique_project_slug__add_unique_project_slug_team
 > sentry:0086_auto__add_field_team_date_added
 > sentry:0087_auto__del_messagefiltervalue__del_unique_messagefiltervalue_project_ke
 > sentry:0088_auto__del_messagecountbyminute__del_unique_messagecountbyminute_projec
 > sentry:0089_auto__add_accessgroup__add_unique_accessgroup_team_name
 > sentry:0090_auto__add_grouptagkey__add_unique_grouptagkey_project_group_key__add_f
 > sentry:0091_auto__add_alert
 > sentry:0092_auto__add_alertrelatedgroup__add_unique_alertrelatedgroup_group_alert
 > sentry:0093_auto__add_field_alert_status
 > sentry:0094_auto__add_eventmapping__add_unique_eventmapping_project_event_id
 > sentry:0095_rebase
 > sentry:0096_auto__add_field_tagvalue_data
 > sentry:0097_auto__del_affecteduserbygroup__del_unique_affecteduserbygroup_project_
 > sentry:0098_auto__add_user__chg_field_team_owner__chg_field_activity_user__chg_fie
 > sentry:0099_auto__del_field_teammember_is_active
 > sentry:0100_auto__add_field_tagkey_label
 > sentry:0101_ensure_teams
 - Migration 'sentry:0101_ensure_teams' is marked for no-dry-run.
 > sentry:0102_ensure_slugs
 - Migration 'sentry:0102_ensure_slugs' is marked for no-dry-run.
 > sentry:0103_ensure_non_empty_slugs
 - Migration 'sentry:0103_ensure_non_empty_slugs' is marked for no-dry-run.
 > sentry:0104_auto__add_groupseen__add_unique_groupseen_group_user
 > sentry:0105_auto__chg_field_projectcountbyminute_time_spent_total__chg_field_group
Created internal Sentry project (slug=sentry, id=1)
 - Loading initial data for sentry.
Installed 0 object(s) from 0 fixture(s)
Running migrations for social_auth:
 - Migrating forwards to 0002_auto__add_unique_nonce_timestamp_salt_server_url__add_unique_associati.
 > social_auth:0001_initial
 > social_auth:0002_auto__add_unique_nonce_timestamp_salt_server_url__add_unique_associati
 - Loading initial data for social_auth.
Installed 0 object(s) from 0 fixture(s)

Synced:
 > django.contrib.auth
 > django.contrib.admin
 > django.contrib.contenttypes
 > django.contrib.messages
 > django.contrib.sessions
 > django.contrib.sites
 > django.contrib.staticfiles
 > crispy_forms
 > raven.contrib.django.raven_compat
 > sentry.plugins.sentry_interface_types
 > sentry.plugins.sentry_mail
 > sentry.plugins.sentry_urls
 > sentry.plugins.sentry_useragents
 > south

Migrated:
 - djcelery
 - kombu.transport.django
 - sentry
 - social_auth
Running service: 'http'
2013-10-14 14:44:33 [18706] [INFO] Starting gunicorn 0.17.4
2013-10-14 14:44:33 [18706] [INFO] Listening at: http://0.0.0.0:9000 (18706)
2013-10-14 14:44:33 [18706] [INFO] Using worker: sync
2013-10-14 14:44:33 [18721] [INFO] Booting worker with pid: 18721
2013-10-14 14:44:33 [18722] [INFO] Booting worker with pid: 18722
2013-10-14 14:44:33 [18723] [INFO] Booting worker with pid: 18723

