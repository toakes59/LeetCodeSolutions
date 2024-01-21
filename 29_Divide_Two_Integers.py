class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == 0:
            return 0

        if divisor == 1:
            quotient = dividend
        elif divisor == -1:
            quotient = -dividend
        else:
            sign = 1 if (dividend > 0) == (divisor > 0) else -1
            dividend = abs(dividend)
            divisor = abs(divisor)
            quotient = 0

            while dividend >= divisor:
                temp_divisor, multiple = divisor, 1
                while dividend > (temp_divisor << 1):
                    temp_divisor <<= 1
                    multiple <<= 1
                dividend -= temp_divisor
                quotient += multiple

            quotient *= sign

        if quotient > INT_MAX:
            return INT_MAX
        elif quotient < INT_MIN:
            return INT_MIN
        else:
            return quotient
