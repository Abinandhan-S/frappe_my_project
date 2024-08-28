import frappe

def get_doc_fun():
    doc=frappe.get_doc("employee_database", "Gowtham-0033")
    doc.first_name="EMP-0008"
    doc.save()
    doc.reload()