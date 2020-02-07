from gasnetwork.typecurve.synthetictypecurve import SyntheticTypeCurve
from gasnetwork.utils import engunits
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import json
import matplotlib.patches as mpatches 

#C:\Users\username\storagelocation\gasnetworkfinal\gasnetwork-master>python ./run_tests.py

# q_zero = 0 # MMSCFD
# q_zero = engunits.convert_value('svf', q_zero, 'MMSCFD')

# q_peak = 10 # MMSCFD
# q_peak = engunits.convert_value('svf', q_peak, 'MMSCFD')

# type_curve = SyntheticTypeCurve(360, q_zero, q_peak, 5, 6, 0, 1, 1)
# ts = list(range(type_curve.months))
# qs = type_curve.build_q_a()
# qs_conv = [0]*len(qs)

# for i in range(len(qs)):
#     qs_conv[i] = engunits.convert_value('svf', qs[i], 'MMSCFD')
# fig1 = plt.plot(ts, qs_conv, 'b', label = 'synthetic type curve')
# print(qs_conv) #in MMSCFD

# ref_series = json.load(open('ref_curve.py'))
# qs_ref=ref_series["qs"]
# ts=ref_series["ts"]
# fig2 = plt.plot(ts, qs_ref, 'r', label = 'referral curve')
# print (qs_ref)  # in MMSCFD

# plt.ylabel('gas flow (MMSCFD)')
# plt.xlabel('time (months)')

# plt.show()

q_zero = 0 # MMSCFD
q_zero = engunits.convert_value('svf', q_zero, 'MMSCFD')

q_peak = 10 # MMSCFD
q_peak = engunits.convert_value('svf', q_peak, 'MMSCFD')

type_curve = SyntheticTypeCurve(360, q_zero, q_peak, 5, 6, 0, 1, 1)
ts = list(range(type_curve.months))

qs = type_curve.build_q_c()
qs_conv = [0] * len(qs)

ps = type_curve.find_p()
ps_conv = [0] * len(ps)

for i in range(len(qs)):
    qs_conv[i] = engunits.convert_value('svf', qs[i], 'MMSCFD')
    ps_conv[i] = engunits.convert_value('Pa', ps[i], 'kPag')
print (qs_conv)
print (ps_conv)

fig1 = plt.plot(qs_conv, ps_conv)
plt.xlabel('Flow[MMSCFD]')
plt.ylabel('Pressure[kPag]')
plt.title('Inflow Performance Curve over Time for n=' + str(type_curve.n))
plt.show()





