#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

    std::ifstream in("plugins/loader.cfg"); // открываем файл для чтения
    if (in.is_open()) {
        std::string plugin;
        while (std::getline(in, plugin)) {
            std::string command = "plugins\\" + plugin;
            std::cout << "Running plugin: " << command << std::endl;
            if (system(command.c_str()) != 0) {
                std::cerr << "Error running plugin: " << command << std::endl;
            }
        }
        in.close(); // закрываем файл
    } else {
        std::cerr << "Error opening file" << std::endl;
    }
    
    return 0;
}