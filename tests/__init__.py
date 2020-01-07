import allure


@allure.epic('Ubuntu testing')
class TestBase:
    @staticmethod
    @allure.step('Compare actual and expected values')
    def compare_values(field, actual_value, expected_value):
        assert str(actual_value) == expected_value, f"{field} is - '{actual_value}' instead of - '{expected_value}'"


