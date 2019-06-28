from datetime import datetime

from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 2


def end_keyword(name, attrs):
    if attrs['status'] == 'FAIL' and (attrs['libname'].endswith(('Verify'))):
        filename = "{}_{}.png".format(datetime.now().strftime("%Y%m%d_%H%M%S"), attrs['libname'])
        BuiltIn().get_library_instance('SeleniumLibrary').capture_page_screenshot(filename)
