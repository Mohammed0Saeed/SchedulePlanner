from classes import plan, util

newPlan = plan.Plan("UNIVERSITY", util.load_courses("courses.csv"))

newPlan.create_plan()
newPlan.print_plan()
newPlan.export_plan("plan.csv")
