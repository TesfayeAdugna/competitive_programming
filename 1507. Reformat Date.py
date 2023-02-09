class Solution:
    def reformatDate(self, date: str) -> str:



        day, month, year = date.split(' ')
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        dayDigits = "".join(char if char.isdigit() else "" for char in day) 
        dayDigits = dayDigits if len(dayDigits) > 1 else "0" + dayDigits 
        
        return year + "-" + months[month] + "-" + dayDigits
