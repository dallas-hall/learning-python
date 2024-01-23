import pytest

# To import this in PyCharm, right click the folder and mark as Sources Root
from employee import Employee


# Use a pytest decorator to create a test fixture that can be used by all testing functions.
@pytest.fixture
def employees():
	"""An employee testing fixture."""
	new_hires = {
		'John Doe': {
			'department': 'HR'
		},
		'Jane Doe': {
			'department': 'IT',
			'salary': 75_000
		},

	}
	employees = []
	for key, value in new_hires.items():
		if value.get('salary'):
			employee = Employee(key, value['department'], value['salary'])
		else:
			employee = Employee(key, value['department'])
		employees.append(employee)
	return employees


# When a parameter matches the name of a @pytest.fixture decorator, the decorator will automatically run.
def test_employees_added(employees):
	"""Test adding an employee."""
	new_employee = Employee("Roger", "Rabbit", 100_000)
	employees.append(new_employee)
	assert new_employee in employees


def test_give_default_raise(employees):
	"""Test the default raise of $5,000."""
	for employee in employees:
		if employee.name == 'John Doe':
			assert employee.salary == 50_000
			employee.increase_salary()
			assert employee.salary == 55_000


def test_give_specific_raise(employees):
	"""Test specific raise of $10,000."""
	for employee in employees:
		if employee.name == 'Jane Doe':
			assert employee.salary == 75_000
			employee.increase_salary(10_000)
			assert employee.salary == 85_000
