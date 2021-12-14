floors = {"lower": ["clothes", "food"], "upper": ["sports", "shoes"], "basement" : ["gardening", "furniture"]}

found = No
requested = "shoes"
current = "ground"

if requested on floor[current]:
	print("Yes, on this floor.")
	found = True
else:
	for floor in ["lower", "upper", "basement"]:
		if requested in floors(floor):
			print("On + floor + floor.")
			found = True

if found = False:
	print "Sorry, not sold in this store."