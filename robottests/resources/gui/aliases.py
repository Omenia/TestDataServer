NOT_ON_PAGE = {
    'the site': '/ui',
    'dashboard page': '/configuration',
    'configuration page': '/',
    'settings page': '/',
    'Swagger page': '/',
}

ON_PAGE = {
    'dashboard page': '/',
    'configuration page': '/configuration',
    'settings page': '/settings',
}

NAV_LINK = {
    'dashboard': 'css=.ta-dashboard-nav-item',
    'configuration': 'css=.ta-configuration-nav-item',
    'settings': 'css=.ta-settings-nav-item',
    'Swagger': 'css=.ta-swagger-nav-item',
}

PAGE_ELEMENT = {
    'dashboard': 'css=.ta-dashboard-header',
    'configuration': 'css=.ta-configuration-header',
    'settings': 'css=.ta-settings-header',
    'Swagger': 'css=#swagger-ui',
}

ADD_NEW_DATASET = {
    'header': 'css=#conf-new-dataset-header',
    'name': 'css=#conf-new-dataset',
    'datatype': 'name=new-dataset-datatype',
    'items': 'css=.ta-new-dataset-items',
    'submit': 'css=.ta-new-dataset-submit',
}

ALERT_TEXT = {
    'delete-dataset': 'Are you sure you want to delete dataset:',
    'delete-item': 'Are you sure you want to delete dataset item:',
}

INFO_ELEMENT = {'ok': 'css=.ok-info', 'error': 'css=.error-info', 'hidden': 'css=.hidden-info'}

INFO_TEXT = {
    'dataset-added-ok': 'Dataset added',
    'dataset-added-error': 'Conflict (dataset exists already)',
    'dataset-deleted-ok': 'Dataset deleted',
    'dataset-deleted-error': 'Not Found (dataset does not exist)',
    'item-deleted-ok': 'Dataset item deleted',
    'item-deleted-error': 'Not Found (dataset item does not exist)',
    'settings-saved-ok': 'Settings saved',
    'settings-saved-error': 'Bad Request (Incorrect timeout syntax)',
}

ADD_NEW_ITEM = {
    'add-icon': 'css=.add-item-{dataset}',
    'input': 'css=#new-dataset-item',
    'submit': 'css=#submit-new-item',
}

EXISTING_DATASETS = {
    'dataset-text': 'xpath=//*[contains(text(), "{dataset}")]',
    'dataset-row': 'css=.ta-name-{dataset}',
    'play-icon': 'css=.ta-play-{dataset}-{index}',
    'stop-icon': 'css=.ta-stop-{dataset}-{index}',
    'item-status': 'css=.ta-status-{dataset}-{index}',
    'delete-dataset': 'css=.ta-delete-{dataset}',
    'delete-item': 'css=.ta-delete-{dataset}-{index}',
}

dataset_path = 'xpath=//div[@class="db-dataset"][contains(text(), "{dataset_name}")]'

DASHBOARD_PAGE = {
    'dataset': dataset_path,
    'item-name': f'{dataset_path} \
        /following-sibling::div[{{index}}]/span[contains(@class, "db-item-name")]',
    'item-time': f'{dataset_path} \
        /following-sibling::div[{{index}}]/span[contains(@class, "db-item-time")]',
    'item-status': f'{dataset_path} \
        /following-sibling::div[{{index}}]/span[contains(@class, "db-item-status")]',
}

SETTINGS_PAGE = {
    'use-status': 'css=#use_status',
    'use-quarantine': 'css=#use_quarantine',
    'timeout': 'css=#timeout',
    'save-settings': 'css=#save-settings',
}
