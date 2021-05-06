'''
Construct a function for validating if the input string was a valid number.

Positive test cases:
    Integers: 1, 2, ..
    Floating point numbers: 3.1, 1.1, .123, ..
    Numbers with positive/negative sign: -1, +9, ..
    Scientific notations: 1.1e-9

Negative test cases:
    Invalid dots: 1.3.2, ..
    Invalid characters: mn, ..
    Spaces between numbers: 1 2, ..
    Combinations: 1 2m, %hgdj, ..

'''
    

def is_valid_number(test_str):
    '''
    Verify if the input string was a valid number.
    Parameters:
        test_str: str
            Input string for validation.
    Returns:
        bool
            Return True if the string was a valid number, otherwise, return False.
    '''
    
    num1_occurred = num2_occurred = num3_occurred = dot_occurred = e_occurred = False             # Setup components that needed to be checked
    s = test_str.strip()                                                                          # Get rid of the spaces at the begining and the end
    idx = 0
    while idx < len(s):
        if s[idx] in '+-':                                                                        # Positive/negative sign can be at the begining or after 'e'
            if idx > 0 and s[idx - 1] != 'e':
                print("Invalid pos/neg position occurred in \"{0}\"".format(s))
                return False

        elif s[idx].isdigit():                                                                    # Check the digit for different sections
            while idx < len(s) and s[idx].isdigit():
                idx += 1
            if not dot_occurred and not e_occurred:
                num1_occurred = True
            elif dot_occurred and not e_occurred:
                num2_occurred = True
            elif e_occurred:
                num3_occurred = True
            continue
            
        elif s[idx] == '.':                                                                       # Dot can only occur once and before 'e'
            if dot_occurred or e_occurred:
                print("Invalid dot occurred in \"{0}\"".format(s))
                return False
            dot_occurred = True
        
        elif s[idx] == 'e':                                                                       # 'e" can only occur once
            if e_occurred:
                print("Invalid scientific notation occurred in \"{0}\"".format(s))
                return False
            e_occurred = True

        else:                                                                                     # Any characters except 'e' should be view as invalid
            print("Invalid character occurred in \"{0}\"".format(s))
            return False
        
        idx += 1
    
    return (num1_occurred or num2_occurred) and not (e_occurred ^ num3_occurred)                  # Verify if the digits were located in the correct section


def is_valid_number_state_machine(test_str):
    '''
    Verify if the input string was a valid number with state machine.
    
    States:
        0: Init
        1: '+', '-' at the begining
        2: Digits before 'e' or '.'    -> final state
        3: '.' occurred
        4: Digits after '.' before 'e' -> final state
        5: 'e' occurred
        6: '+', '-' after 'e'
        7: Digits after 'e'            -> final state
        
        
    Parameters:
        test_str: str
            Input string for validation.
    Returns:
        bool
            Return True if the string was a valid number, otherwise, return False.
    '''
    
    s = test_str.strip()
    state = 0
    for i in range(len(s)):
        if s[i] in '+-':
            if state == 0 or state == 5:
                state += 1
            else:
                print("Invalid pos/neg position occurred in \"{0}\"".format(s))
                return False
            
        elif s[i].isdigit():
            if state < 2:
                state = 2
            elif 3 <= state <= 4:
                state = 4
            elif 5 <= state <= 7:
                state = 7
                
        elif s[i] == '.':
            if state <= 2:
                state = 3
            else:
                print("Invalid dot occurred in \"{0}\"".format(s))
                return False
            
        elif s[i] == 'e':
            if state == 2 or state == 4:
                state = 5
            else:
                print("Invalid scientific notation occurred in \"{0}\"".format(s))
                return False
            
        else:
            print("Invalid character occurred in \"{0}\"".format(s))
            return False
        
    return state in [2, 4, 7]


if __name__ == "__main__":
    for test_method in [is_valid_number, is_valid_number_state_machine]:
        # Integers
        assert test_method('1') == True

        # Floating point numbers
        assert test_method('3.1') == True
        assert test_method('.123') == True

        # Numbers with positive/negative sign
        assert test_method('-1.3') == True
        assert test_method('+9') == True

        # Scientific notations
        assert test_method('+1.1e-9') == True

        # Invalid dots
        assert test_method('1.3.2') == False
        assert test_method('2e9.1') == False

        # Invalid pos/neg sign
        assert test_method('2+2') == False
        assert test_method('3e9-2') == False
        
        # Invalid scientific notations
        assert test_method('e-10') == False
        
        # Invalid characters
        assert test_method('mn') == False

        # Invalid spaces between numbers
        assert test_method('1 2') == False

        # Invalid Combinations
        assert test_method('1m') == False
        assert test_method('1 2m') == False
        assert test_method('%hgdj') == False

        # Spaces before and after could be seen as valid
        assert test_method(' 1.2 ') == True
    
        print("All test cases passed with test method: \"{0}\"".format(test_method.__name__))
    