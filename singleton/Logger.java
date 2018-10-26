import static java.lang.String.format;
import java.time.LocalDateTime;

class Logger {

    private static final String FMT = "%s - %s";
    private static Logger instance = null;
    
    private Logger() { }

    public static Logger getLogger() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    public void log(String msg) {
        System.out.println(format(FMT, LocalDateTime.now(), msg));
    }
    
    public static void main(String args[]) {
        Logger logger = Logger.getLogger();
        logger.log("Logger initialized");
        assert(logger.equals(Logger.getLogger()));
    }

}