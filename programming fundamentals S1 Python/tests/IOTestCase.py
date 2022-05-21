import contextlib
import importlib
from io import StringIO
from unittest import TestCase, mock


class IOTestCase(TestCase):
    modules = {}

    def package_name(self):
        return ""

    def import_module(self, module_name):
        package_name = self.package_name()

        if package_name:
            module_name = package_name + "." + module_name

        if module_name in self.modules:
            old = self.modules[module_name]
            self.modules[module_name] = importlib.reload(old)
        else:
            self.modules[module_name] = importlib.import_module(module_name)

    def get_output(self, module_name, input_arr):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            with mock.patch('builtins.input', side_effect=input_arr):
                self.import_module(module_name)
        return temp_stdout.getvalue()

    def assertOutputEqual(self, module_name, input_arr, expected_output):
        output = self.get_output(module_name, input_arr)
        self.assertEqual(expected_output, output)

    def create_io_tester(self, fn):
        def tester(inputs, expected_result):
            return self.assertOutputEqual(fn, inputs, expected_result)
        return tester
