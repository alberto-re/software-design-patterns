package proud.pattern.observer;

public class MyObserver implements Observer {

    @Override
    public void update(Observable observable, Object args) {
        System.out.println(args);
    }
}
