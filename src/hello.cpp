#include "hello.hpp"

#include <iostream>
#include <Eigen/Dense>

void hello() {
  std::cout << "hello world!\n" << Eigen::MatrixXd::Random(3, 3) << "\n";
}
