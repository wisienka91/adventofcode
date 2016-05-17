# -*- coding: utf-8 -*-


class Wire(object):
    
    def __init__(self, operands, operator, target):
        self.operands = operands
        self.operator = operator
        self.target = target
        self.bit_limit = 65535

    def handle_subwires(self):
        if isinstance(self.operands[0], Wire):
            self.operands[0] = self.operands[0].get_signal()
        if len(self.operands) > 1 and isinstance(self.operands[1], Wire):
            self.operands[1] = self.operands[1].get_signal()

    def get_signal(self):
        self.handle_subwires()
        if self.operator == 'NOT':
            return self.bit_limit - self.operands[0]

        elif self.operator == 'AND':
            return self.operands[0] & self.operands[1]

        elif self.operator == 'OR':
            return self.operands[0] | self.operands[1]

        elif self.operator == 'LSHIFT':
            return self.operands[0] << self.operands[1]

        elif self.operator == 'RSHIFT':
            return self.operands[0] >> self.operands[1]

        else:
            return self.operands[0]

    def update_operands(self, operands):
        self.operands = operands


class Wires(object):

    def __init__(self):
       self.wires = {}
       self.operators = ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']

    def get_wires(self, input_file):
        for line in input_file.readlines():
            data = line.strip('\n').split()
            operator = self.get_operator(data)
            operands = self.get_operands(data, operator)
            target_wire = data[-1]
            self.wires.update({
                target_wire: Wire(operands, operator, target_wire)
            })

    def get_operator(self, rule):
        operator = None
        for part in rule:
            if part in self.operators:
                operator = part
        return operator

    def sanitize_operand(self, operand):
        sanitized = None
        try:
            sanitized = int(operand)
        except ValueError:
            sanitized = operand
        return sanitized

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

    def connect_wire(self, wire):
        for operand in wire.operands:
            if isinstance(operand, str):
                wire.operands[
                    wire.operands.index(operand)] = self.wires.get(operand)

    def connect_wires(self):
        for wire in self.wires.values():
            self.connect_wire(wire)

    def get_signal_value(
        self, wire, updated=False, wire_to_update=None, new_operands=None):
        input_file = open('day07.txt', 'r')
        self.get_wires(input_file)
        if updated:
            self.wires.get(wire_to_update).update_operands(new_operands)
        self.connect_wires()
        output_wire = self.wires.get(wire)
        result = output_wire.get_signal()
        print '%s-wire signal is: %s' % (wire, result)
        return result


if __name__ == '__main__':
    a_wire_value = Wires().get_signal_value('a')
    Wires().get_signal_value(
        'a', updated=True, wire_to_update='b', new_operands=[a_wire_value])

