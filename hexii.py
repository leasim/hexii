import sys
import binascii

def print_h(value):
#Given a single byte (character), print its hex representation followed
#by a space and no new line.
    sys.stdout.write('{0} '.format(binascii.hexlify(value).upper()))

def print_l(byte):
#Given a byte string, print hex representation in groups of 16 bytes
#and show "printable" characters after hex representation.
    min_byte = '\x20'
    max_byte = '\x7f'
    count = 0
    byte_l = []
    for i in byte:
        print_h(i)
        if not (min_byte < i < max_byte):
            byte_l.append('.')
        else:
            byte_l.append(i)
        count += 1
        if count % 16 == 0:
            count = 0
            print " | {0}".format("".join(byte_l))
            byte_l[:] = []
    if count:
        sys.stdout.write("   " * (16 - count))
        print " | {0}".format("".join(byte_l))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print " Usage: python {0} <file name> <# of bytes>".format(sys.argv[0])
        sys.exit(1)
    with open(sys.argv[1], 'rb') as f:
        print_l(f.read(int(sys.argv[2])))
