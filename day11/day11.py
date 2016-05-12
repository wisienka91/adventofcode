# -*- coding: utf-8 -*-
import string

class PasswordIterator(object):

    def __init__(self):
        self.allowed_letters = string.lowercase

    def has_row_of_three(self, password):
        letters = self.allowed_letters
        for i in range(len(letters) - 2):
            condition = '%s%s%s' % (letters[i], letters[i+1], letters[i+2])
            if condition in password:
                return True
        return False

    def has_two_pairs(self, password):
        pair = ''
        pairs = 0
        for i in range(len(password) - 1):
            if password[i] == password[i+1] != pair:
                pair = password[i]
                pairs += 1
        if pairs == 2:
            return True
        return False

    def has_no_forbidden_letters(self, password):
        for ch in password:
            if ch =='i' or ch == 'l' or ch == 'o':
                return False
        return True


    def is_not_valid(self, next_pass):
        return not (
            self.has_row_of_three(next_pass) and 
            self.has_two_pairs(next_pass) and 
            self.has_no_forbidden_letters(next_pass)
        )

    def carry_letter(self, password):
        letters = self.allowed_letters
        next_pass = ''
        first_allowed = letters[0]
        last_allowed = letters[-1]
        next_pass = password
        carry_one_more = False
        for i in range(1, len(password), 1):
            if password[len(password) - i] == last_allowed:
                next_pass = (
                    password[:len(password) - i] +
                    first_allowed +
                    next_pass[len(password) - i + 1:]
                )
                carry_one_more = True
            elif carry_one_more:
                next_pass = (
                    next_pass[:len(password) - i] +
                    letters[letters.index(password[len(password) - i]) + 1] +
                    next_pass[len(password) - i + 1:]
                )
                carry_one_more = False
        return next_pass

    def get_next_iteration(self, password):
        letters = self.allowed_letters
        next_pass = ''
        last_allowed = letters[-1]
        last = password[-1]
        if last == last_allowed:
            next_pass = self.carry_letter(password)
        else:
            next_pass = password[:-1]
            next_pass += letters[letters.index(last) + 1]
        return next_pass

    def generate_next_password(self, start_pass):
        next_pass = self.get_next_iteration(start_pass)
        while self.is_not_valid(next_pass):
            next_pass = self.get_next_iteration(next_pass)
        print 'Next password would be %s.' % next_pass
        return next_pass

if __name__ == '__main__':
    input_file = open('day11.txt', 'r')
    start_password = input_file.readline().strip()
    pi = PasswordIterator()
    new_password = pi.generate_next_password(start_password)
    pi.generate_next_password(new_password)

