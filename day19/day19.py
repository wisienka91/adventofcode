# -*- coding: utf-8 -*-
import re
from random import shuffle


class MedicineFactory(object):

    def get_data(self, line):
        rule = None
        data = line.split('=>')
        if len(data) == 2:
            rule = {data[0].strip(): data[1].strip()}
        elif len(data) == 1:
            rule = data[0].strip()
        return rule

    def get_rules_and_molecule(self):
        input_file = open('day19.txt', 'r')
        self.rules = []
        for line in input_file.readlines():
            data = self.get_data(line.strip())
            if data:
                self.rules.append(data)
        self.starting_molecule = self.rules.pop(-1)

    def update_molecules(self, rule, molecules):
        (key, value) = rule.items()[0]
        occurences = [
            m.start() for m in re.finditer(key, self.starting_molecule)]
        for index in occurences:
            molecule = self.starting_molecule[
                :index] + value + self.starting_molecule[index + len(key):]
            molecules.add(molecule)
        return molecules

    def count_distinct_molecules(self):
        self.get_rules_and_molecule()
        molecules = set()
        for rule in self.rules:
            molecules = self.update_molecules(rule, molecules)
        molecules_count = len(list(molecules))
        print 'Possible molecules to create: %s' % molecules_count

    def do_the_reverse_engineering(self, rule, molecule):
        self.count += molecule.count(rule.values()[0])
        molecule = molecule.replace(rule.values()[0], rule.keys()[0])
        return molecule

    def count_shortest_formula(self, molecule):
        mol = molecule
        for rule in self.rules:
            while rule.values()[0] in molecule:
                molecule = self.do_the_reverse_engineering(rule, molecule)
        if mol == molecule:
            #surprisingly deterministic and fast way to get the correct answer
            #TO-DO: prove the method is deterministic or change the method
            molecule = self.starting_molecule
            self.count = 0
            shuffle(self.rules)
        return molecule

    def get_shortest_formula_count(self):
        self.count = 0
        molecule = self.starting_molecule
        while molecule != 'e':
            molecule = self.count_shortest_formula(molecule)
        print 'Shortest formula takes %s moves to create medicine' % self.count


if __name__ == '__main__':
    mf = MedicineFactory()
    mf.count_distinct_molecules()
    mf.get_shortest_formula_count()

