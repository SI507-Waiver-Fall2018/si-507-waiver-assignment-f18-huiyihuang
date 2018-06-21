# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
data_object = sqlite3.connect("Northwind_small.sqlite")
d = data_object.cursor()

#  python3 part2.py customers
if sys.argv[1] == 'customers':
	d.execute("SELECT Id, CompanyName FROM Customer")
	customer_d = d.fetchall()
	print("ID \t Customer Name")
	for everyrow in customer_d:
		print("{} \t {}".format(everyrow[0],everyrow[1]))

#  python3 part2.py employees
if sys.argv[1] == 'employees':
	d.execute("SELECT Id, FirstName, LastName FROM Employee")
	employee_d = d.fetchall()
	print("ID \t Employee Name")
	for everyrow in employee_d:
		print("{} \t {} {}".format(everyrow[0],everyrow[1],everyrow[2]))

#  python3 part2.py orders cust=<customer id>
if sys.argv[1] == 'orders' and sys.argv[2][:4] == 'cust':
	# d.execute("SELECT OrderDate FROM 'Order' WHERE CustomerId = %s " % sys.argv[2][5:])
	d.execute("SELECT OrderDate FROM 'Order' WHERE CustomerId = '{}'".format(sys.argv[2][5:]))
	orders_d = d.fetchall()
	print("Order Dates")
	for everyrow in orders_d:
		print("{}".format(everyrow[0]))


#  python3 part2.py orders emp=<employee last name>
if sys.argv[1] == 'orders' and sys.argv[2][:3] == 'emp':
	d.execute("SELECT Id FROM 'Employee' WHERE LastName = '{}'".format(sys.argv[2][4:]))
	person_id = d.fetchall()[0][0]
	d.execute("SELECT OrderDate FROM 'Order' WHERE EmployeeId = '{}'".format(person_id))
	employee_date = d.fetchall()
	print("Order Dates")
	for everyrow in employee_date:
		print("{}".format(everyrow[0]))
