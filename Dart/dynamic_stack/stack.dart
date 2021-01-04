class Stack {
  List<dynamic> _data;
  int _top;

  Stack() {
    _data = [];
    _top = -1;
  }
  bool _isEmpty() {
    if (this._top == -1)
      return true;
    else
      return false;
  }

  void push(dynamic data) {
    this._top++;
    this._data.add(data);
  }

  dynamic pop() {
    if (_isEmpty()) {
      print("Stack underflow");
      return -1;
    }
    return this._top--;
  }

  dynamic peek() {
    if (_isEmpty()) {
      print("Stack underflow");
      return -1;
    }
    return this._data[_top];
  }

  void display() {
    if (_isEmpty()) {
      print("Stack underflow");
      return;
    }
    print("Stack elements : ");
    for (var i = _top; i >= 0; i--) {
      print(this._data[i]);
    }
  }

  dynamic get currentSize => this._top + 1;
}
