class ParkingSystem {
private:
    int type [3];
public:
    ParkingSystem(int big, int medium, int small) {
        this->type[0] = big;
        this->type[1] = medium;
        this->type[2] = small;
    }
    
    bool addCar(int carType) {
        return this->type[carType - 1]-- > 0;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
 