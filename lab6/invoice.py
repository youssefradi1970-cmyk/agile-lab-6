FEE_PER_HOUR = 1200
SCHOLARSHIP_RATE = 0.5
INTERNATIONAL_RATE = 2000
INTERNATIONAL_SERVICE_FEE = 5000


def make_invoice(student, kind):
    total = 0
    for code in student.courses:
        h = student.courses[code]
        if kind == "regular":
            total = total + h * FEE_PER_HOUR
        elif kind == "scholarship":
            total = total + h * FEE_PER_HOUR * SCHOLARSHIP_RATE
        elif kind == "international":
            total = total + h * INTERNATIONAL_RATE
    if kind == "international":
        total = total + INTERNATIONAL_SERVICE_FEE
    text = "Invoice for " + student.student_id + ": " + str(int(total)) + " EGP"
    f = open("invoice_" + student.student_id + ".txt", "w")
    f.write(text)
    f.close()
    print(text)
    return total