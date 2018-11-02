package proud.pattern.observer;

import java.util.ArrayList;
import java.util.List;

abstract class Observable {

    List<Observer> registered_observers = new ArrayList<>();

    public void register(Observer observer) {
        registered_observers.add(observer);
    }

    protected void update_observers(Object args) {
        for (Observer observer : registered_observers) {
            observer.update(this, args);
        }
    }
}