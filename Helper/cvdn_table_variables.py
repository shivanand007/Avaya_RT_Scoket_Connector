import re


def cvdn_table_variables_extraction(cms_string):


    # Split the CM string into individual values
    values = re.split(r'\|', cms_string)

    # Create a dictionary to store the column names and values
    cvdn_data = {
        'F1': values[0].strip(),
        'VDN': int(values[1].strip()) if values[1].strip() else 0,
        'VDN_SYNONYM': values[2].strip(),
        'INPROGRESS_ATAGENT': int(values[3].strip()) if values[3].strip() else 0,
        'OLDESTCALL': values[4].strip(),
        'AVG_ANSWER_SPEED': values[5].strip(),
        'ABNCALLS': int(values[6].strip()) if values[6].strip() else 0,
        'AVG_ABANDON_TIME': values[7].strip(),
        'ACDCALLS': int(values[8].strip()) if values[8].strip() else 0,
        'AVG_ACD_TALK_TIME': values[9].strip(),
        'ACTIVECALLS': int(values[10].strip()) if values[10].strip() else 0
    }



    # Print the CVDN data dictionary
    print(cvdn_data)
    return cvdn_data

