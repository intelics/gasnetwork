from gasnetwork.typecurve.synthetictypecurve import SyntheticTypeCurve
from gasnetwork.utils import engunits
import matplotlib.pyplot as plt
import numpy as np
import json
# class Tester ():
    
#     def __init__(self, q_zero, q_peak):
#         #engineering units gas flow, measured in Standard Volume Flow (q) - converted to Million Standard Cubic Feet per Day (MMSCFD)
#         self.q_zero_converted = engunits.convert_value('svf', q_zero, 'MMSCFD')
#         self.q_peak_converted = engunits.convert_value('svf', q_peak, 'MMSCFD')

#     def test_synthetic_type_classes(self):
#         type_curve = SyntheticTypeCurve(self.q_zero_converted, self.q_peak_converted, 5, 6, 0, 1, 1)
#         # q_zero, q_peak, t_peak, t_plat, k, b, a
#         type_curve.t = 3

#         q=type_curve.calculate_synthetic_type_curve()

#         fig = plt.figure()
#         plt.plot(q, type_curve.t)
#         plt.xlabel('q[MMscf/d]')
#         plt.ylabel('t[months]')
#         plt.show()

        
# if __name__ == "__main__":
#     tester = Tester(10, 20)
#     tester.test_synthetic_type_classes()

q_zero = 0 # MMSCFD
q_zero = engunits.convert_value('svf', q_zero, 'MMSCFD')

q_peak = 10 # MMSCFD
q_peak = engunits.convert_value('svf', q_peak, 'MMSCFD')

type_curve = SyntheticTypeCurve(q_zero, q_peak, 5, 6, 0, 1, 1)
ts = list(range(12 * 30))
qs = type_curve.build_curve(ts)

print (ts)  # in months
print (qs)  # in Sm3/s
# to convert qs to MMSCFD
# qs = [engunits.convert_value(q.....) for q in qs]
# ref_series = json.load(open('ref_curve1.txt', 'r'))
fig = plt.plot(ts, qs)
plt.show()






