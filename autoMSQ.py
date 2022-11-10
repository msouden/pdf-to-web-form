import sys, os, subprocess, PyPDF2, regex, urllib.parse, webbrowser


### The URL we want to open:

url = 'https://not.a.real/url/referral_form'

### Define the field Ids (HTML field classes) with sensible names

entering_email = 'field45865550'
work_comp_type = 'field45865551'
claim_number = 'field45865552'
adj_fname = 'field45865555-first'
adj_lname = 'field45865555-last'
adj_email = 'field45865559'
adj_phn = 'field45865560'
ins_co = 'field45865561'
iw_fname = 'field45865574-first'
iw_mid_initial = 'field45865574-initial'
iw_lname = 'field45865574-last'
iw_phn1 = 'field45865575'
# iw_phn2 = 'field45865576'
iw_add_1 = 'field45865578-address'
iw_add_2 = 'field45865578-address2'
iw_city = 'field45865578-city'
iw_state = 'field45865578-state'
iw_zip = 'field45865578-zip'
iw_dob = 'field45865580'
iw_doi = 'field45865581'
employer = 'field45865584'
exam_1 = 'field45865589'
modality_1 = 'field45865590'
exam_1_without = 'field45865591_1'
exam_1_with = 'field45865591_2'
exam_1_wandwithout = 'field45865591_3'
exam_2 = 'field45865595'
modality_2 = 'field45865596'
exam_2_without = 'field45865597_1'
exam_2_with = 'field45865597_2'
exam_2_wandwithout = 'field45865597_3'
additional_instructions = 'field45865603'
phy_name = 'field45865607-first'
#phy_last_name = 'field45865607-last'
phy_phn = 'field45865608'
phy_fax_number = 'field45865609'
phy_add_1 = 'field45865610-address'
phy_city = 'field45865610-city'
phy_state = 'field45865610-state'
phy_zip = 'field45865610-zip'


pdffile = sys.argv[1]

#Old version was a script that asked for the pdf
#pdffile = input('Please enter the file name:')

#open the pdf in default application for reviewing
subprocess.Popen([pdffile],shell=True)

### Extract the text of the QA and write it to text-extract.txt

with open (pdffile, 'rb') as pdfFileObj, open (pdffile+'-text.txt', 'w') as text_file:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    number_of_pages = pdfReader.getNumPages()
    for page_number in range(number_of_pages):
        pageObj = pdfReader.getPage(page_number)
        page_text = pageObj.extractText().replace('\n','|')
        text_file.write(page_text)

### Open the generated text file and
#  search and obtain matches/values for each field's contents

with open (pdffile+'-text.txt', 'r') as text_file:
    text = text_file.read() 
    entering_email_value = regex.search(r'(?<=Email:\|)(.*?)(?=\|)(?=.*\|Adjuster Information:)|$', text)
    wc_type_value = 'Workers Compensation'
    claim_number_value = regex.search(r'(?<=Claim Number:\|)(.*?)(?=\|)|$', text)
    adj_fname_value = regex.search(r'(?<=Physician Information:\|.*.Name:\|)(.*?)(?=\|)(?=.*\|Adjuster Information:)|$', text)
    #adj_lname_value = regex.search(r'(?<=Physician Information:\|.*.Name:\|.* )(.*?)(?=\|)(?=.*\|Adjuster Information:)|$', text)
    adj_email_value = regex.search(r'(?<=Physician Information:\|.*)(?<=.Email:\|)(.*?)(?=\|)(?=.*\|Adjuster Information:)|$', text)
    ins_co_value = regex.search(r'(?<=Claim Number:\|.*\|)(.*?)(?=\|Claim Payer:)|$', text)
    iw_fname_value = regex.search(r'(?<=First Name:\|)(.*?)(?=\|)|$', text)
    iw_lname_value = regex.search(r'(?<=Last Name:\|)(.*?)(?=\|)|$', text)
    iw_phn1_value = regex.search(r'(?<=Date Services Needed:.*)(?:\([2-9]\d{2}\)\ ?|[2-9]\d{2}(?:\-?|\ ?))[2-9]\d{2}[- ]?\d{4}(?=.*Physician Information:)|$', text)
    iw_add_1_value = regex.search(r'(?<=Last Name:\|.*Address:\|)(.*?)(?=\|)(?=.*Patient Information:)|$', text)
    iw_city_value = regex.search(r'(?<=Last Name:\|.*City & State:\|)(.*?)(?=,)(?=.*Patient Information:)|$', text)
    iw_state_value = regex.search(r'(?<=Last Name:\|.*)(?<=, )(.*?)(?= )(?=.*Patient Information:)|$', text)
    iw_zip_value = regex.search(r'(?<=Last Name:\|.*, [A-Z][A-Z] )(.*?)(?=\|)(?=.*Patient Information:)|$', text)
    iw_dob_value = regex.search(r'(?<=Date Services Needed:\|.*)([A-Z].*?)(?= [0-9][0-9]:[0-9][0-9])|$', text)
    iw_doi_value = regex.search(r'(?<=Date of Injury:\|)(.*?)(?=\|)|$', text)
    employer_value = regex.search(r'(?<=Date of Injury:\|.*Employer:\|)(.*?)(?=\|Diagnosis:)|$', text)
    exam_1_value = regex.search(r'(?<=Case Manager Information:\|.*)(CT|MRI|EMG|MRI Arthrogram|CT Arthrogram|Ultrasound)(?=.*Payer Notes:\|)|$', text)
    additional_instructions_value = regex.search(r'(?<=\|Amount\|.*)(.*)|$', text)
    phy_name_value = regex.search(r'(?<=Date Services Needed:\|.*Name:\|)(.*?)(?=\|)(?=.*Physician Information:)|$', text)
    phy_phn_value = regex.search(r'(?<=Physician Information:\|.*\|[A-Z][A-Z]\|)(.*?)(?=\|Name:)(?=.*Adjuster Information:)|$', text)
    phy_add_1_value = regex.search(r'(?<=Physician Information:\|.*Phone:\|)(.*?)(?=\|[A-Z][A-Z]\|)|$', text)
    phy_city_value = regex.search(r'(?<=Date Services Needed:\|.*City:\|)(.*?)(?=\|)|$', text)
    phy_state_value = regex.search(r'(?<=Physician Information:\|.*\|)([A-Z][A-Z])(?=\|)|$', text)
    phy_zip_value = regex.search(r'(?<=Date Services Needed:\|.*Zip:\|)(.*?)(?=\|)|$', text)

#Assign these findings to the matching field

getVars = {entering_email: entering_email_value.group(), 
            work_comp_type: 'Workers Compensation',  # always
            claim_number: claim_number_value.group(),
            adj_fname: adj_fname_value.group(),
            adj_email: adj_email_value.group(),
            ins_co: ins_co_value.group(),
            iw_fname: iw_fname_value.group(),
            iw_lname: iw_lname_value.group(),
            iw_phn1: iw_phn1_value.group(),
            iw_add_1: iw_add_1_value.group(),
            iw_city: iw_city_value.group(),
            iw_state: iw_state_value.group(),
            iw_zip: iw_zip_value.group(),
            iw_dob: iw_dob_value.group(),
            iw_doi: iw_doi_value.group(),
            employer: employer_value.group(),
            exam_1: exam_1_value.group(),
            additional_instructions: additional_instructions_value.group(),
            phy_name: phy_name_value.group(),
            phy_phn: phy_phn_value.group(),
            phy_add_1: phy_add_1_value.group(),
            phy_city: phy_city_value.group(),
            phy_state: phy_state_value.group(),
            phy_zip: phy_zip_value.group()}

#Open the web form page and write the values to the correct fields>

webbrowser.open(url + urllib.parse.urlencode(getVars), new=0, autoraise=True)
# print (entering_email_value.group(), claim_number_value.group(), adj_fname_value.group(), adj_email_value.group(), 
#         ins_co_value.group().strip('|'), iw_fname_value.group(), iw_lname_value.group(), iw_phn1_value.group(), iw_add_1_value.group(), iw_city_value.group())
# print (iw_state_value.group(), iw_zip_value.group())
os.remove(pdffile+'-text.txt')
