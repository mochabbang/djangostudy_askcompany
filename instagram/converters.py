class YearConvert:
    regex = r"20\d{2}"
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)
    
    
class MonthConverter(YearConvert):
    regex = r"\d{1,2}" # "02" => 2
        
class DayConverter(YearConvert):
    regex = r"[0123]\d" # "02" => 2
    