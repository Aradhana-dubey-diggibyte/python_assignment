from datetime import datetime

def time_difference(t1: str, t2: str) -> int:
    # Format to parse the datetime string including timezone
    format_str = '%a %d %b %Y %H:%M:%S %z'
    
    dt1 = datetime.strptime(t1, format_str)
    dt2 = datetime.strptime(t2, format_str)
    
    # Calculate absolute difference in seconds
    diff = abs(int((dt1 - dt2).total_seconds()))
    return diff
