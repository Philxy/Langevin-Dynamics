// normal_distribution
#include <iostream>
#include <string>
#include <random>
#include <fstream>

double kBT = .1;
const double dt = 0.005;
const double sqrtdt = sqrt(dt);
const double tMax = 100;
const int nMax = int(tMax / dt);
const int numParticles = 1000;
const int nrolls = 100000;
const double mean = 0;
const double stdDev = 1;

const double eta = 1.0087;
const double a = 0.1;
const double D_R = kBT/(8*3.141*a*a*a*eta);
const double D_T = kBT/(6*3.141*eta*a);
const double v0 = 10;

class Particle
{
public:
  double x = 0;
  double y = 0;
  double phi = 0;
  double vx = 0;
  double vy = 0;

  std::random_device rd{};

  // std::mt19937 generator{rd()};
  std::default_random_engine generator{rd()};
  std::normal_distribution<double> distribution;

  void update()
  {
    double rndx = sqrt(2 * D_T * dt) * distribution(generator);
    double rndy = sqrt(2 * D_T * dt) * distribution(generator);
    double rndphi = sqrt(2 * D_R * dt) * distribution(generator);

    //double vxp = vx;
    //double vyp = vy;

    // stochastic Euler-method
    x += rndx + v0 * cos(phi)* dt;
    y += rndy + v0 * sin(phi)* dt;
    //x += ((vx + vxp) / 2) * dt;
    //y += ((vy + vyp) / 2) * dt;
    phi += rndphi;
  }
};

int main()
{

  double ensembleMSD[nMax] = {0};

  for (int partCount = 0; partCount < numParticles; partCount++)
  {
    Particle p;

    for (int n = 0; n < nMax; n++)
    {
      // trajectoryFile << n * dt << "," << p.x << "," << p.y << "," << p.vx << "," << p.vy << "," << p.vz << "\n";

      ensembleMSD[n] += (p.x * p.x + p.y * p.y);
      p.update();
    }
  }

  std::ofstream MSDFile("MSDs/" + std::to_string(v0) + ".csv");

  for (int i = 0; i < nMax; i++)
  {
    MSDFile << i * dt << "," << ensembleMSD[i] / (numParticles) << "\n";
  }

  return 0;
}