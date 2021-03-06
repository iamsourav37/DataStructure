import 'Queue.dart';

void main() {
  Queue q = Queue();
  q.enQueue(12);
  q.enQueue(32);
  q.enQueue(24);
  q.enQueue(5);
  q.enQueue(18);
  q.enQueue(35);

  q.display();

  print("delete element : ${q.deQueue()}");
  print("delete element : ${q.deQueue()}");
  print("delete element : ${q.deQueue()}");

  q.display();
}
