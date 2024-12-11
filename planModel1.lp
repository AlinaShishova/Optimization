\* OptimalPlan *\
Minimize
OBJ: Span
Subject To
_C1: - Span + StartTime_('job1',_'R1') <= -10
_C10: 80 Order_job2_R1_before_job3_R1 + 0 StartTime_('job2',_'R1') <= 60
_C11: - 80 Order_job2_R1_before_job3_R1 - StartTime_('job2',_'R1')
 + StartTime_('job3',_'R1') <= -30
_C2: - Span + StartTime_('job2',_'R1') <= -20
_C3: - Span + StartTime_('job3',_'R1') <= -30
_C4: - Span + StartTime_('job4',_'R2') <= -5
_C5: - Span + StartTime_('job5',_'R3') <= -15
_C6: 80 Order_job1_R1_before_job2_R1 + 0 StartTime_('job1',_'R1') <= 70
_C7: - 80 Order_job1_R1_before_job2_R1 - StartTime_('job1',_'R1')
 + StartTime_('job2',_'R1') <= -20
_C8: 80 Order_job1_R1_before_job3_R1 + 0 StartTime_('job1',_'R1') <= 70
_C9: - 80 Order_job1_R1_before_job3_R1 - StartTime_('job1',_'R1')
 + StartTime_('job3',_'R1') <= -30
Bounds
 0 <= Span <= 80
 0 <= StartTime_('job1',_'R1') <= 80
 0 <= StartTime_('job2',_'R1') <= 80
 0 <= StartTime_('job3',_'R1') <= 80
 0 <= StartTime_('job4',_'R2') <= 80
 0 <= StartTime_('job5',_'R3') <= 80
Generals
Span
StartTime_('job1',_'R1')
StartTime_('job2',_'R1')
StartTime_('job3',_'R1')
StartTime_('job4',_'R2')
StartTime_('job5',_'R3')
Binaries
Order_job1_R1_before_job2_R1
Order_job1_R1_before_job3_R1
Order_job2_R1_before_job3_R1
End
