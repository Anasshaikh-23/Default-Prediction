import requests
import json

url = "http://192.168.1.211:5000/prediction"

payload = json.dumps({
  "Gender": 0,
  "Married": 0,
  "Dependents": 10,
  "Education": 1,
  "Self_Employed": 0,
  "ApplicantIncome": 1,
  "CoapplicantIncome": 0,
  "LoanAmount": 104300,
  "Loan_Amount_Term": 36,
  "Credit_History": 0,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
