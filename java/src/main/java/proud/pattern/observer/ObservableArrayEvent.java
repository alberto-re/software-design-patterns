package proud.pattern.observer;

public class ObservableArrayEvent<T> {

    private String eventType;
    private T value;

    public void setEventType(String eventType) {
        this.eventType = eventType;
    }

    public void setValue(T value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "ObservableArrayEvent{" +
                "eventType='" + eventType + '\'' +
                ", value=" + value +
                '}';
    }
}
