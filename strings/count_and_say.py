class Solution:
    def countAndSay(self, n: int) -> str:
        # Initial condition for output
        output = '1'

        while n > 1:
            # Use two pointers to count identical elements in the string
            # Start from first element in the string
            i = j = 0

            # Make copy of output string
            temp_str = output

            # Restart output string
            output = ''

            # While end sequence pointer (j) is less than length of the string
            while j < len(temp_str):

                # If elements are the same at start (i) and end (j) of sequence
                if temp_str[i] == temp_str[j]:

                    # We increment j
                    j += 1
                else:

                    # If elements are different we count how many elements are between i and j and add it to the output string
                    # Sequence is ['count' + 'element'] : example: '21',  count = 1, element = '2' and count = 1, element = '1',  makes it 1211
                    output += str(j - i) + temp_str[i]

                    # Restart the sequence
                    i = j

            # Once we reach the end of the list we add the count and element to the output string
            output += str(j - i) + temp_str[i]

            # The output string will go back to the top of the loop if n > 1 and then script will run again with new output string
            n -= 1

        return output