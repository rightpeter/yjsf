#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Rightpeter'
import rsa
import sys
import os
import os.path
import re

enc_pattern = re.compile(r'.*\.enc$')
dec_pattern = re.compile(r'.*\.dec$')
pickle_pattern = re.compile(r'.*\.pickle$')
zip_pattern = re.compile(r'.*\.zip$')


def enc(file_path):
    with open(file_path) as inputfile:
        content = inputfile.read()

    # print 'content: ', content
    # content = content[:245]
    with open('public.pem') as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)

    with open('private.pem') as privatefile:
        p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)

    crypto = ''
    # print '========start========='
    while content:
        message = content[:245]
        content = content[245:]

        enc_message = rsa.encrypt(message, pubkey)
        crypto += enc_message
        # print '-----------------message: -------------\n', message
        # print '-----------------content: -------------\n', content
        # print '-----------------enc_message: ---------\n', enc_message
        # print '-----------------crypto: --------------\n', crypto

    # crypto = rsa.encrypt(content, pubkey)
    # print 'crypto: ', crypto

    with open(file_path + '.enc', 'w+') as outputfile:
        outputfile.write(crypto)
        outputfile.close()


if __name__ == '__main__':
    # print 'argv[0]: ', sys.argv[0]
    # print 'argv[1]: ', sys.argv[1]
    rootdir = os.path.join(os.getcwd(), 'email_input.txt')

    enc(rootdir)
