package proud.pattern.strategy;

import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;

public class InetAddressValidation implements ValidationStrategy {

  public boolean isValidAddress(String emailAddress) {
    try {
      new InternetAddress(emailAddress);
      return true;
    } catch (AddressException e) {
      return false;
    }
  }
}
