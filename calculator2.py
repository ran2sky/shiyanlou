import sys


class Args:
    def __init__(self, args):
        self.args = args

    def _parse_arg(self, arg):

        try:
            value = self.args[self.args.index(arg) + 1]
        except (ValueError, IndexError):
            value = None
        return value

    def get_arg_value(self, arg):
        value = self._parse_arg(arg)
        if value is None:
            raise ArgError
        return value
class SheBaoConfig:
    def __init__(self, file):
        result = self.__parse_config(file)
        self.jishu_low = result[0]
        self.jishu_high = result[1]
        self.total_rate = result[2]

    def __parse_config(self, file):
       rate = 0

       with open(file) as f:
           for line in f:
               key, value = line.split('=')
               key = key.strip()
               value = value.strip()
               if key == 'JiShuL':
                   jishu_low = float(value.strip())
               elif key == 'JiShuH':
                   jishu_high = float(value.strip())
               else:
                   rate += float(value.strip())
       return jishu_low, jishu_high, rate
class EmployeeData:
    def __init__(self, file):
        self.data = self.__parse_file(file)

    def __parse_file(self, file):
        data = []
        for line in open(file):
            key, value = line.split(',')
            data.append((int(key), int(value)))
        return data
    def __iter__(self):
        return iter(self.data)

class Calculator:
    tax_start = 3500
    tax_table = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (35000, 0.3, 2755),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0),
    ]
    def __init__(self, config):
        self.config = config
    def calculate(self, data_item):
        employee_id, gongzi = data_item

        if gongzi < self.config.jishu_low:
            shebao = self.config.jishu_low * self.config.total_rate
        elif gongzi > self.config.jishu_high:
            shebao = self.config.jishu_high * self.config.total_rate
        else:
            shebao = gongzi * self.config.total_rate
        left_gongzi = gongzi - shebao
        tax_gongzi = left_gongzi - self.tax_start
        tax_left_gongzi = left_gongzi

        if tax_gongzi < 0:
            tax = 0

        else:
            for item in self.tax_table:

                if tax_gongzi > item[0]:
                    tax = tax_gongzi * item[1] - item[2]
                    tax_left_gongzi = left_gongzi - tax
                    break
        return str(employee_id), str(gongzi), '{:.2f}'.format(shebao), '{:.2f}'.format(tax), '{:.2f}'.format(tax_left_gongzi)
class Exporter:
    def __init__(self, file):
        self.file = file
    def export(self, data):
        with open(self.file, 'w') as f:
            for item in data:
                line = (','.join(item)) + '\n'
                f.write(line)
class Executor:
    def __init__(self):

        args = Args(sys.argv[1:])
        config = SheBaoConfig(args.get_arg_value('-c'))
        self.employee_data = EmployeeData(args.get_arg_value('-d'))
        self.exporter = Exporter(args.get_arg_value('-o'))
        self.calculator = Calculator(config)

    def execute(self):
        results = []
        for item in self.employee_data:
            result = self.calculator.calculate(item)
            results.append(result)
        self.exporter.export(results)

if __name__ == '__main__':
    executor = Executor()
    executor.execute()

