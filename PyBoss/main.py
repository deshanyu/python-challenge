us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
import os
import csv
emp_id=[]
first_name=[]
last_name=[]
dob=[]
ssn=[]
state=[]
for employee_datafile in ["employee_data1.csv", "employee_data2.csv"]:
    employee_data_csv = os.path.join(employee_datafile)

    # Improved Reading using CSV module
    with open(employee_data_csv, newline="") as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)
        #  Each row is read as a row
    
        for row in csvreader:
            emp_id.append(row[0])
            first_name.append(row[1].split(' ')[0])
            last_name.append(row[1].split(' ')[1])
            dob_split=row[2].split('-')
            year=dob_split[0]
            month=dob_split[1]
            day=dob_split[2]
            dob.append(month +'/' + day + '/' + year )
            ssn.append('***-**-' + row[3].split('-')[2])
            state.append(us_state_abbrev[row[4]])

    new_csv = zip(emp_id, first_name, last_name, dob, ssn, state)

    # Set variable for output file
    output_file = os.path.join("new_" + employee_datafile)

    #  Open the output file
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # Write the header row
        writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

        # Write in zipped rows
        writer.writerows(new_csv)



    
   