from robot.libraries.BuiltIn import BuiltIn


def set_multiple_test_variables(**variables):
    """
    Set multiple test variables

    :param **variables: kwargs containing key/values pairs
    """
    for key, value in variables.items():
        BuiltIn().set_test_variable(f'${{{key}}}', value)
