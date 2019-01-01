#include <iostream>
#include "Message.h"
#include <string>

#ifndef MARMOSET_TESTING
int main();
#endif

Node::Node(unsigned int id, std::string frag){
	identifier = id;
	fragment = frag;
	p_next = nullptr;
}

std::string Node::get_fragment(){
	return fragment;
}

Node* Node::get_next(){
	return p_next;
}

Message::Message(){
	head = nullptr;
}

Message::~Message()
{
	Node *temp_node = head;
	while(temp_node != nullptr){
		temp_node = head->p_next;
        delete head;
        head = temp_node;
	}
}

void Message::insert( unsigned int id, std::string fragment){
	Node *temp_node1 = head;
	Node *temp_node2 = new Node(id, fragment);

	if (head == nullptr){
		head = temp_node2;
	}

	else if (id < head->identifier){
		temp_node2->p_next = head;
		head = temp_node2;
	}

	else {
		while ((temp_node1->p_next != nullptr)&&(id > temp_node1->p_next->identifier)){
			temp_node1 = temp_node1 -> p_next;
		}
		if (temp_node1->p_next != nullptr){
			temp_node2->p_next = temp_node1->p_next;
			temp_node1->p_next = temp_node2;
		}
		else {
			temp_node1->p_next = temp_node2;
		}
	}
	temp_node1 = nullptr;
}

void Message::print_message(){
	Node *temp_node = head;
	int counter = -1;

	while(temp_node != nullptr){
		for (int i = 0; (temp_node->identifier - counter - 1) > i; i++){
			std::cout << "... ";
		}

		counter = temp_node->identifier;

		if (temp_node->fragment != "EOT"){
			if (temp_node->p_next != nullptr){
        	std::cout << temp_node->fragment << " ";
			}
			else {
				std::cout << temp_node->fragment;
			}
		}

		if (temp_node->p_next == nullptr){
			if(temp_node->fragment == "EOT"){
				break;
			}
			else if(temp_node->fragment == "EOT") {
				std::cout<< "???";
			}
		}

		temp_node = temp_node->p_next;
    }
    std::cout<<std::endl;
}

#ifndef MARMOSET_TESTING
int main(){
  Message message;
	int input = 0;
	std::string a;

	while(true){
		std::cin >> input;

		if (input == -1){
			message.print_message();
		}
		else if (input >= 0){
			std::cin >> a;
			message.insert(input, a); 
		}
		else if (input == -2){
			return 0;
		}
	}
}
#endif