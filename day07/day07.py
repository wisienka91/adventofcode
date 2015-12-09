# -*- coding: utf-8 -*-

class Wires(object):

    def __init__(self):
       self.wires = {}
       self.rules = []
       self.operators = ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']

    def sanitize_line(self, line):
        return line.strip('\n')

    def get_rules(self, input_file):
        for line in input_file.readlines():
            new_line = self.sanitize_line(line).split()
            operator = self.get_operator(new_line)
            operands = self.get_operands(new_line, operator)
            target_wire = new_line[-1]
            self.rules.append({
                'operator': operator,
                'operands': operands,
                'target_wire': target_wire
            })


    def get_operator(self, rule):
        operator = None
        for part in rule:
            if part in self.operators:
                operator = part
        return operator

    def sanitize_operand(self, operand):
        try:
            return int(operand)
        except ValueError:
            return operand

    def get_operands(self, rule, operator):
        operands = []
        if operator == 'NOT':
            operands.append(self.sanitize_operand(rule[1]))
        elif operator in self.operators:
            operands.append(self.sanitize_operand(rule[0]))
            operands.append(self.sanitize_operand(rule[2]))
        else:
            operands.append(self.sanitize_operand(rule[0]))
        return operands

    def set_wires(self):
        new_list = []
        for rule in self.rules:
            if not rule['operator']:
                self.wires[rule['target_wire']] = rule['operands'][0]
            else:
                new_list.append(rule)
        self.rules = new_list

    def apply_rules(self, input_file):
        self.get_rules(input_file)
        self.set_wires()


    def get_signal_value(self):
        input_file = open('day07.txt', 'r')
        self.apply_rules(input_file)
        print self.wires
        print 'Signal strength is: %s' % self.wires.get('a')

if __name__ == '__main__':
    Wires().get_signal_value()

