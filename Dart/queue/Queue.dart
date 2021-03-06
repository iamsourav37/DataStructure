class Queue {
  List<int> _queueList = [];

  void enQueue(int data) {
    this._queueList.insert(0, data);
  }

  int deQueue() {
    if (this._queueList.isEmpty) {
      throw Exception("queue is empty");
    } else {
      int deleteData = this._queueList.removeLast();
      return deleteData;
    }
  }

  void display() {
    if (this._queueList.isEmpty) {
      print("Queue is empty");
    } else {
      int length = this._queueList.length;
      for (int i = length - 1; i >= 0; i--) {
        print(this._queueList[i]);
      }
    }
  }
}
