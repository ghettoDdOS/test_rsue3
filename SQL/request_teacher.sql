SELECT D.day,DS.subject, PR.time_str, TC.full_name, AD.name, TP.type, POS.position, WE.parity
FROM shedule AS RP
JOIN days AS D 
ON D.id = RP.day
JOIN subjects AS DS
ON DS.id = RP.subject AND
D.id = 1
JOIN classes as PR
ON PR.id = RP.class
JOIN teachers AS TC
ON TC.id = RP.teacher
JOIN positions_of_teacher AS POS
ON POS.id = TC.position
JOIN audiences AS AD
ON AD.id = RP.audience
JOIN type_of_classes AS TP
ON TP.id = RP.type_of_class
JOIN weeks as WE
ON WE.id = RP.week
WHERE TC.full_name='ДОЛЖЕНКО А.И.'
ORDER BY start_time
