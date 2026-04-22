# Write your code here
# Note: You can write your input manually
def validate_data(raw_data):
    validation_summary = {
        "data": None,
        "error" : None
    }

    col_names = ["id", "sales", "revenue"]



    if not isinstance(raw_data, list):
        validation_summary["error"] = "Mismatch input type"
        return validation_summary

    if len(raw_data) < 2:
        validation_summary["error"] = "Mismatch input size. The data is not in 2D"
        return validation_summary

    for col in raw_data[0]:
        if col not in col_names:
          validation_summary['error'] = "Mismatch data columns name"
          return validation_summary

    if raw_data[0] != col_names:
        validation_summary['error'] = "Mismatch data columns sequence"
        return validation_summary
    
    data_error = []

    for i in range(1,len(raw_data)):
      detail_error = []

      for j in range(len(raw_data[i])):
        if raw_data[i][j] == None:
          detail_error.append(f"None value on col:{col_names[j]}")
        
        elif j==0:
          if not isinstance(raw_data[i][j], str):
            detail_error.append(f"Mismatch input type on col:{col_names[j]}. Should be a string")
    
        elif j!=0:
          if not isinstance(raw_data[i][j], (int, float)):
            detail_error.append(f"Mismatch input type on col:{col_names[j]}. Should be a number")

        elif raw_data[i][j] < 0:
            detail_error.append(f"Negative value on col:{col_names[j]}")

      if detail_error:
        data_error.append({'index': i, "error":detail_error})

    validation_summary['error'] = data_error
    if not validation_summary['error']:
      validation_summary['data'] = raw_data
    
    return validation_summary
    # bisa pakai conditional statemen
    # jika tipenya buka list
