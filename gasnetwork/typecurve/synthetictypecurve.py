class SyntheticTypeCurve ():

    """
        Implementing synth as per "Developing synthetic reservoir type curve model for use in evaluating surface facility and gathering pipe network designs" 

    """

    def __init__(self, q_zero, q_peak, t_peak):
        self.q_zero = q_zero
        self.q_peak = q_peak
        self.t_peak = t_peak

    def build_curve(self):
        pass

    def calculate_linear_ramp_slope(self):
        # Equation 3
        return (self.q_peak - self.q_zero) / self.t_peak

    def get_flow(self, interval):
        pass


    def get_backpressure(self, interval, flow):
        pass

