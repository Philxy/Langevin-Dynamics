// normal_distribution
#include <iostream>
#include <string>
#include <random>
#include <fstream>

const double kBT = 1;
const double friction = 1;
const double m = 1;
const double k = 0;
const double dt = 0.001;
const double sqrtdt = sqrt(dt);
const double tMax = 10;
const int nMax = int(tMax / dt);
const int numParticles = 5000;
const int nrolls = 100000;
const double mean = 0;
const double stdDev = 1;
const double v0x = sqrt(1);
const double v0y = sqrt(1);

class Particle
{
public:
  double x = 1;
  double y = 1;
  double vx = v0x;
  double vy = v0y;

  std::random_device rd{};

  // std::mt19937 generator{rd()};
  std::default_random_engine generator{rd()};
  std::normal_distribution<double> distribution;

  void update()
  {
    double rndx = sqrt(2 * kBT * friction * dt) * distribution(generator) ;
    double rndy = sqrt(2 * kBT * friction * dt) * distribution(generator) ;

    double vxp = vx;
    double vyp = vy;

    // verlet method
    double b = 1 / (1 + (friction * dt / (2 * m)));
    double a = (1 - (friction * dt / (2 * m))) * b;
    double fx = -k * x;
    double fy = -k * y;

    x += b * dt * vx + b * dt * dt / (2 * m) * fx + b * dt / (2 * m) * rndx;
    y += b * dt * vy + b * dt * dt / (2 * m) * fy + b * dt / (2 * m) * rndy;

    double fxn = -k * x;
    double fyn = -k * y;

    vx = a * vx + dt / (2 * m) * (a * fx + fxn) + b / m * rndx;
    vy = a * vy + dt / (2 * m) * (a * fy + fyn) + b / m * rndy;

    // stochastic Euler-method
    // vx += (-friction * vx * dt - k * x * dt + sqrtdt * rndx) / m;
    // vy += (-friction * vy * dt - k * y * dt + sqrtdt * rndy) / m;
    // x += ((vx + vxp) / 2) * dt;
    // y += ((vy + vyp) / 2) * dt;
  }
};

int main()
{

  double ensembleMSD[nMax] = {0};
  for (int partCount = 0; partCount < numParticles; partCount++)
  {
    Particle p;

    // std::ofstream trajectoryFile("HarmonicTraj/" + std::to_string(partCount)  +  ".csv");

    //  std::ofstream MSDFile("MSD/MSD" + std::to_string(partCount) + ".csv");
    // std::ofstream MSDsFile("MSDs/MSD" + std::to_string(partCount) + ".csv");

    for (int n = 0; n < nMax; n++)
    {
      // trajectoryFile << n * dt << "," << p.x << "," << p.y << "," << p.vx << "," << p.vy << "\n";

      // MSDsFile << n*dt << "," << p.x * p.x + p.y * p.y << "\n";
      //ensembleMSD[n] += (p.vx) * (p.vx ) + (p.vy) * (p.vy );
      ensembleMSD[n] += (p.vx) +  (p.vy ) ;
      //ensembleMSD[n] += (p.x * p.x + p.y * p.y);
      p.update();
    }
  }

  std::ofstream MSDFile("MSD.csv");

  for (int i = 0; i < nMax; i++)
  {
    MSDFile << i * dt * 10 << "," << ensembleMSD[i] / (numParticles * 2) << "\n";
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

  return 0;

  // random force correlation function
  int numOfRands = 10000;
  double rndNums[numOfRands] = {0};
  double sum = 0;
  for (int i = 0; i < numOfRands; i++)
  {
    double rnd = sqrt(2*kBT * friction)  * distribution(generator);
    rndNums[i] = rnd;
  }

  int num_correlations = 1000;
  double correlations[num_correlations] = {0};

  int norm_count[num_correlations] = {0};

  for (int rnd_index = 0; rnd_index < numOfRands; rnd_index++)
  {
    for (int dt = 0; dt < num_correlations && rnd_index + dt < numOfRands; dt++)
    {
      correlations[dt] += rndNums[rnd_index] * rndNums[rnd_index + dt];
      norm_count[dt]++;
    }
  }

  std::ofstream correlogram("correlogram.csv");

  for(int i = 0; i < num_correlations; i++)
  {
    correlations[i] /= (numOfRands-i);
    correlogram << i << "," << correlations[i] << "\n";
  }


  return 0;
}