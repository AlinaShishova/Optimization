\* optimalPlan *\
Minimize
OBJ: completion_J1 + completion_J10 + completion_J11 + completion_J12
 + completion_J13 + completion_J14 + completion_J15 + completion_J16
 + completion_J2 + completion_J3 + completion_J4 + completion_J5
 + completion_J6 + completion_J7 + completion_J8 + completion_J9
Subject To
_C1: - completion_J1 - start_J1 + start_J2 >= 0
_C10: - completion_J3 + start_J2 - start_J3 >= 0
_C11: - completion_J2 - start_J2 + start_J8 >= 0
_C12: - completion_J8 + start_J2 - start_J8 >= 0
_C13: - completion_J2 + start_J11 - start_J2 >= 0
_C14: - completion_J11 - start_J11 + start_J2 >= 0
_C15: - completion_J3 - start_J3 + start_J8 >= 0
_C16: - completion_J8 + start_J3 - start_J8 >= 0
_C17: - completion_J3 + start_J11 - start_J3 >= 0
_C18: - completion_J11 - start_J11 + start_J3 >= 0
_C19: - completion_J8 + start_J11 - start_J8 >= 0
_C2: - completion_J2 + start_J1 - start_J2 >= 0
_C20: - completion_J11 - start_J11 + start_J8 >= 0
_C21: - completion_J4 - start_J4 + start_J9 >= 0
_C22: - completion_J9 + start_J4 - start_J9 >= 0
_C23: - completion_J4 + start_J12 - start_J4 >= 0
_C24: - completion_J12 - start_J12 + start_J4 >= 0
_C25: - completion_J9 + start_J12 - start_J9 >= 0
_C26: - completion_J12 - start_J12 + start_J9 >= 0
_C27: - completion_J5 - start_J5 + start_J6 >= 0
_C28: - completion_J6 + start_J5 - start_J6 >= 0
_C29: - completion_J5 - start_J5 + start_J7 >= 0
_C3: - completion_J1 - start_J1 + start_J3 >= 0
_C30: - completion_J7 + start_J5 - start_J7 >= 0
_C31: - completion_J5 + start_J10 - start_J5 >= 0
_C32: - completion_J10 - start_J10 + start_J5 >= 0
_C33: - completion_J5 + start_J13 - start_J5 >= 0
_C34: - completion_J13 - start_J13 + start_J5 >= 0
_C35: - completion_J6 - start_J6 + start_J7 >= 0
_C36: - completion_J7 + start_J6 - start_J7 >= 0
_C37: - completion_J6 + start_J10 - start_J6 >= 0
_C38: - completion_J10 - start_J10 + start_J6 >= 0
_C39: - completion_J6 + start_J13 - start_J6 >= 0
_C4: - completion_J3 + start_J1 - start_J3 >= 0
_C40: - completion_J13 - start_J13 + start_J6 >= 0
_C41: - completion_J7 + start_J10 - start_J7 >= 0
_C42: - completion_J10 - start_J10 + start_J7 >= 0
_C43: - completion_J7 + start_J13 - start_J7 >= 0
_C44: - completion_J13 - start_J13 + start_J7 >= 0
_C45: - completion_J10 - start_J10 + start_J13 >= 0
_C46: - completion_J13 + start_J10 - start_J13 >= 0
_C5: - completion_J1 - start_J1 + start_J8 >= 0
_C6: - completion_J8 + start_J1 - start_J8 >= 0
_C7: - completion_J1 - start_J1 + start_J11 >= 0
_C8: - completion_J11 + start_J1 - start_J11 >= 0
_C9: - completion_J2 - start_J2 + start_J3 >= 0
lim_line_0: completion_J5 - start_J4 <= 0
lim_line_1: completion_J4 - start_J3 <= 0
lim_line_2: completion_J3 - start_J2 <= 0
lim_line_3: completion_J13 - start_J9 <= 0
lim_line_4: completion_J11 - start_J10 <= 0
lim_time_J1: completion_J1 - start_J1 = 10
lim_time_J10: completion_J10 - start_J10 = 15
lim_time_J11: completion_J11 - start_J11 = 30
lim_time_J12: completion_J12 - start_J12 = 20
lim_time_J13: completion_J13 - start_J13 = 30
lim_time_J14: completion_J14 - start_J14 = 10
lim_time_J15: completion_J15 - start_J15 = 5
lim_time_J16: completion_J16 - start_J16 = 25
lim_time_J2: completion_J2 - start_J2 = 20
lim_time_J3: completion_J3 - start_J3 = 30
lim_time_J4: completion_J4 - start_J4 = 5
lim_time_J5: completion_J5 - start_J5 = 15
lim_time_J6: completion_J6 - start_J6 = 20
lim_time_J7: completion_J7 - start_J7 = 10
lim_time_J8: completion_J8 - start_J8 = 15
lim_time_J9: completion_J9 - start_J9 = 5
Bounds
 0 <= completion_J1
 0 <= completion_J10
 0 <= completion_J11
 0 <= completion_J12
 0 <= completion_J13
 0 <= completion_J14
 0 <= completion_J15
 0 <= completion_J16
 0 <= completion_J2
 0 <= completion_J3
 0 <= completion_J4
 0 <= completion_J5
 0 <= completion_J6
 0 <= completion_J7
 0 <= completion_J8
 0 <= completion_J9
 0 <= start_J1
 0 <= start_J10
 0 <= start_J11
 0 <= start_J12
 0 <= start_J13
 0 <= start_J14
 0 <= start_J15
 0 <= start_J16
 0 <= start_J2
 0 <= start_J3
 0 <= start_J4
 0 <= start_J5
 0 <= start_J6
 0 <= start_J7
 0 <= start_J8
 0 <= start_J9
Generals
completion_J1
completion_J10
completion_J11
completion_J12
completion_J13
completion_J14
completion_J15
completion_J16
completion_J2
completion_J3
completion_J4
completion_J5
completion_J6
completion_J7
completion_J8
completion_J9
start_J1
start_J10
start_J11
start_J12
start_J13
start_J14
start_J15
start_J16
start_J2
start_J3
start_J4
start_J5
start_J6
start_J7
start_J8
start_J9
End
