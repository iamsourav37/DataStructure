import 'dart:io';

import 'stack.dart';

void main() {
  Stack stack = Stack();
  dynamic data;

  while (true) {
    switch (showMenu()) {
      case 1:
        print("Enter any data : ");
        data = stdin.readLineSync();
        stack.push(data);
        break;
      case 2:
        print("Poped element : ${stack.pop()}");
        break;
      case 3:
        print("Peek : ${stack.peek()}");
        break;
      case 4:
        stack.display();
        break;
      case 5:
        print("Length of the stack : ${stack.currentSize}");
        break;
      case 6:
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
