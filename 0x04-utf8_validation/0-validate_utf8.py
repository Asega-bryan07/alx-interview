#!/usr/bin/python3
'''
a method that determines if a given data set represents a valid
UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer
'''
def validUTF8(data):
    '''
    A method that determines if a given data set represents a valid UTF-8 encoding.
    '''
    expected_continuation_bytes = 0

    # The bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10_000_000
    UTF8_BIT_2 = 1 << 7  # 01_000_000

    # Loop over for each input data byte
    for byte in data:
        '''
        Initialize a mask checking for leading 1's in the current byte.
        '''
        leading_one_mask = 1 << 7

        '''
        If still not expecting any continuation bytes.
        '''
        if expected_continuation_bytes == 0:
            '''
            Count the number of leading 1's in the current byte and
            determine the number of continuation bytes.
            '''
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask >> 1

            '''
            If it is not a multi-byte sequence.
            '''
            if expected_continuation_bytes == 0:
                continue

            '''
            If the number of continuation bytes is not between
            2 and 4, the sequence is invalid.
            '''
            if expected_continuation_bytes == 1 or \
                    expected_continuation_bytes > 4:
                return False
        # If we are expecting continuation bytes
        else:
            '''
            Check that the byte starts with a '10' prefix and not '11'.
            '''
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

            '''
            Decrement the expected number of continuation bytes.
            '''
            expected_continuation_bytes -= 1

            '''
            If we have processed all bytes and not encountered
            any other continuation bytes, the sequence is valid.
            '''
            if expected_continuation_bytes == 0:
                return True
            else:
                return False
