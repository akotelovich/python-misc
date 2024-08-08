def convert_str(match_obj):    
  if match_obj.group(1) is not None and match_obj.group(2) is not None:        
    return match_obj.group(1) + "\"" + re.sub(r"\s+", " ", match_obj.group(2)) +"\""


string = '''set one "thing"
set comment "test 
test"
set other "test"'''

match = re.sub(r"^(set comment )\"([^\"]*)\"$", convert_str, o, flags=re.M)
