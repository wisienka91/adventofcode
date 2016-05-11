# -*- coding: utf-8 -*-

class LookAndSay(object):

    def analyze(self, output):
        result = []
        previous = ''
        counter = 0
        for ch in output:
            if ch == previous:
                counter += 1
            elif previous != '':
                counter += 1
                result.append((previous, counter))
                counter = 0
            previous = ch
        if output[-1] == result[-1][0]:
            last = result.pop([-1])
            result.append((last[0], last[1] + 1))
        else:
            result.append((output[-1], 1))

        return result

    def count_next_output(self, output):
        analyzed = self.analyze(output)
        new_output = ''
        for item in analyzed:
            new_output += str(item[1]) + item[0]
        return new_output

    def count_for_input_and_iterations(self, initial, iterations):
        output = initial
        for i in range(iterations):
            output = self.count_next_output(output)
        result = len(output)
        return result

    def run(self):
        input_file = open('day10.txt', 'r')
        for line in input_file.readlines():
            initial = line.strip('\n').split()[0]
            iterations = int(line.strip('\n').split()[1])
            result = self.count_for_input_and_iterations(initial, iterations)
            print 'Number length after %s iterations is %s.' % (
                iterations, result
            )

if __name__ == '__main__':
    LookAndSay().run()

