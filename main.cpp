// normal_distribution
#include <iostream>
#include <string>
#include <random>
#include <fstream>

const double kBT = 5;
const double friction = 0.1;
const double m = 3;
const double dt = 0.01;
const double sqrtdt = sqrt(dt);
const double tMax = 1000;
const int nMax = int(tMax / dt);
const int numParticles = 1000;
const int nrolls = 100000;
const double mean = 0;
const double stdDev = sqrt(2 * kBT * friction); 

class Particle
{
public:
  double x = 0, y = 0;
  double vx = 0, vy = 0;

  std::random_device rd{};
  // std::mt19937 generator{rd()};
  std::default_random_engine generator{rd()};
  std::normal_distribution<double> distribution;

  void update()
  {
    double rndx =  distribution(generator);
    double rndy = distribution(generator);

    vx += (-friction * vx * dt + sqrtdt * rndx) / m;
    vy += (-friction * vy * dt + sqrtdt * rndy) / m;
    x += vx * dt;
    y += vy * dt;
  }
};

int main()
{

  double ensembleMSD[nMax] = {0};

  for (int partCount = 0; partCount < numParticles; partCount++)
  {
    Particle p;

    // std::ofstream trajectoryFile("trajectories/trajectory" + std::to_string(partCount) + ".csv");
    // std::ofstream MSDFile("MSD/MSD" + std::to_string(partCount) + ".csv");

    for (int n = 0; n < nMax; n++)
    {
      // trajectoryFile << p.x << "," << p.y << "," << p.vx << "," << p.vy << "\n";
      ensembleMSD[n] += (p.x * p.x + p.y * p.y);
      p.update();
    }
  }

  std::ofstream MSDFile("MSD.csv");

  for (int i = 0; i < nMax; i++)
  {
    MSDFile << i * dt << "," << ensembleMSD[i] / numParticles << "\n";
  }

  std::random_device rd{};
  // std::mt19937 generator{rd()};
  std::default_random_engine generator{rd()};
  std::normal_distribution<double> distribution(mean, stdDev);

  std::ofstream randomNumbersFile("randomNumbers.csv");
  // randomNumbersFile << "# " << mean << "," << stdDev << "\n";

  for (int i = 0; i < nrolls; i++)
  {
    double randomNumber = distribution(generator);
    randomNumbersFile << randomNumber << "\n";
  }

  // random force correlation function
  double rndNums[100000] = {0};
  double sum = 0;
  for (int i = 0; i < 100000; i++)
  {
    double rnd = sqrt(2 * kBT * friction) * distribution(generator);
    sum += rnd * rnd;
  }
  std::cout << sum / 100000 << " " << 2 * kBT * friction << std::endl;

  return 0;
}