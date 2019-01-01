#include <iostream>
#include <string>
#include <cmath>

int main();
void interval_calculator();

void interval_calculator(){

	bool run = true;

	bool interval_initialization = false;
	bool array_initialization = false;
	double a;
	double b;
	double memory[2]{};

//This loop will run as long as the command prompt is active
	while (run == true){
		std::string input;
		std::cout<<"input :> ";
		std::cin>>input; 

		//Each IF(input) statement in the loop represents a command

		if (input=="exit"){
			std::cout<<"Bye bye: Terminating interval calculator program. ";
			run = false;
		}

		else if (input=="enter"){
			double a_temp; double b_temp;
			std::cin >> a_temp >> b_temp;

			if (a_temp > b_temp){
				std::cout<<"Error: invalid interval as "<< a_temp <<" > "<< b_temp <<std::endl;
			}
			
			else if (a_temp <= b_temp){
				a = a_temp;
				b = b_temp;
				interval_initialization = true;
			}
			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}

			if ((interval_initialization == true)||(a_temp <= b_temp)){
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="negate"){
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				double temp = a;
				a = -1*b;
				b = -1*temp;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="invert"){
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				//Checking if the interval contains a 0
				if (((a == 0)||(b==0))||((a < 0) && (b > 0))) {
					std::cout<<"Error: division by zero"<<std::endl;
					std::cout<<"--"<<std::endl;
				}
				else {
					double temp = a;
					a = 1/b;
					b = 1/temp;
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}
			}	
		}

		else if (input=="ms"){
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				memory[0] = a;
				memory[1] = b;
				array_initialization = true;

				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="mr"){
			if (array_initialization == false) {
				if (interval_initialization == false){
					std::cout<<"--"<<std::endl;
				}

				else if (interval_initialization == true){
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}
			}

			else if (array_initialization == true){
				a = memory[0];
				b = memory[1];
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}

		}

		else if (input=="mc"){
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {

				if (array_initialization == true){
					
					array_initialization = false;

					std::cout<<"["<<memory[0]<<", "<<memory[1]<<"]"<<std::endl;
				}
			}
		}

		else if (input=="m+") {
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				memory[0] = memory[0] + a;
				memory[1] = memory[1] + b;

				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}			
		}

		else if (input=="m-") {
			if ((interval_initialization == false)||(array_initialization == false)) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				memory[0] = memory[0] - b;
				memory[1] = memory[1] - a;

				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}			
		}

		else if (input=="scalar_add") {
		double scalar;
		std::cin >> scalar;

			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				a = a+scalar;
				b = b+scalar;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}			
		}

		else if (input=="scalar_subtract") {
		double scalar;
		std::cin >> scalar;

			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}

			else if (interval_initialization == true) {
				a = a-scalar;
				b = b-scalar;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}			
		}

		else if (input=="scalar_multiply") {
		double scalar;
			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				std::cin >> scalar;
				a = a*scalar;
				b = b*scalar;

				if (scalar >= 0) {
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}
				else if (scalar < 0){
					double temp = a;
					a = b;
					b = temp;
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}
			}			
		}

		else if (input=="scalar_divide") {
		double scalar;
		std::cin >> scalar;				

			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}

			else if (interval_initialization == true) {
				if (scalar == 0) {
					std::cout << "Error: division by zero"<<std::endl;
					std::cout<<"--"<<std::endl;
					interval_initialization = false;
				}

				if (scalar > 0) {
					a = a/scalar;
					b = b/scalar;
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}

				else if (a > b){
					double temp = a;
					a = b/scalar;
					b = temp/scalar;
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}
			}
		}

		else if (input=="scalar_divided_by") {
		double scalar;
		std::cin >> scalar;

			if (interval_initialization == false) {
				std::cout<<"--"<<std::endl;
			}
			else if (interval_initialization == true) {
				if (((a == 0)||(b == 0))||((a < 0) && (b > 0))) {
					std::cout << "Error: division by zero" << std::endl;
					std::cout<<"--"<<std::endl;
				}

				else {
					a = scalar*(1/a);
					b = scalar*(1/b);

					if (scalar <= 0) {
						std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
					}
					else if (scalar > 0){
						double temp = a;
						a = b;
						b = temp;
						std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
					}
				}
			}
		}

		else if (input=="interval_add"){
			double a_add; double b_add;
			bool endIF {true};

			std::cin >> a_add >> b_add;
			if (a_add > b_add){
				std::cout<<"Error: invalid interval as "<< a_add <<" > "<< b_add <<std::endl;
			}
			if ((a_add <= b_add)&&(interval_initialization == true)){
				a = a+a_add;
				b = b+b_add;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				endIF = false;
			}
			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
			else if (endIF == true) {
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="interval_subtract"){
			double c; double d;
			bool endIF {true};

			std::cin >> c >> d;
			if (c > d){
				std::cout<<"Error: invalid interval as "<< c <<" > "<< d <<std::endl;
			}
			if ((c <= d)&&(interval_initialization == true)){
				a = a-d;
				b = b-c;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				endIF = false;
			}
			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
			else if (endIF == true) {
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		//The command for interval multiply is a little long 
		else if (input=="interval_multiply"){
			double c; double d;
			bool endIF {true};

			std::cin >> c >> d;
			if (c > d){
				std::cout<<"Error: invalid interval as "<< c <<" > "<< d <<std::endl;
			}

			if ((c <= d)&&(interval_initialization == true)){

				//Algorithm to find the minimum of an array of values, which will determine a and b
				int counter = 0;
				double min = a*c;
				double numbers[4]={a*c, a*d, b*c, b*d};
				while (counter < 4){
					if (numbers[counter] < min){
						min = numbers[counter];
					}
					counter++;
				}

				//Algorithm to find the maximum of an array of values, which will determine a and b
				counter = 0;
				int max = a*c;
				while (counter < 4){
					if (numbers[counter] > max){
						max = numbers[counter];
					}
					counter++;
				}

				a = min;
				b = max;

				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				endIF = false;
			}

			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
			else if (endIF == true) {
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}


		else if (input=="interval_divide"){
			double c; double d;
			bool endIF {true};

			std::cin >> c >> d;
			if (c > d){
				std::cout<<"Error: invalid interval as "<< c <<" > "<< d <<std::endl;
			}

			//Checking if the interval contains 0
			if (((c == 0)||(d==0))||((c < 0) && (d > 0))) {
				std::cout<<"Error: division by zero"<<std::endl;
				std::cout<<"--"<<std::endl;
				endIF = false;
			}

			if ((c <= d)&&(interval_initialization == true)&&(endIF==true)){

				//Algorithm to find the minimum of an array of values, which will determine a and b
				int counter = 0;
				double min = a/c;
				double numbers[4]={a/c, a/d, b/c, b/d};
				while (counter < 4){
					if (numbers[counter] < min){
						min = numbers[counter];
					}
					counter++;
				}

				//Algorithm to find the maximum of an array of values, which will determine a and b
				counter = 0;
				double max = a/c;

				while (counter != 4){
					if (numbers[counter] > max){
						max = numbers[counter];
					}
					counter++;
				}

				a = min;
				b = max*1.0;

				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				endIF = false;
			}

			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
			else if (endIF == true) {
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="intersect"){
			double c; double d;
			bool endIF {false};
			bool intersect{false};
			std::cin >> c >> d;

			if (c > d){
				std::cout<<"Error: invalid interval as "<< c <<" > "<< d <<std::endl;
				interval_initialization = false;
			}

			else if ((c <= d)&&(interval_initialization == true)) {

				//Finding if interval c d intercets interval a b
				if ((c > a)&&(c < b)){
					a = c;
					intersect = true;
				}
				if (d < b){
					b = d;
					intersect = true;
				}
				//The interval is only printed if it is changed
				if ((intersect == true)||((c < a)&&(d > b))){
					std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
				}

				//Case of which out of range
				if ((c > b)||(d < a)){
					interval_initialization = false;
				}
			}

			if ((endIF == true)&&(interval_initialization == true)) {
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}

			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
		}

		else if (input=="integers"){

			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}

			if (interval_initialization == true) {
				int p;
				p = ceil(a);

				//algorithm for sorting all the integers that lie between the interval into an array and printing it
				while(p != ceil(b)){
					std::cout << p;
					p++;
					if (p == ceil(b)){
						std::cout<<std::endl;
					}
					else if(p!= ceil(b)){
						std::cout<<", ";
					}
				}
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else if (input=="cartesian_integers"){

			double c; double d;
			std::cin >> c >> d;

			double d2 = d;

			if (c > d2){
				std::cout<<"Error: invalid interval as "<< c <<" > "<< d <<std::endl;
				interval_initialization = false;
			}

			if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}

			else if(interval_initialization == true){
				for (int i = ceil(a); i <= floor(b); ++i){
					for (int j = ceil(c); j <= floor(d2); ++j){
						std::cout<<"("<<i<<","<<j<<")";
						if(!((i==b)&&(j==floor(d2)))){
							std::cout<<", ";
						}
					}
				}
				std::cout<<std::endl;
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
		}

		else {
			std::cout<<"Error: illegal command"<<std::endl;

			if (interval_initialization == true){
				std::cout<<"["<<a<<", "<<b<<"]"<<std::endl;
			}
			else if (interval_initialization == false){
				std::cout<<"--"<<std::endl;
			}
		}
	}
}

int main(){
	interval_calculator();
	return 0;
}