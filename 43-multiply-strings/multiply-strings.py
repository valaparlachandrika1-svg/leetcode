class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        # Multiply digit by digit
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert result array to string
        ans = ""

        for digit in result:
            if not (ans == "" and digit == 0):
                ans += str(digit)

        return ans
        