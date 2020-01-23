import math

class SyntheticTypeCurve ():

    """
        Implementing synth as per "Developing synthetic reservoir type curve model for use in evaluating surface facility and gathering pipe network designs" 
    """

    def __init__(self, q_zero, q_peak, t_peak, t_plat, k, b, a):
        # Time (t) - measured in months (m)
        self.t = 0 
        self.t_plat = max(t_plat, 0)

        # Standard Volume Flow (q) - measured in Standard meters cubes per second (Sm^3/s)
        self.q_zero = min(q_zero, q_peak)
        self.q_peak = q_peak
        self.t_peak = max(t_peak, 0)
        

        # Interpolation degree between linear and sinusoidal ramp to peak (k)
        self.k = k
        if self.k>1:
            self.k=1
        else:
            if self.k<0:
                self.k=0

        # Flow decline exponent (b)
        self.b = b
        if self.b>1:
            self.b=1
        else:
            if self.b<0:
                self.b=0

        # Flow decline constant (a) - a=ln(q_zero/q)/t
        self.a = max(a, 0) 
        

    def build_curve(self):
        pass

    def calculate_ramp_to_peak_flow(self):
        # Equation 2
        # returns the q_flow at time self.f
        return (self.calculate_linear_ramp_slope() * self.t) + self.q_zero 

    def calculate_linear_ramp_slope(self):
        # Equation 3
        try:     
            return (self.q_peak - self.q_zero) / self.t_peak
        except Exception as err:
            return 0

    def calculate_sine_ramp_flow(self):
        # Equation 4
        try:
            return (self.q_peak / 2) * math.sin((math.pi / self.t_peak) * self.t - (math.pi / 2)) + (self.q_peak / 2)
        except Exception as err:
            return 0

    def calculate_ramp_flow(self):
        # Equation 5
        return (self.k * self.calculate_sine_ramp_flow()) + ((1 - self.k) * self.calculate_ramp_to_peak_flow()) 
    
    def calculate_peak_flow_plateau(self): 
        # Equation 6
        return (self.q_peak)
    
    def calculate_decline_flow(self):
        if self.b == 0:
            # Equation 8
            return self.q_peak * math.exp((-1 * (self.a)) * (self.t - self.t_peak - self.t_plat))
        else:
            # Equation 7
            return self.q_peak / math.pow((1 + (self.b * self.a * (self.t - self.t_peak - self.t_plat))) , (1/self.b))
                          
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

