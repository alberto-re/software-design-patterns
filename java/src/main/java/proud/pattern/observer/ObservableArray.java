package proud.pattern.observer;


import sun.reflect.generics.reflectiveObjects.NotImplementedException;

import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;

public class ObservableArray<T> extends Observable implements Collection<T> {

    private T[] array;
    private int size = 0;

    public ObservableArray(int size) {
        array = (T[])new Object[size];
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean contains(Object o) {
        for (T element : array) {
            if (element.equals(o)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Iterator<T> iterator() {
        throw new NotImplementedException();
    }

    @Override
    public Object[] toArray() {
        return array;
    }

    @Override
    public <T1> T1[] toArray(T1[] a) {
        throw new NotImplementedException();
    }

    @Override
    public boolean add(T t) {
        if (size < array.length) {
            array[size++] = t;
            ObservableArrayEvent<T> event = new ObservableArrayEvent<>();
            event.setEventType("add");
            event.setValue(t);
            update_observers(event);
            return true;
        } else {
            throw new IndexOutOfBoundsException();
        }
    }

    @Override
    public boolean remove(Object o) {
        throw new NotImplementedException();
    }

    @Override
    public boolean containsAll(Collection<?> c) {
        throw new NotImplementedException();
    }

    @Override
    public boolean addAll(Collection<? extends T> c) {
        throw new NotImplementedException();
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        throw new NotImplementedException();
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        throw new NotImplementedException();
    }

    @Override
    public void clear() {
        throw new NotImplementedException();
    }

    @Override
    public String toString() {
        return "ObservableArray{" +
                "array=" + Arrays.toString(array) +
                ", size=" + size +
                '}';
    }

    public static void main(String[] args) {
        ObservableArray<Integer> array = new ObservableArray<>(10);

        MyObserver observer = new MyObserver();
        array.register(observer);
        array.add(5);
        array.add(10);
        array.add(7);
    }
}
