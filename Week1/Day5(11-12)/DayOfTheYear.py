class Solution:
    def dayOfYear(self, date: str) -> int:
        date_format = date.split('-')
        year = int(date_format[0])
        month = int(date_format[1])
        day = int(date_format[2])

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if month == 1:
                return day
            elif month == 2:
                return 31 + day
            elif month == 3:
                return 60 + day
            elif month == 4:
                return 91 + day
            elif month == 5:
                return 121 + day
            elif month == 6:
                return 152 + day
            elif month == 7:
                return 182 + day
            elif month == 8:
                return 213 + day
            elif month == 9:
                return 244 + day
            elif month == 10:
                return 274 + day
            elif month == 11:
                return 305 + day
            elif month == 12:
                return 335 + day
        else:
            if month == 1:
                return day
            elif month == 2:
                return 31 + day
            elif month == 3:
                return 59 + day
            elif month == 4:
                return 90 + day
            elif month == 5:
                return 120 + day
            elif month == 6:
                return 151 + day
            elif month == 7:
                return 181 + day
            elif month == 8:
                return 212 + day
            elif month == 9:
                return 243 + day
            elif month == 10:
                return 273 + day
            elif month == 11:
                return 304 + day
            elif month == 12:
                return 334 + day

solution = Solution()
print(solution.dayOfYear("2004-03-01"))