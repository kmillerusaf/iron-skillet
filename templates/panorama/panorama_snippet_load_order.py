# This dictionary option loads to shared top of the hierarchy, not each device group
# Useful for enterprise deployments sharing the same configuration elements
# Remove doc comment quotes from here to dictionary above to switch load options
from collections import OrderedDict

panorama_gold_template_dict = OrderedDict([
      ('panorama_system', ['panorama_system']),
      ('panorama_setting', ['panorama_setting']),
      ('panorama_log_settings', ['panorama_log_settings']),
      ('template', ['template']),
      ('device_group', ['device_group']),
      ('shared_tag', ['tag']),
      ('log_settings', ['shared_log_settings']),
      ('device_system', ['device_system']),
      ('device_setting', ['device_setting']),
      ('shared_address', ['address']),
      ('shared_external_list', ['external_list']),
      ('shared_profiles_custom_url_category', ['profiles_custom_url_category']),
      ('shared_profiles_decryption', ['profiles_decryption']),
      ('shared_profiles_file_blocking', ['profiles_file_blocking']),
      ('shared_profiles_spyware', ['profiles_spyware']),
      ('shared_profiles_url_filtering', ['profiles_url_filtering']),
      ('shared_profiles_virus', ['profiles_virus']),
      ('shared_profiles_vulnerability', ['profiles_vulnerability']),
      ('shared_profiles_wildfire_analysis', ['profiles_wildfire_analysis']),
      ('shared_profile_group', ['profile_group']),
      ('shared_log_settings_profiles', ['log_settings_profiles']),
      ('shared_post_rulebase_default_security_rules', ['post_rulebase_default_security_rules']),
      ('shared_pre_rulebase_security', ['pre_rulebase_security']),
      ('shared_pre_rulebase_decryption', ['pre_rulebase_decryption']),
      ('shared_post_rulebase_decryption', ['post_rulebase_decryption']),
      ('zone_protection_profile', ['zone_protection_profile']),
      ('log_collector_group', ['log_collector_group']),
      ('reports', ['reports_simple']),
      ('report_group', ['report_group_simple']),
      ('email_scheduler', ['email_scheduler_simple']),
                          ])