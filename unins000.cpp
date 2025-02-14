#include <iostream>
#include <vector>
#include <string>

int main() {
    system("cls");
    std::vector<std::string> filesToDelete = {
        "app.exe", 
        "icon.png",
        "p_loader.exe",
        "plugins",
        "public",
        "config",
        "logs.txt",
    };

    std::string response;

    std::cout << "Do you really want to delete the following files?" << std::endl;
    for (const auto& file : filesToDelete) {
        std::cout << " - " << file << std::endl;
    }
    
    std::cout << "Type 'yes' to confirm: ";
    std::cin >> response;

    if (response == "yes") {
        std::cout << "Are you absolutely sure? Type 'yes' to continue: ";
        std::cin >> response;

        if (response == "yes") {
            for (const auto& file : filesToDelete) {
                if (remove(file.c_str()) == 0) {
                    std::cout << "File " << file << " is deleted successfully!" << std::endl;
                } else {
                    std::perror(("Error when trying to delete " + file).c_str());
                }
            }
        } else {
            std::cout << "Deletion was canceled." << std::endl;
        }
    } else {
        std::cout << "Skipping deletion." << std::endl;
    }

    return 0;
}