#include <iostream>
#include <deque>
#include <vector>
#include <string>
#include <algorithm>
#include <tuple>
#include <cctype> // for std::isdigit

//using namespace boost::algorithm;

using namespace std;


string least_interval(const vector<string>& tasks) {
    //deque<tuple<char, int, int, int>> task_queue; // (task, count, cooldown, cooldown_timer)
    string result;
    // Parse the tasks and their respective cooling periods
    deque < tuple< char, string, int, int, int> > task_queue;

    for (const auto& task : tasks) {
        std::string task_letter;
    // Extracting letters from the task (assuming tasks are in the format "LetterNumber")
        for (char ch : task) {
            if (!std::isdigit(ch)) {
                task_letter.push_back(ch);
            } else {
                break; // Stop at the first digit
            }
        }
        // Extracting letters from the task (assuming tasks are in the format "LetterNumber")
        //task_letter = trim_right_copy_if(task, is_any_of("0123456789"))
        int count = task_letter.length();
        // Extracting cooldown period from the task
        std::string cooldown_str = task.substr(task_letter.length());
        int cooldown = std::stoi(cooldown_str); // Convert cooldown period to integer
        char t = task_letter[0];

        // Append task details to the queue
        task_queue.emplace_back(t, task_letter, count, cooldown, 0); // (task, count, cooldown, cooldown_timer)
        //cout<<"task_queue"<< task_queue << endl;
        //cout<<"task_letter: "<< task_letter << endl;
        //cout<<"count: "<< count << endl;
        //cout<<"cooldown: "<< cooldown  << endl;
        //cout<<"t: "<< t  << endl;
    }


    while (!task_queue.empty()) {
        bool executed = false;
        for (int i = 0; i < task_queue.size(); ++i) {
            auto& [t, task, count, cooldown, cooldown_timer] = task_queue[i];

            if (cooldown_timer == 0) {
                result.append(string(min(count, cooldown), t));
                count -= cooldown;
                cooldown_timer = cooldown; // Reset the cooldown timer after execution

                if (count > 0) {
                    task_queue[i] = make_tuple(t, task, count, cooldown, cooldown_timer);
                } 
                else {

                    auto& [t, task, count, cooldown, cooldown_timer] = task_queue[i];
                    cout << "removing"<< t<< task<<count<< cooldown<<cooldown_timer<< endl;

                    task_queue.erase(task_queue.begin() + i);
                   //auto& [t, task, count, cooldown, cooldown_timer] = task_queue[i];
                   // cout << "removed" <<t<< task<<count<< cooldown<<cooldown_timer<< endl;
                    break; // Break since we've executed a task
                }
                //executed = true;
                // Decrement the cooldown timer of all tasks
                for (int j = 0; j < task_queue.size(); ++j) {
                    if (j != i) {
                        auto& [t_j, task_j, count_j, cooldown_j, cooldown_timer_j] = task_queue[j];
                        if (cooldown_timer_j > 0) {
                            //cooldown_timer_j = max(cooldown_timer_j - 1, 0);
                            cooldown_timer_j = 0 ;
                            task_queue[j] = make_tuple(t_j, task_j, count_j, cooldown_j, cooldown_timer_j);
                        }
                    }
                } 
            }
            executed = true;
        }

        if (!executed) {
            // If no task was executed, we need to idle
            result.push_back('-');

            // Decrement the cooldown timer of all tasks
            for (int j = 0; j < task_queue.size(); ++j){
                auto& [t_j, task_j, count_j, cooldown_j, cooldown_timer_j] = task_queue[j] ;
                if (cooldown_timer_j > 0) {
                    cooldown_timer_j = max(cooldown_timer_j - 1, 0);
                    task_queue[j] = make_tuple(t_j, task_j, count_j, cooldown_j, 0);

                }
            }
        }
    }

    return result;
}




int main() {
    // Example usage
    vector<string> tasks = {"BB1", "CCC2"};
    cout << least_interval(tasks) << endl;
    return 0;
}