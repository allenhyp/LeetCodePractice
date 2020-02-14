class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_hand = minutes * 6
        h_hand = hour * 30 + minutes * 0.5
        angle = abs(h_hand - m_hand)
        return angle if angle <= 180 else 360 - angle
