class SyntheticTypeCurve ():
    import math

    """
        Implementing synth as per "Developing synthetic reservoir type curve model for use in evaluating surface facility and gathering pipe network designs" 
    """

    def __init__(self, t, q_zero, q_peak, t_peak, k, b, a, t_plat):
        self.t = t
        self.q_zero = q_zero
        self.q_peak = q_peak
        self.t_peak = t_peak
        self.k = k
        self.b = b
        self.a = a 
        self.t_plat = t_plat

    def build_curve(self):
        pass

    def calculate_ramp_to_peak_flow(self):
        # Equation 2
        return (self.calculate_linear_ramp_slope * self.t) + self.q_zero 

    def calculate_linear_ramp_slope(self):
        # Equation 3
        return (self.q_peak - self.q_zero) / self.t_peak

    def calculate_sine_ramp_flow(self):
        # Equation 4
        return ((self.q_peak / 2) * math.sin((math.pi / self.t_peak) * self.t - (math.pi / 2))) + (self.q_peak / 2)

    def calculate_ramp_flow(self):
        # Equation 5
        return (self.k * self.calculate_sine_ramp_flow) + ((1 - self.k) * self.calculate_ramp_to_peak_flow) 
    
    def calculate_peak_flow_plateau(self).
        # Equation 6
        return (self.q_peak)
    
    def calculate_decline_flow(self):
        if b != 0:
            # Equation 7
            return self.q_peak / math.pow((1 + (self.b * self.a * (self.t - self.t_peak - self.t_plat))) , (1/self.b))
        else:
            # Equation 8
            return self.q_peak * math.exp(-1 * (self.a) * (self.t - self.t_peak - self.t_plat))    

    def calculate_synthetic_type_curve(self):
        # Equation 9
        if self.t == 0:
            return self.q_zero
        else:
            if self.t > 0 and self.t <= self.t_peak:
                return self.calculate_ramp_flow
            else:
                if self.t > self.t_peak and self.t <= (self.t_peak + self.t_plat):
                    return self.calculate_peak_flow_plateau
                else:
                    if self.t > (self.t_peak + self.t_plat):
                        return calculate_decline_flow

    def get_flow(self, interval):
        pass


    def get_backpressure(self, interval, flow):
        pass

