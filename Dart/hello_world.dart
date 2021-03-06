import 'dart:async';
import 'dart:io';

void main() {
  print("Program Start");

  int a = 0;
  int b = 90;
  try {
    print("try block first line");
    int result = b ~/ a; // error in this line
    print(result);
    print("try block last line");
  } on DeferredLoadException {
    print("Library is not loading yet");
  } on IOException {
    print("Input Output error");
  } on IntegerDivisionByZeroException {
    print("You can't divide by Zero");
  } catch (e) {
    // if any on bloc is not execute then catch block execute
    print(e.toString());
  }
  try {
    String parseThis = "45wer";
    int parseIntNumber = int.parse(parseThis);
    print("Parse Number is : $parseIntNumber");
  } on FormatException {
    print("Only parse numbers in parse method");
  } catch (e) {
    print(e.toString());
  }
  try {
    String parseThis = "37";
    int parseIntNumber = int.parse(parseThis);
    print("Parse Number is : $parseIntNumber");
  } on FormatException {
    print("Only parse numbers in parse method");
  } catch (e) {
    print(e.toString());
  }
  finallyExample();
  throwsExample(3000);
  throwsExample(8000);

  print("Program End");
}

void finallyExample() {
//   Finally
// To ensure that some code runs whether or not an exception is thrown, use a finally clause. If no catch clause matches the exception, the exception is propagated after the finally clause runs

  try {
    // print(34 ~/ 0);
    print(34 ~/ 2);
  } catch (e) {
    print(e);
  } finally {
    print(
        "this is from finaly block , program is execute normaly or throws an exception, finaly block is execute for sure");
  }
}

void throwsExample(int withdraw_balance) {
  int bank_balance = 5000;

  try {
    if (bank_balance >= withdraw_balance)
      print("Money deduct from your bank balance");
    else
      throw "Insufficient balance";
  } catch (e) {
    print(e);
  }
}