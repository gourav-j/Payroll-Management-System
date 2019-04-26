from pms.models import User, SalaryStructure, Salary, Attendance
import datetime
import calendar

def update():
	user = User.objects.all()
	for u in user:
		try:
			structure = SalaryStructure.objects.get(user = u)
		except SalaryStructure.DoesNotExist:
		#print("LL")
			structure = None
		if structure:
			pf = structure.basic_salary+structure.DA+structure.HRA
			pf = pf*0.12
			gross = structure.basic_salary+structure.DA+structure.HRA+structure.conveyance_allowance+structure.bonus-pf-structure.medical_insurance
			today = datetime.date.today()
			first = today.replace(day=1)
			last = first - datetime.timedelta(days=1)
			sundays = len([1 for i in calendar.monthcalendar(last.year,
                                last.month) if i[6] != 0])
			total_days = calendar.monthrange(last.year,last.month)[1]
			leaves=0
			Salary.objects.create(user = u,gross_salary = gross, leave = leaves)
