// normal_distribution
#include <iostream>
#include <string>
#include <random>
#include <fstream>

double kBT = 1;
const double friction = 1000;
const double k = 1;
const double dt = 0.01;
const double sqrtdt = sqrt(dt);
const double tMax = 100;
const int nMax = int(tMax / dt);
const int numParticles = 100;
const int nrolls = 100000;
const double mean = 0;
const double stdDev = 1;
const double v0x = sqrt(0);
const double v0y = sqrt(0);
const double v0z = sqrt(0);

const double sizeX = 2;
const double sizeY = 2;

class Particle
{
public:
  double x = 0;
  double y = 0;
  double z = 0;

  double vx = v0x;
  double vy = v0y;
  double vz = v0z;

  std::random_device rd{};

  // std::mt19937 generator{rd()};
  std::default_random_engine generator{rd()};
  std::normal_distribution<double> distribution;

  void fixOutOfBounds()
  {
    if (fabs(x) > sizeX)
    {
      if (x > sizeX)
      {
        x -= sizeX * 2;
      }
      else
      {
        x += sizeX * 2;
      }
    }
    if (fabs(y) > sizeY)
    {
      if (y > sizeY)
      {
        y -= sizeY * 2;
      }
      else
      {
        y += sizeY * 2;
      }
    }
  }

  void update()
  {
    double rndx = sqrt(2 * kBT * friction * dt) * distribution(generator);
    double rndy = sqrt(2 * kBT * friction * dt) * distribution(generator);
    // double rndz = sqrt(2 * kBT * friction * dt) * distribution(generator) ;

    double vxp = vx;
    double vyp = vy;
    // double vzp = vz;

    // verlet method
    double b = 1 / (1 + (friction * dt / (2 * m)));
    double a = (1 - (friction * dt / (2 * m))) * b;

    // harmomic potential
    // double fx = -k * x;
    // double fy = -k * y;

    // escape potential
    // double x_max = 1;
    // double y_max = 1;
    // double z_max = 1;
    // double fx = -k * x * (3 * x_max - 3 * x) / (3 * x_max);
    // double fy = -k * y * (3 * y_max - 3 * y) / (3 * y_max);
    // double fz = -k * z * (3 * z_max - 3 * z) / (3 * z_max);
    // fx = 0;
    // fy = 0;
    // fz = 0;

    // periodic potential
    double A = .5;
    double omega = 2 * 3.1415926;
    double fx = -A * omega * cos(omega * x);
    double fy = -A * omega * cos(omega * y);
    // double fz = A*sin(z);

    x += b * dt * vx + b * dt * dt / (2 * m) * fx + b * dt / (2 * m) * rndx;
    y += b * dt * vy + b * dt * dt / (2 * m) * fy + b * dt / (2 * m) * rndy;
    // z += b * dt * vz + b * dt * dt / (2 * m) * fz + b * dt / (2 * m) * rndz;

    // harmomic potential
    // double fxn = -k * x;
    // double fyn = -k * y;

    // escape potential
    // double fxn = -k * x * (3 * x_max - 3 * x) / (3 * x_max);
    // double fyn = -k * y * (3 * y_max - 3 * y) / (3 * y_max);
    // double fzn = -k * z * (3 * z_max - 3 * z) / (3 * z_max);
    // fxn = 0;
    // fyn = 0;
    // fzn = 0;

    // periodic potential
    double fxn = -A * omega * cos(omega * x);
    double fyn = -A * omega * cos(omega * y);

    vx = a * vx + dt / (2 * m) * (a * fx + fxn) + b / m * rndx;
    vy = a * vy + dt / (2 * m) * (a * fy + fyn) + b / m * rndy;
    // vz = a * vz + dt / (2 * m) * (a * fz + fzn) + b / m * rndz;

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
  for(double T = 0.2; T < 0.3 ; T *= 10){
  for (int partCount = 0; partCount < numParticles; partCount++)
  {
    kBT = T;
    Particle p;

    //std::ofstream trajectoryFile("trajectories/" + std::to_string(partCount)  +  ".csv");
    //std::ofstream escapeTrajFile("EscapeTrajectories/" + std::to_string(partCount) + "_" + std::to_string(kBT) +  ".csv");

    //  std::ofstream MSDFile("MSD/MSD" + std::to_string(partCount) + ".csv");
    // std::ofstream MSDsFile("MSDs/MSD" + std::to_string(partCount) + ".csv");

    for (int n = 0; n < nMax; n++)
    {
      //trajectoryFile << n * dt << "," << p.x << "," << p.y << "," << p.vx << "," << p.vy << "," << p.vz << "\n";

      /*
      if(p.x > 1.1)
      {
        escapeTrajFile << n * dt << "," << p.x << "," << p.y << "\n";
        break;
      }
      */

      // MSDsFile << n*dt << "," << p.x * p.x + p.y * p.y << "\n";
      // ensembleMSD[n] += (p.vx) * (p.vx ) + (p.vy) * (p.vy );
      // ensembleMSD[n] += (p.vx) +  (p.vy ) ;
      p.update();
      //p.fixOutOfBounds();
      ensembleMSD[n] += (p.x * p.x + p.y * p.y);
    }

  }
  std::ofstream MSDFile("MSDs/" + std::to_string(kBT) + ".csv");

  for (int i = 0; i < nMax; i++)
  {
    MSDFile << i * dt << "," << ensembleMSD[i] / (numParticles) << "\n";
  }
}
  /*
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

  */

  return 0;
}