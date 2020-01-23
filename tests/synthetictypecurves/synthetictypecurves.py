from .typecurve.synthetictypecurve import SyntheticTypeCurve
import unittest

# https://docs.python.org/3/library/unittest.html

class TestMethods(unittest.TestCase):
    def test_calculate_ramp_to_peak_flow(self):
        # Errors considered: q_zero>q_peak, t_peak==0
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 1, 1)
        # q_zero, q_peak, t_peak, t_plat, k, b, a

        # t = 0, q_zero = 0, k = 0 (full linear ramp), expect ramp_to_peak_flow to return 0
        q = type_curve.calculate_ramp_to_peak_flow()
        self.assertEqual(q, 0)

        # t = 1, q_zero = 0, k = 0 (full linear ramp), expect ramp_to_peak_flow to return linear_ramp_slope
        type_curve.t = 1
        q = type_curve.calculate_ramp_to_peak_flow()
        self.assertEqual(q, type_curve.calculate_linear_ramp_slope)

    def test_calculate_sine_ramp_flow(self):
        # Errors considered: q_zero>q_peak, t_peak==0
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 1, 1)
        
        
        # q_peak = 100, t_peak = 5, t=0, expect sine_ramp_flow to return 0
        type_curve.t = 0
        q = type_curve.calculate_sine_ramp_flow()
        self.assertEqual(q,0)

        # q_peak = 100, t_peak = 5, t=1, expect sine_ramp_flow to return 9.549150281
        type_curve.t = 1
        q = type_curve.calculate_sine_ramp_flow()
        self.assertEqual(q,9.549150281)

    def test_calculate_ramp_flow(self):
        # Errors considered: k>1, k<0
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 1, 1)

        # k = 0 (full linear ramp), expect ramp_flow to return ramp_to_peak_flow
        type_curve.t = 0
        q = type_curve.calculate_ramp_flow()
        self.assertEqual(q, type_curve.calculate_ramp_to_peak_flow)

        # k = 1 (full sinusodal ramp), expect ramp_flow to return sin_ramp_flow
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 1, 1, 1)
        q = type_curve.calculate_ramp_flow()
        self.assertEqual(q, type_curve.calculate_sine_ramp_flow)

    def test_calculate_peak_flow_plateau(self):
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 1, 1)

        # q_peak = 100, expect peak_flow_plateau to return 100
        q_type_curve.calculate_peak_flow_plateau()
        self.assertEqual(q, 100)

    def test_calculate_decline_flow(self):
        # Errors considered: t_plat < 0, t_peak < 0, a<0, b>1, b<0, math.pow((1 + (self.b * self.a * (self.t - self.t_peak - self.t_plat))) , (1/self.b)) == 0, (t - t_peak - t_plat) < 0
        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 1, 1)

        # q_peak = 100, b = 1, a = 1, t = 20, t_peak = 5, t_plat = 6, expect decline flow to return 10
        type_curve.t = 20
        q_type_curve.calculate_decline_flow()
        self.assertEqual(q, 10)

        type_curve = SyntheticTypeCurve(0, 100, 5, 6, 0, 0, 1)

        # q_peak = 100, b = 0, a = 1, t = 20, t_peak = 5, t_plat = 6, expect decline flow to return 0.01234098041
        q_type_curve.calculate_decline_flow()
        self.assertEqual(q, 0.01234098041)

        

        



