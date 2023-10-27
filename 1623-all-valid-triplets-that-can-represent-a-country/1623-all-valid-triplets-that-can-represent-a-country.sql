# Write your MySQL query statement below
select distinct schoola.student_name as member_A,
schoolb.student_name as member_B,
schoolc.student_name as member_C

from schoola join schoolb join schoolc
where schoola.student_id <> schoolb.student_id and
schoola.student_id <> schoolc.student_id and
schoolb.student_id <> schoolc.student_id and 
schoola.student_name <> schoolb.student_name and
schoola.student_name <> schoolc.student_name and
schoolb.student_name <> schoolc.student_name