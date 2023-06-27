select codigo_id, greatest(max(e2),max(c1),max(s_11),max(i_2))
from fechas
group by codigo_id