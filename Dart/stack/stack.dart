// Fixed length stack implementation

class Stack {
  List<int> _stackData;
  int _top;
  int _size;

  Stack(int size) {
    this._size = size;
    this._stackData = List<int>(_size); // fixed length List or array
    this._top = -1; // initialize top as -1
  }
  bool _isEmpty() {
    return _top == -1;
  }

  bool _isFull() {
    return _top == _size - 1;
  }

  // get stack current length
  int get stackLength => this._top + 1; // getter
  int peek() {
    // this method returns top element of the stack if stack is not empty
    if (_isEmpty()) {
      print("Stack is empty");
      return -1;
    }
    return _stackData[_top];
  }

  void push(int data) {
    if (_isFull()) {
      print("Stack is overflow");
      return;
    }
    _top++;
    _stackData[_top] = data;
    // _stackData.insert(_top, data); Error :  Cannot add to a fixed-length list
  }

  void pop() {
    if (_isEmpty()) {
      print("Stack is empty");
      return;
    }
    print("Poped element is : ${_stackData[_top]}");
    _top--;
    // _stackData.removeAt(_top--); Error : Cannot remove from a fixed-length list
  }

  void display() {
    if (_isEmpty()) {
      print("Stack is empty");
      return;
    }
    print("****Stack elements : ");
    for (var i = _top; i >= 0; i--) {
      print(_stackData[i]);
    }
  }
}
