#! /usr/bin/env python

'''
Created on May, 14 2015

@author: Patrick Gray
'''

import argparse

class PermutationBuilder(object):
    def __init__(self):
        pass

    def build_permutations(self, s):
        #find all permutations of string s
        if len(s)==1:
            return [s]

        past_perms=self.build_permutations(s[1:])
        first_char=s[0]
        current_perms=[]
        for p in past_perms:
            for i in range(len(p)+1):
                current_perms.append(p[:i] + first_char + p[i:])
        return current_perms

def parse_args():
    parser = argparse.ArgumentParser(description='Prints all the permutations from a given string.')
    parser.add_argument('--string', nargs='?', type=str, help="String to use for finding all permutations.")
    args = vars(parser.parse_args())

    if args["string"] == None:
       parser.error('You must include a string. Use -h for more info.')

    return (args["string"])

def main(argv=None):
    s = parse_args()
    
    permutation_builder = PermutationBuilder()

    print(permutation_builder.build_permutations(s))

if __name__ == "__main__":
    main()
