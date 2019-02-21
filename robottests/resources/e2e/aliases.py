NOT_ON_PAGE = {
    'the site': '/ui',
    'dashboard page': '/configuration',
    'configuration page': '/',
    'Swagger page': '/',
}

ON_PAGE = {'dashboard page': '/', 'configuration page': '/configuration'}

NAV_LINK = {
    'dashboard': 'css=.ta_dashboard_nav_item',
    'configuration': 'css=.ta_configuration_nav_item',
    'Swagger': 'css=.ta_swagger_nav_item',
}

PAGE_ELEMENT = {
    'dashboard': 'css=.ta_dashboard_header',
    'configuration': 'css=.ta_configuration_header',
    'Swagger': 'css=#swagger-ui',
}

ADD_NEW_DATASET = {
    'header': 'css=#add-new-dataset-header',
    'name': 'css=.ta-new-dataset-name',
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
}
