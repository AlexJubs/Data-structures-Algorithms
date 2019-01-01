#include <iostream>
#include <cmath>
#include "Polynomial.h"

#ifndef MARMOSET_TESTING

int main();

#endif

void init_poly(poly_t &p, double const init_coeffs[], unsigned int const init_degree) {
	//Function to initialize the polynomial
	//Checking if the polynomial has already been initialized

	if(p.a_coeffs != nullptr){
		destroy_poly(p);
	}

	p.a_coeffs = new double[init_degree + 1];
	p.degree = init_degree;

	for (std::size_t k = 0; k <= init_degree; ++k){
		p.a_coeffs[k] = init_coeffs[k];
	}
}

void destroy_poly(poly_t &p){
	//Function to destroy the initialized polynomial

	delete[] p.a_coeffs;
	p.a_coeffs = nullptr;
}

unsigned int poly_degree( poly_t const &p ){

	if (p.a_coeffs == nullptr){
		throw 0;
	}
	else {
		return p.degree;
	}
}

void poly_print(poly_t const &p) {

	std::cout << "The Polynomial is" << std::endl;

	for (size_t k = 0; k <= p.degree; ++k) {
		if (k == 0){
			std::cout << p.a_coeffs[k]<< " ";
		}
		else if (k == 1) {
			std::cout << p.a_coeffs[k] << "x ";			
		}
		else {
			std::cout << p.a_coeffs[k] << "x^" << k << " ";
		}
	}
	std::cout<<std::endl;
}

double poly_coeff(poly_t const &p, unsigned int n){

	if (p.a_coeffs == nullptr){
		throw 0;
	}
	else {
		return p.a_coeffs[n];
	}
}

double poly_val(poly_t const &p, double const x){
	if (p.a_coeffs == nullptr){
		throw 0;
	}
	else {
		double sum{p.a_coeffs[0]};
		for(size_t k = 1; k <= p.degree; k++){
			sum = sum +  p.a_coeffs[k]*pow(x, k);
		}
		return sum;
	}
}

void poly_add(poly_t &p, poly_t const &q) {
	unsigned int array_size{0};

	if ((p.a_coeffs == nullptr)||(q.a_coeffs == nullptr)) {
		throw 0;
	}

	if (p.degree == q.degree) {
		array_size = p.degree + 1;
		std::size_t i{p.degree};
		int k = 1;
			while (p.a_coeffs[i] == -1*q.a_coeffs[i]) {
				array_size = array_size - k;
				i--;
				k++;
			}
		}

	else if (p.degree > q.degree) {
		array_size = p.degree + 1;
	}
	else if (p.degree < q.degree) {
		array_size = q.degree +1;
	}

	double *temp_array = new double[array_size]{};

	for (size_t k = 0; k <= p.degree; k++){
		temp_array[k] = p.a_coeffs[k];
	}

	for(size_t k = 0; k <= q.degree; k++){
		temp_array[k] = temp_array[k] + q.a_coeffs[k];
	}

	destroy_poly(p);

	p.a_coeffs = temp_array;
	p.degree = array_size - 1;
}

void poly_subtract(poly_t &p, poly_t const &q ) {
	unsigned int array_size{0};

	if ((p.a_coeffs == nullptr)||(q.a_coeffs == nullptr)) {
		throw 0;
	}

	if (p.degree == q.degree) {
		array_size = p.degree + 1;
		std::size_t i{p.degree};
		int k = 1;
			while (p.a_coeffs[i] == -1*q.a_coeffs[i]) {
				array_size = array_size - k;
				i--;
				k++;
			}
		}

	else if (p.degree > q.degree) {
		array_size = p.degree + 1;
	}
	else if (p.degree < q.degree) {
		array_size = q.degree +1;
	}

	double *temp_array = new double[array_size]{};

	for (size_t k = 0; k <= p.degree; k++){
		temp_array[k] = p.a_coeffs[k];
	}

	for(size_t k = 0; k <= q.degree; k++){
		temp_array[k] = temp_array[k] - q.a_coeffs[k];
	}

	destroy_poly(p);

	p.a_coeffs = temp_array;
	p.degree = array_size - 1;
}

void poly_multiply(poly_t&p, poly_t const &q ){

	if ((p.a_coeffs == nullptr)||(q.a_coeffs == nullptr)) {
		throw 0;
	}

	unsigned int capacity {(p.degree + q.degree + 1)};
	double *temp_array{new double[capacity]{}};

	if ((p.a_coeffs[0] == 0 && p.degree == 0)||(q.a_coeffs[0] == 0 && q.degree == 0)){
		delete[] p.a_coeffs;
		p = poly_t{new double[1]{}, 0};
		return;
	}

	for (std::size_t i{0}; i <= p.degree; i++) {
		for (std::size_t j{0}; j <= q.degree; j++){
			temp_array[j+i] = temp_array[j+i] + (p.a_coeffs[i])*(q.a_coeffs[j]);
		}
	}

	delete[] p.a_coeffs;
	p.a_coeffs = temp_array;
	p.degree = capacity - 1;
	temp_array = nullptr;
}

double poly_divide(poly_t &p, double r) {
	if (p.a_coeffs == nullptr){
		throw 0;
	}

	if (p.degree == 0){
		p.a_coeffs[0] = 0;
		return p.a_coeffs[0];
	}
	else {
		unsigned int temp_array_size = p.degree;
		double *temp_array = new double[temp_array_size];
		double temp_var = p.a_coeffs[p.degree];
		temp_array[temp_array_size - 1] = temp_var;
		int counter = temp_array_size - 2;
			for (unsigned int i{temp_array_size - 2}; counter >= 0; i--){
				temp_array[i] = r*temp_var + p.a_coeffs[i + 1];
				temp_var = temp_array[i];
				counter--;
			}

		double remain = p.a_coeffs[0] +temp_var*r;
		destroy_poly(p);
		p.a_coeffs = temp_array;
		p.degree = temp_array_size -1;
		temp_array = nullptr;
	

	return remain;
	}
}

void poly_diff(poly_t &p){
	if (p.a_coeffs == nullptr){
		throw 0;
	}

	double *temp_array = new double[p.degree - 1];

    //for loop assigning entries which are 1 appart in index
	for (std::size_t k = 1; k <= p.degree; k++){
		temp_array[k-1] = (k)*p.a_coeffs[k];
		p.a_coeffs[k] = temp_array[k-1];
	}

	p.degree =  p.degree - 1;

}

double poly_approx_int(poly_t const&p , double a, double b, unsigned int n ){
    if(p.a_coeffs == nullptr) {
        throw 0;
    }

    double height = (b-a)/n;
    double area = 0;

    //applying the formula:
    area = area + poly_val(p, (a + 0*height));
    for(int i = 1; i < n; ++i) {
        area = area + 2*(poly_val(p, (a + i*height)));
    }
    area = area + poly_val(p, (a + n*height));

    area = area*(height/2);

    return area;
}

#ifndef MARMOSET_TESTING

int main(){
	
	
	poly_t my_poly = {nullptr, 0};
	poly_t my_other_poly = {nullptr, 0};

	double Polynomial_input1[9]{2,17,1,12,1,122,106,12,3};
	double Polynomial_input2[5]{9,2,2,4,2};

	init_poly(my_poly, Polynomial_input1, 8);
	init_poly(my_other_poly, Polynomial_input2, 4);

	poly_print(my_poly), poly_print(my_other_poly);

	std::cout << "---------------" << std::endl;

	poly_diff(my_other_poly);
	poly_diff(my_poly);
	poly_print(my_poly), poly_print(my_other_poly);
	
	return 0;
}

#endif