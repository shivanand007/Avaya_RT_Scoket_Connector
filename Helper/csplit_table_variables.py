import re


def csplit_table_variables_extraction(cms_string):

    # Split the CM string into individual values
    values = re.split(r'\|', cms_string)

    # Create a dictionary to store the column names and values
    csplit_data = {
        'F1': values[0].strip(),
        'SPLIT': int(values[1].strip()),
        'INQUEUE_INRING': int(values[2].strip()),
        'AVAILABLE': int(values[3].strip()),
        'ANSTIME_ACDTALKCALLS': values[4].strip(),
        'ABNCALLS': int(values[5].strip()),
        'ACD': int(values[6].strip()),
        'OLDESTCALL': values[7].strip(),
        'ACD_CALLS': int(values[8].strip()),
        'ACDTIME_ACD_CALLS': values[9].strip(),
        'ABNTIME_ABNCALLS': values[10].strip(),
        'AGINRING': int(values[11].strip()),
        'ONACD': int(values[12].strip()),
        'INACW': int(values[13].strip()),
        'OTHER': int(values[14].strip()),
        'IN_AUX': int(values[15].strip()),
        'STAFFED': int(values[16].strip()),
        'EWTHIGH': values[17].strip(),
        'EWTMEDIUM': values[18].strip(),
        'EWTLOW': values[19].strip(),
        'DA_INQUEUE_DA_INRING': int(values[20].strip()),
        'ACCEPTABLE_CALLSOFFERED': int(values[21].strip()),
        'SERVICELEVEL': int(values[22].strip()),
        'CALLSOFFERED': int(values[23].strip())
    }

    # Print the CSPLIT data dictionary
    print(csplit_data)
    return csplit_data
