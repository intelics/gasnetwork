from gasnetwork.typecurve.synthetictypecurve import SyntheticTypeCurve
from gasnetwork.utils import engunits
import matplotlib.pyplot as plt
import numpy as np
import json

q_zero = 0 # MMSCFD
q_zero = engunits.convert_value('svf', q_zero, 'MMSCFD')

q_peak = 10 # MMSCFD
q_peak = engunits.convert_value('svf', q_peak, 'MMSCFD')

type_curve = SyntheticTypeCurve(q_zero, q_peak, 5, 6, 0, 1, 1)
ts = list(range(12 * 30))
qs = type_curve.build_curve(ts)

#referral curve
# data = json.dumps({
#     "success": True,
#         "data":[
#             {
#                 "qs": [0.003586945, 0.004451828, 0.005321532, 0.007187207, 0.009798565, 0.012047511, 0.015235924, 0.018384252, 0.021770349, 0.02626894, 0.033534579, 0.039711135, 0.046150247, 0.053633453, 0.061170181, 0.070424316, 0.078825899, 0.09075108, 0.099687426, 0.109503742, 0.119162246, 0.129672655, 0.138484258, 0.14929019, 0.155005355, 0.163990938, 0.163990938, 0.152120935, 0.142441645, 0.135907271, 0.123724046, 0.112632969, 0.101577635, 0.092471844, 0.087405019, 0.079569713, 0.069765993, 0.062918208, 0.05947072, 0.05313209, 0.048825554, 0.043621529, 0.039711135, 0.035813343, 0.032602904, 0.029680261, 0.026767035, 0.025063878, 0.023469091, 0.021365235, 0.020005789, 0.018384252, 0.016894146, 0.015671312, 0.014401099, 0.013484773, 0.012391787, 0.011603311, 0.010563147, 0.009798565, 0.009004358, 0.008510981, 0.008120548, 0.007532766, 0.007053464, 0.006729893, 0.006481757]
#                 "ts": [0.417218543, 0.625827815, 1.529801325, 2.433774834, 3.059602649, 3.963576159, 5.145695364, 6.258278146, 7.231788079, 8.483443709, 9.804635762, 11.12582781, 12.30794702, 13.76821192, 15.1589404, 16.54966887, 17.8013245, 19.67880795, 21, 22.52980132, 23.9205298, 25.45033113, 27.04966887, 28.50993377, 30.45695364, 31.84768212, 32.54304636, 33.02980132, 33.79470199, 34.4205298, 35.32450331, 36.57615894, 37.75827815, 38.87086093, 39.70529801, 40.81788079, 42.34768212, 43.87748344, 44.99006623, 46.3807947, 47.63245033, 49.23178808, 50.62251656, 52.15231788, 53.47350993, 55.07284768, 56.60264901, 57.92384106, 59.17549669, 60.70529801, 61.88741722, 63.13907285, 64.80794702, 66.1986755, 67.72847682, 68.98013245, 70.44039735, 71.90066225, 73.70860927, 75.2384106, 76.35099338, 77.8807947, 79.06291391, 80.31456954, 81.70529801, 82.81788079, 83.93046358]
#             }
#         ]
# })
# data=json.loads(data)
# time = [i['ts'] for i in data["ts"]]
# gasflow = [i['qs'] for i in data["qs"]]

print (ts)  # in months
print (qs)  # in Sm3/s
# to convert qs to MMSCFD
#qs = [engunits.convert_value(type_curve.calculate_synthetic_type_curve)]
fig = plt.plot(ts, qs, 'b')

ref_series = json.load(open('ref_curve.py'))
qs=ref_series["qs"]
ts=ref_series["ts"]
print(ts)
print(qs)
plt.plot(ts, qs, 'r')

plt.show()

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



