package proud.pattern.strategy;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexValidation implements ValidationStrategy {

  // Just for the sake of example
  public static final Pattern EMAIL_ADDRESS_REGEX =
      Pattern.compile("^[A-Z0-9._]+@[A-Z0-9.]+\\.[A-Z]$", Pattern.CASE_INSENSITIVE);

  public boolean isValidAddress(String emailAddress) {
    Matcher matcher = EMAIL_ADDRESS_REGEX.matcher(emailAddress);
    return matcher.find();
  }

}
