class Solution {
private:
    // c++11 random floating point number generation
    mt19937 gen{random_device{}()};
    uniform_real_distribution<double> dis{0, 1};
    double radius, x_center, y_center;
public:
    Solution(double radius, double x_center, double y_center) {
        this->radius = radius;
        this->x_center = x_center;
        this->y_center = y_center;
    }
    
    vector<double> randPoint() {
        double d = sqrt(dis(gen)) * radius;
        double theta = dis(gen) * 2 * M_PI;
        return {d * cos(theta) + x_center, d * sin(theta) + y_center};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj.randPoint();
 */
