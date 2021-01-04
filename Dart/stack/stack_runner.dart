import 'stack.dart';
import 'dart:io'; // for user input

void main() {
  int size;
  print("Enter stack size : ");
  size = int.parse(stdin.readLineSync());
  Stack stack = Stack(size);

  while (true) {
    switch (showMenu()) {
      case 1: // push
        int data;
        print("Enter data to add : ");
        data = int.parse(stdin.readLineSync());
        stack.push(data);

        break;
      case 2: // pop
        stack.pop();
        break;
      case 3: // peek
        print("Peek : ${stack.peek()}");
        break;
      case 4: // display
        stack.display();
        break;
      case 5: // current length of the stack
        print("Current length of stack : ${stack.stackLength}");
        break;
      case 6: // exit from the program
        exit(0);
        break;
      default:
        print("Wrong Choice");
    }
  }
}

int showMenu() {
  int choice;
  print("1. Push");
  print("2. Pop");
  print("3. Peek");
  print("4. Display");
  print("5. Current Length of stack");
  print("6. EXIT");
  print("Enter your choice : ");

  choice = int.parse(stdin.readLineSync());
  return choice;
}
